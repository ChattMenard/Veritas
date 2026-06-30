# Evidence Dependency Graph

**Date:** June 29, 2026
**Purpose:** Visual representation of evidence collection priorities and dependencies

---

## 🎯 EVIDENCE COLLECTION PRIORITY

### Priority 1: Public Data (Immediate Access, No ATIP Required)
**Timeline:** This week
**Effort:** Low
**Blockers:** None

1. **US FOIA Pfizer Data**
   - Source: PHMPT v. FDA court docket
   - Script: `scripts/download_us_foia_pfizer_data.py`
   - Output: `EVIDENCE_COLLECTED/US_FOIA_DATA/`
   - Dependencies: None
   - Supports: Phase 1 evidence, legal action template

2. **Lobbying Registry Data**
   - Source: Office of the Lobbying Commissioner
   - Script: `scripts/download_lobbying_registry.py`
   - Output: `EVIDENCE_COLLECTED/LOBBYING_DATA/`
   - Dependencies: None
   - Supports: Timeline analysis, lobbying correlation

3. **CanadaBuys Contract Data**
   - Source: CanadaBuys website
   - Script: `scripts/scrape_canadabuys.py`
   - Output: `EVIDENCE_COLLECTED/CANADABUYS_DATA/`
   - Dependencies: None
   - Supports: Financial track analysis

4. **Corporate Registry Data**
   - Source: Corporations Canada, provincial registries
   - Script: `scripts/corporate_registry_search.py`
   - Output: `EVIDENCE_COLLECTED/CORPORATE_REGISTRY_DATA/`
   - Dependencies: None
   - Supports: Family network investigation

---

### Priority 2: Parliamentary Records (Public, But Require Analysis)
**Timeline:** This week
**Effort:** Low
**Blockers:** None

1. **Parliamentary Question Responses**
   - Source: Parliament of Canada website
   - Document: `PARLIAMENTARY_QUESTION_RESPONSE_ANALYSIS.md`
   - Dependencies: None
   - Supports: Obstruction evidence, legal arguments

---

### Priority 3: ATIP Requests (Requires Filing, 30-90 Day Wait)
**Timeline:** File immediately, expect response in 3-6 months
**Effort:** Medium
**Blockers:** Government response time

1. **Pfizer Vaccine Contract**
   - Template: `ATIP_REQUEST_TEMPLATES.md`
   - Target: PSPC
   - Dependencies: None
   - Supports: Phase 1 evidence, court action

2. **Moderna Vaccine Contract**
   - Template: `ATIP_REQUEST_TEMPLATES.md`
   - Target: PSPC
   - Dependencies: None
   - Supports: Phase 1 evidence, court action

3. **VaccineConnect Deloitte Procurement**
   - Template: `ATIP_REQUEST_TEMPLATES.md`
   - Target: PSPC
   - Dependencies: None
   - Supports: Financial track, corruption evidence

4. **PMPRB Internal Communications**
   - Template: `ATIP_REQUEST_TEMPLATES.md`
   - Target: Health Canada
   - Dependencies: None
   - Supports: Revolving door evidence

5. **CIB Investment Decisions**
   - Template: `ATIP_REQUEST_TEMPLATES.md`
   - Target: CIB
   - Dependencies: None
   - Supports: Financial track, Brookfield evidence

6. **Canada Growth Fund Allocations**
   - Template: `ATIP_REQUEST_TEMPLATES.md`
   - Target: Canada Growth Fund
   - Dependencies: None
   - Supports: Financial track, Brookfield evidence

---

### Priority 4: Legal Actions (Requires Legal Counsel)
**Timeline:** After evidence collection
**Effort:** High
**Blockers:** Legal counsel availability

1. **Ethics Complaint**
   - Template: `ACTION_Draft_Ethics_Complaint_Duclos.md`
   - Dependencies: Ethics disclosures, lobbying data
   - Supports: Regulatory accountability

2. **Competition Act Complaint**
   - Template: `ACTION_Competition_Act_Complaint_Framework.md`
   - Dependencies: Lobbying data, policy documents
   - Supports: Legal accountability

3. **Class Action Intervention**
   - Template: `ACTION_Sakamoto_Class_Action_Intervention.md`
   - Dependencies: FDA redactions, patent secrecy, VISP data
   - Supports: Legal accountability

4. **Court Disclosure Action**
   - Template: `ACTION_Court_Disclosure_Application_Merck_Frosst_Precedent.md`
   - Dependencies: ATIP responses, Merck Frosst precedent
   - Supports: Forced disclosure

---

## 🔗 EVIDENCE DEPENDENCY CHAIN

### Phase 1 Evidence Chain
```
Penn Patents (2017) → NIH/Moderna Agreement (Dec 2019) → DARPA Funding (2013) → Gates Framework (2016)
    ↓
US FOIA Pfizer Data (parallel) → Confirms Pre-Built Platform
    ↓
ATIP: Vaccine Contracts (pending) → Confirms Deployment
```

### Financial Track Evidence Chain
```
Carney Stock Holdings (SEC) → Brookfield Contracts (CanadaBuys) → Parliamentary Questions (Q-735/736/603)
    ↓
Lobbying Registry Data → Map Meetings to Policy Changes
    ↓
ATIP: CIB/Canada Growth Fund (pending) → Confirms Allocation Patterns
```

### Lobbying Track Evidence Chain
```
IMC Lobbying Registry → PMPRB Regulatory Changes → Ministerial Appointments
    ↓
Ethics Disclosures → Revolving Door Patterns
    ↓
ATIP: PMPRB Internal Communications (pending) → Confirms Conflicts
```

### Family Network Evidence Chain
```
Intelcom Corporate Registry → Joly Recusal Disclosures → Contract Awards
    ↓
Irving Corporate Registry → LeBlanc Recusal Timeline → Shipbuilding Contracts
    ↓
Political Donations → Policy Correlation
```

---

## 🎯 EXECUTION ORDER

### Week 1: Immediate Actions
1. Run all data collection scripts (US FOIA, Lobbying, CanadaBuys, Corporate)
2. Document parliamentary question patterns
3. File Ethics Complaint (no dependency on ATIP)
4. File ATIP requests (start clock on 30-90 day timeline)

### Week 2-4: Analysis
1. Run `timeline_analyzer.py` on collected lobbying/contract data
2. Run `evidence_cross_reference_mapper.py` on all data
3. Draft Competition Act complaint
4. Contact Sakamoto counsel

### Month 2-3: Legal Actions
1. File Competition Act complaint
2. File court disclosure action (if ATIP responses inadequate)
3. Coordinate with Sakamoto plaintiffs (if invited)

### Month 4-6: Follow-up
1. Analyze ATIP responses as they arrive
2. Update evidence with new data
3. Consider private prosecution (if smoking gun emerges)
4. Publicize findings

---

## 📊 EVIDENCE MATURITY MATRIX

| Evidence Type | Current Status | Target Status | Path to Target |
|--------------|----------------|---------------|----------------|
| Phase 1 Platform Evidence | ✅ Strong | ✅ Strong | Complete |
| US FOIA Pfizer Data | ⚠️ Not Collected | ✅ Collected | Run script |
| Lobbying Registry Data | ⚠️ Not Collected | ✅ Collected | Run script |
| CanadaBuys Data | ⚠️ Not Collected | ✅ Collected | Run script |
| Corporate Registry Data | ⚠️ Not Collected | ✅ Collected | Run script |
| Parliamentary Questions | ✅ Documented | ✅ Documented | Complete |
| ATIP Vaccine Contracts | ⚠️ Filed/Pending | ✅ Received | Wait 3-6 months |
| ATIP CIB/CGF | ⚠️ Filed/Pending | ✅ Received | Wait 3-6 months |
| Ethics Complaint | ✅ Ready | ✅ Filed | File this week |
| Competition Act Complaint | ⚠️ Template | ✅ Filed | Draft Month 2 |
| Court Disclosure Action | ✅ Template | ✅ Filed | File Month 3 |

---

## 🎯 CRITICAL PATH TO LEGAL ACTION

**Fastest Path to Accountability:**
1. Ethics Complaint → File this week (no dependency on ATIP)
2. Competition Act Complaint → File Month 2 (depends on lobbying data)
3. Court Disclosure Action → File Month 3 (depends on ATIP response or Merck Frosst precedent)

**Slowest Path (Most Comprehensive):**
1. Wait for ATIP responses → 3-6 months
2. Court disclosure action → Uses ATIP responses as evidence
3. Private prosecution → If smoking gun emerges from ATIP

---

*This dependency graph shows evidence collection priorities and the optimal execution order for legal actions.*
