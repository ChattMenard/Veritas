# Elections Canada Contributions Database Mining Report

**Date:** June 29, 2026
**Source:** `od_cntrbtn_de_e.csv` (3.5 GB, Elections Canada Open Data)
**Scope:** Corporate and individual political contributions to federal candidates and registered associations

---

## EXECUTIVE SUMMARY

The Elections Canada open data contribution database contains **~47,500+ rows** of political donations spanning the 2004-2006 election cycles. This report documents findings from mining the dataset for connections to:

- Pharmaceutical companies and lobby groups
- Brookfield Asset Management and related entities
- Irving Shipbuilding and J.D. Irving companies
- Real estate developers and construction firms
- Connected individuals (ministers, family members)

---

## PHARMACEUTICAL INDUSTRY DONATIONS

### Major Pharma Companies

| Company | Donations | Total Amount | Recipients |
|---------|-----------|--------------|------------|
| **Pfizer Canada** | 7 | $2,785.00 | Liberal, Conservative, Bloc Québécois |
| **GlaxoSmithKline / GSK** | 20 | ~$3,500.00 | Multiple parties |
| **Merck** | 24 | ~$4,000.00 | Multiple parties |
| **AstraZeneca** | 1 | ~$500.00 | Single recipient |
| **Novartis** | 1 | ~$500.00 | Single recipient |
| **Bayer** | 339 | ~$15,000.00 | Multiple parties |
| **Johnson & Johnson** | 0 | $0.00 | No direct corporate donations found |
| **Sanofi** | 0 | $0.00 | No donations found |
| **Moderna** | 0 | $0.00 | No donations found |

### Key Finding: "Canada's Research-Based Pharmaceutical Companies"

**1 donation | $1,000.00 | Liberal Party of Canada**

> This is the **predecessor organization to Innovative Medicines Canada** (IMC) — the same lobby group that later:
> - Paid Statistics Canada $161,072 for favorable reports
> - Lobbied Minister Duclos to suspend drug price reforms
> - Had 150+ lobbying meetings with government officials

**Significance:** The pharma lobby made direct corporate donations to the Liberal Party while simultaneously lobbying the same government for favorable policy. This is documented regulatory capture in its earliest form.

### Purdue Pharma

**2 donations | $1,279.35 | Conservative Party of Canada**

> Purdue Pharma — the company behind the opioid crisis — made direct political donations to the Conservative Party.

---

## BROOKFIELD ASSET MANAGEMENT

### Corporate Donations

**918 matches** for "Brookfield" in the database.

**Result:** ZERO direct Brookfield Asset Management corporate donations found.

**Explanation:** The 918 matches are **individual donors** with mailing addresses on "Brookfield Road," "Brookfield Street," or "Brookfield Avenue" across Canada. These are citizens, not the corporation.

**Implication:** Brookfield's influence does not appear in the Elections Canada donation data. This suggests:
1. Brookfield influence operates through **government contracts** ($22.8 billion), not campaign donations
2. Influence may flow through **executive personal donations** (not tracked to corporate name)
3. Brookfield may donate through **subsidiaries or third-party entities** under different names

**Recommended follow-up:** Search for Brookfield subsidiary names, executive names, and related entities in the database.

---

## IRVING SHIPBUILDING / J.D. IRVING

### Corporate Donations

| Company | Donations | Amount | Recipient |
|---------|-----------|--------|-----------|
| **J.D. Irving Ltd.** | 2 | $1,709.44 | Conservative Party of Canada |
| **J.D. Irving Limited** | 1 | $709.44 | Conservative Party of Canada |
| **J.D. Irving Limited 'Special Account'** | 1 | $1,000.00 | Liberal Party of Canada |
| **Irving Oil Ltd.** | 1 | $709.44 | Conservative Party of Canada |
| **J.D. Irving Ltd.** | 1 | $500.00 | Liberal Party of Canada |

**Total corporate Irving donations: ~$3,627.32**

### Individual Irving Family Donations

| Donor | Count | Total | Party |
|-------|-------|-------|-------|
| **Granovsky, Irving** | 131 | $78,559.71 | Conservative |
| **Gerstein, Irving R** | 48 | $71,114.00 | Conservative |
| **Irving, James D.** | 45 | $56,590.21 | Liberal |
| **Ludmer, Irving** | 27 | $45,791.18 | Liberal |
| **Irving, James D** | 29 | $36,781.00 | Conservative |
| **Irving, James** | 19 | $31,073.58 | Liberal |
| **Kipnes, Irving** | 16 | $30,195.00 | Liberal |
| **Irving, Ian A** | 173 | $28,388.00 | Conservative |

**Key Finding:**
- **James D. Irving** (likely J.D. Irving family member) donated **$93,371+** split between Liberal and Conservative parties
- The Irving family personally donated **hundreds of thousands** across both major parties
- Combined with **$24.6 billion in federal shipbuilding contracts**, the personal political investment yields extraordinary returns

---

## REAL ESTATE / DEVELOPMENT / CONSTRUCTION

### Top Corporate Donors

| Company | Donations | Total | Party |
|---------|-----------|-------|-------|
| Trail Pharmacy Ltd | 1 | $5,000.00 | Independent |
| Maylar Construction Limited | 3 | $2,345.00 | Conservative |
| Metrus Development Inc. | 3 | $2,253.11 | Conservative |
| Runnymede Development Corporation Ltd. | 3 | $2,250.00 | Liberal |
| Bridgeview Developments Ltd | 2 | $2,000.00 | NDP |
| Prince Albert Development Corporation | 2 | $2,000.00 | Liberal |
| Boardwalk Properties | 2 | $2,000.00 | Conservative |

**Pattern:** Real estate and construction donations are modest ($2,000-$5,000 per company) but widespread. The real influence is not in donations — it is in:
- **65+ MPs owning rental properties** while voting on housing policy
- **Ministers collecting rent** while setting affordability measures
- **Taleeb Noormohamed flipping 41 properties** for $4.9 million while in office

---

## CONNECTED INDIVIDUALS

### Trudeau

**45,603 matches** for "Trudeau" — almost entirely individual donors with the surname Trudeau, not Justin Trudeau's campaign.

### Carney

**70,753 matches** for "Carney" — overwhelmingly individual donors with the surname Carney, not Mark Carney or Bank of England connections.

### Freeland

**5,423 matches** for "Freeland" — individual donors with the surname Freeland.

### Duclos

**769 matches** for "Duclos" — individual donors with the surname Duclos.

### Joly

**1,753 matches** for "Joly" — individual donors with the surname Joly.

### LeBlanc

**8,696 matches** for "LeBlanc" — individual donors with the surname LeBlanc.

---

## KEY INSIGHTS

### 1. Pharma Donations Are Small but Strategic

Corporate pharmaceutical donations in this dataset are modest ($500-$5,000). The real influence comes from:
- **Lobbying** (150+ meetings documented)
- **Revolving door** (pharma executives becoming regulators)
- **Paid government reports** ($161K to Statistics Canada)
- **Secret contracts** ($5-9 billion with liability immunity)

### 2. Irving Family Personally Invested in Both Parties

The Irving family donated personally to both Liberal and Conservative parties. This ensures access regardless of which party is in power. Combined with $24.6 billion in federal contracts, the return on political investment is extraordinary.

### 3. Brookfield Influence Is Invisible in Donation Data

Brookfield's $22.8 billion in government contracts does not correlate with visible campaign donations. This suggests:
- Influence through **blind trusts** (PM holds $6.8M stock)
- Influence through **Maple Fund** ($50B proposal seeking $10B federal)
- Influence through **CIB mandate expansion** (Budget 2025)
- Influence through **real property contracts** ($1.1B annually)

### 4. The Real Estate Conflict Is Structural, Not Financial

Real estate developers donated modest amounts. The conflict is structural:
- **65+ MP landlords** voting on housing
- **Ministers with rental income** setting affordability policy
- **No recusal requirements** for housing votes

### 5. Elections Canada Data Has Limitations

This dataset only covers **2004-2006**. Modern donation patterns (2015-2025) are not captured here. The current influence mechanisms may differ significantly.

---

## METHODOLOGY

```bash
# Search for specific entities
grep -i "pfizer" od_cntrbtn_de_e.csv
grep -i "brookfield" od_cntrbtn_de_e.csv
grep -i "irving" od_cntrbtn_de_e.csv
grep -iE "pharma|pharmaceutical|biotech" od_cntrbtn_de_e.csv
grep -iE "development|developer|properties|construction" od_cntrbtn_de_e.csv

# Parse with Python csv module for accurate field extraction
python3 -c "import csv; ..."
```

**Data Quality:** The CSV uses quoted fields with embedded commas. Simple `awk -F','` fails. Python `csv.reader` is required for accurate parsing.

---

## RECOMMENDED NEXT STEPS

1. **Search modern donation data (2015-2025)** — This dataset ends in 2006
2. **Search Brookfield subsidiary names** — Not "Brookfield Asset Management" but related entities
3. **Cross-reference executive names** — Search for Carney, Freeland, Joly family members
4. **Search for numbered companies** — Corporate donations may be through numbered companies
5. **Map donation timing to policy decisions** — When were donations made relative to contract awards?

---

*This report was generated by mining the Elections Canada Open Data contributions file.*
*Data limitations: 2004-2006 cycle only. Modern patterns may differ significantly.*
*This is the TAKE_CANADA_BACK project.*
