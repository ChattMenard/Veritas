#!/usr/bin/env python3
"""Analyze Elections Canada donation data for pharma/lobby connections."""
import csv, re, sys
from collections import defaultdict
from pathlib import Path

CSV_PATH = Path(__file__).parent.parent / "EVIDENCE_COLLECTED/PoliticalFinance/od_cntrbtn_de_e.csv"
OUT_PATH = Path(__file__).parent.parent / "EVIDENCE_COLLECTED/PoliticalFinance/pharma_donation_analysis.md"

PHARMA_KEYWORDS = re.compile(
    r"\b(?:pfizer|moderna|astrazeneca|biontech|merck\b|novartis|"
    r"abbott\b|eli\s*lilly|seqirus|sanofi|apotex|teva|"
    r"mylan|sandoz|bausch|gsk\b|glaxosmithkline|glaxo|"
    r"johnson\s*(?:&|\band)?\s*johnson|janssen\s+(?:pharm|inc|canad|biotech)|"
    r"innovative\s+medicines\s+canada|rx\s*&\s*d\b|bio\s*syntech|biolyse)",
    re.IGNORECASE
)

LOBBY_KEYWORDS = re.compile(
    r"\b(?:michel\s+fralick|christiane\s+hamelin|terry\s+digby|"
    r"bruno\s+marie|pascale\s+dion|glaxosmithkline|gsk\s*canad|"
    r"pfizer\s*canad|astrazeneca\s*canad|merck\s*canad|novartis\s*canad|"
    r"johnson\s*(?:&|\band)?\s*johnson\s*canad|janssen\s*canad)",
    re.IGNORECASE
)

TARGET_RECIPIENTS = re.compile(
    r"duclos|carney|trudeau|freeland|hajdu|tam|"
    r"anand|champagne|leblanc|morneau",
    re.IGNORECASE
)

pharma_hits = []
lobby_hits = []
recipient_hits = defaultdict(lambda: defaultdict(float))
party_pharma = defaultdict(float)
year_pharma = defaultdict(float)
party_lobby = defaultdict(float)

print(f"Scanning {CSV_PATH} ...", flush=True)

with open(CSV_PATH, encoding="utf-8-sig", errors="replace") as f:
    reader = csv.DictReader(f)
    for i, row in enumerate(reader):
        contributor = row.get("Contributor name", "") or ""
        recipient   = row.get("Recipient", "") or ""
        party       = row.get("Political Party of Recipient", "") or ""
        date        = row.get("Fiscal/Election date", "") or ""
        year        = date[:4] if date else "?"
        contrib_type = row.get("Contributor type", "") or ""
        try:
            amount = float(row.get("Monetary amount", "0").replace(",", "").strip() or 0)
        except ValueError:
            amount = 0.0

        if PHARMA_KEYWORDS.search(contributor):
            pharma_hits.append({
                "contributor": contributor.strip(),
                "recipient":   recipient.strip(),
                "party":       party.strip(),
                "year":        year,
                "amount":      amount,
                "type":        contrib_type.strip(),
            })
            party_pharma[party.strip()] += amount
            year_pharma[year] += amount

        if LOBBY_KEYWORDS.search(contributor):
            lobby_hits.append({
                "contributor": contributor.strip(),
                "recipient":   recipient.strip(),
                "party":       party.strip(),
                "year":        year,
                "amount":      amount,
                "type":        contrib_type.strip(),
            })
            party_lobby[party.strip()] += amount

        if TARGET_RECIPIENTS.search(recipient) and amount > 0:
            recipient_hits[recipient.strip()][contributor.strip()] += amount

        if i % 500_000 == 0:
            print(f"  {i:,} rows processed ...", flush=True)

# ── Build report ────────────────────────────────────────────────────────────
lines = [
    "# Pharma & Lobby Political Donation Analysis",
    "",
    f"**Source:** Elections Canada Open Data ({CSV_PATH.name})",
    f"**Rows scanned:** {i+1:,}",
    f"**Pharma keyword donations found:** {len(pharma_hits)}",
    f"**Lobby keyword donations found:** {len(lobby_hits)}",
    "",
    "## Pharma Donations by Party",
    "",
    "| Party | Total ($) |",
    "| ----- | --------- |",
    *[f"| {p} | {v:,.2f} |" for p, v in sorted(party_pharma.items(), key=lambda x: -x[1])],
    "",
    "## Pharma Donations by Year",
    "",
    "| Year | Total ($) |",
    "| ---- | --------- |",
    *[f"| {y} | {v:,.2f} |" for y, v in sorted(year_pharma.items())],
    "",
    "## All Pharma-Linked Donation Records",
    "",
    "| Contributor | Type | Recipient | Party | Year | Amount ($) |",
    "| ----------- | ---- | --------- | ----- | ---- | ---------- |",
    *[f"| {h['contributor']} | {h['type']} | {h['recipient']} | {h['party']} | {h['year']} | {h['amount']:,.2f} |"
      for h in sorted(pharma_hits, key=lambda x: -x["amount"])],
    "",
    "## Lobby-Linked Donation Records",
    "",
    "| Contributor | Type | Recipient | Party | Year | Amount ($) |",
    "| ----------- | ---- | --------- | ----- | ---- | ---------- |",
    *[f"| {h['contributor']} | {h['type']} | {h['recipient']} | {h['party']} | {h['year']} | {h['amount']:,.2f} |"
      for h in sorted(lobby_hits, key=lambda x: -x["amount"])],
    "",
    "## Donations TO Target Politicians (all sources)",
    "",
]

for recipient, donors in sorted(recipient_hits.items()):
    total = sum(donors.values())
    lines += [
        f"### {recipient}  (total: ${total:,.2f})",
        "",
        "| Contributor | Amount ($) |",
        "| ----------- | ---------- |",
        *[f"| {d} | {a:,.2f} |" for d, a in sorted(donors.items(), key=lambda x: -x[1])[:50]],
        "",
    ]

OUT_PATH.write_text("\n".join(lines), encoding="utf-8")
print(f"\nDone. Report written to {OUT_PATH}")
print(f"Pharma hits: {len(pharma_hits)}, Target politicians: {len(recipient_hits)}")
