"""Visualization data router for evidence dashboard."""

from fastapi import APIRouter
from typing import Dict, List, Any

router = APIRouter(prefix="/api/visualization", tags=["visualization"])

# Inline data to avoid file dependency issues in Railway container
TIMELINE_EVENTS = [
  {"date": "2005-01-01", "year": 2005, "title": "Katalin Karikó and Drew Weissman publish foundational mRNA paper at University of Pennsylvania", "description": "Katalin Karikó and Drew Weissman publish foundational mRNA paper at University of Pennsylvania", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2009-01-01", "year": 2009, "title": "Dr. Thomas Madden (Cullis collaborator) founds AlCana Technologies (later Acuitas)", "description": "Dr. Thomas Madden (Cullis collaborator) founds AlCana Technologies (later Acuitas)", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2010-01-01", "year": 2010, "title": "Penn exclusively licenses patent to mRNA RiboTherapeutics (Madison, WI)", "description": "Penn exclusively licenses patent to mRNA RiboTherapeutics (Madison, WI)", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2012-01-01", "year": 2012, "title": "Karikó \"kicked out\" of Penn, \"forced to retire\" - joins BioNTech in Germany", "description": "Karikó \"kicked out\" of Penn, \"forced to retire\" - joins BioNTech in Germany", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2012-01-01", "year": 2012, "title": "Arbutus licenses LNP patents to Acuitas", "description": "Arbutus licenses LNP patents to Acuitas", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2013-03-22", "title": "DARPA awards Moderna **~$1.4 million** for \"modified RNA technology for production of antibodies for", "description": "DARPA awards Moderna **~$1.4 million** for \"modified RNA technology for production of antibodies for immune prophylaxis\"", "category": "funding", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2013-10-02", "title": "DARPA awards Moderna **up to $25 million** under ADEPT-PROTECT program", "description": "DARPA awards Moderna **up to $25 million** under ADEPT-PROTECT program", "category": "funding", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2016-01-01", "year": 2016, "title": "mRNA RiboTherapeutics sublicenses to affiliate Cellscript LLC", "description": "mRNA RiboTherapeutics sublicenses to affiliate Cellscript LLC", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2016-01-01", "year": 2016, "title": "Acuitas grants sublicense to Moderna; Arbutus declares it improper", "description": "Acuitas grants sublicense to Moderna; Arbutus declares it improper", "category": "funding", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2016-01-01", "year": 2016, "title": "Acuitas enters development agreement with CureVac (including LNP patents)", "description": "Acuitas enters development agreement with CureVac (including LNP patents)", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2017-01-10", "title": "Dr. Anthony Fauci delivers keynote at Georgetown University", "description": "Dr. Anthony Fauci delivers keynote at Georgetown University", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2017-06-26", "title": "Cellscript sublicenses to **Moderna** (BEFORE pandemic)", "description": "Cellscript sublicenses to **Moderna** (BEFORE pandemic)", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2017-07-14", "title": "Cellscript sublicenses to **BioNTech** (BEFORE pandemic)", "description": "Cellscript sublicenses to **BioNTech** (BEFORE pandemic)", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2018-01-01", "year": 2018, "title": "Litigation settled between Acuitas and Arbutus; Moderna begins filing patent challenges", "description": "Litigation settled between Acuitas and Arbutus; Moderna begins filing patent challenges", "category": "patent", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2019-10-18", "title": "Johns Hopkins Center for Health Security, **World Economic Forum**, and **Bill & Melinda Gates Found", "description": "Johns Hopkins Center for Health Security, **World Economic Forum**, and **Bill & Melinda Gates Foundation** host \"Event 201\"", "category": "simulation", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2019-12-12", "title": "Dr. Ralph Baric at UNC signs agreement to receive \"mRNA coronavirus vaccine candidates developed and", "description": "Dr. Ralph Baric at UNC signs agreement to receive \"mRNA coronavirus vaccine candidates developed and jointly-owned by NIAID and Moderna\"", "category": "agreement", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2019-12-16", "title": "UNC's Jacqueline Quay signs", "description": "UNC's Jacqueline Quay signs", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2019-12-17", "title": "Moderna's Sunny Himansu and Shaun Ryan sign", "description": "Moderna's Sunny Himansu and Shaun Ryan sign", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2019-12-31", "title": "WHO \"becomes aware\" of viral pneumonia in Wuhan", "description": "WHO \"becomes aware\" of viral pneumonia in Wuhan", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2020-01-09", "title": "WHO reports \"novel coronavirus\"", "description": "WHO reports \"novel coronavirus\"", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2020-01-10", "title": "SARS-CoV-2 genome published", "description": "SARS-CoV-2 genome published", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2020-01-13", "title": "cGMP production initiated (3 days)", "description": "cGMP production initiated (3 days)", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2020-03-16", "title": "First Phase 1 trial participant vaccinated (**66 days** after sequence)", "description": "First Phase 1 trial participant vaccinated (**66 days** after sequence)", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"date": "2020-05-29", "title": "Phase 2 begins (**74 days** after Phase 1)", "description": "Phase 2 begins (**74 days** after Phase 1)", "category": "general", "source_document": "Pre_Pandemic_Connections_The_Platform.md"}
]

NETWORK_NODES = [
  {"id": "acuitas", "name": "Acuitas", "type": "pharma", "influence_score": 85},
  {"id": "anthony_fauci", "name": "Anthony Fauci", "type": "person", "influence_score": 60},
  {"id": "arbutus", "name": "Arbutus", "type": "pharma", "influence_score": 85},
  {"id": "bill_and_melinda_gates_foundation", "name": "Bill & Melinda Gates Foundation", "type": "foundation", "influence_score": 70},
  {"id": "barney_graham", "name": "Barney Graham", "type": "person", "influence_score": 60},
  {"id": "biontech", "name": "BioNTech", "type": "pharma", "influence_score": 85},
  {"id": "cepi", "name": "CEPI", "type": "foundation", "influence_score": 70},
  {"id": "cellscript", "name": "Cellscript", "type": "pharma", "influence_score": 85},
  {"id": "darpa", "name": "DARPA", "type": "government", "influence_score": 75},
  {"id": "drew_weissman", "name": "Drew Weissman", "type": "person", "influence_score": 60},
  {"id": "gates_foundation", "name": "Gates Foundation", "type": "foundation", "influence_score": 70},
  {"id": "inex", "name": "Inex", "type": "pharma", "influence_score": 85},
  {"id": "johns_hopkins", "name": "Johns Hopkins", "type": "government", "influence_score": 75},
  {"id": "katalin_karikó", "name": "Katalin Karikó", "type": "person", "influence_score": 60},
  {"id": "moderna", "name": "Moderna", "type": "pharma", "influence_score": 85},
  {"id": "niaid", "name": "NIAID", "type": "government", "influence_score": 75},
  {"id": "nih", "name": "NIH", "type": "government", "influence_score": 75},
  {"id": "penn", "name": "Penn", "type": "government", "influence_score": 75},
  {"id": "pfizer", "name": "Pfizer", "type": "pharma", "influence_score": 85},
  {"id": "pieter_cullis", "name": "Pieter Cullis", "type": "person", "influence_score": 60},
  {"id": "ralph_baric", "name": "Ralph Baric", "type": "person", "influence_score": 60},
  {"id": "tekmira", "name": "Tekmira", "type": "pharma", "influence_score": 85},
  {"id": "thomas_madden", "name": "Thomas Madden", "type": "person", "influence_score": 60},
  {"id": "ubc", "name": "UBC", "type": "government", "influence_score": 75},
  {"id": "unc", "name": "UNC", "type": "government", "influence_score": 75},
  {"id": "university_of_british_columbia", "name": "University of British Columbia", "type": "organization", "influence_score": 50},
  {"id": "university_of_pennsylvania", "name": "University of Pennsylvania", "type": "government", "influence_score": 75},
  {"id": "wef", "name": "WEF", "type": "foundation", "influence_score": 70},
  {"id": "world_economic_forum", "name": "World Economic Forum", "type": "foundation", "influence_score": 70},
  {"id": "mrna_ribotherapeutics", "name": "mRNA RiboTherapeutics", "type": "organization", "influence_score": 50}
]

FINANCIAL_FLOWS = [
  {"source": "Penn", "target": "BioNTech", "amount": 1200.0, "amount_display": "$1.2 billion", "category": "funding", "description": "- BioNTech paid Hospital of University of Pennsylvania **$1.2 billion** in 10 royalty payments (2021-2022)", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"source": "DARPA", "target": "Moderna", "amount": 1.4, "amount_display": "$1.4 million", "category": "funding", "description": "- **March 22, 2013**: DARPA awards Moderna **~$1.4 million** for \"modified RNA technology for production of antibodies for immune prophylaxis\"", "source_document": "Pre_Pandemic_Connections_The_Platform.md"},
  {"source": "DARPA", "target": "Moderna", "amount": 25.0, "amount_display": "$25 million", "category": "funding", "description": "- **October 2, 2013**: DARPA awards Moderna **up to $25 million** under ADEPT-PROTECT program", "source_document": "Pre_Pandemic_Connections_The_Platform.md"}
]

LOBBYING_MEETINGS = [
  {"date": "2022-02-15", "attendees": ["Simon Kennedy", "Deputy Minister"], "subject": "Industry, IP", "description": "Simon Kennedy (Deputy Minister, ISED) - Industry, IP", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2022-06-09", "attendees": ["Sebastien Bock", "Sandenga Yeba", "Senior Policy"], "subject": "Health, Industry, S&T", "description": "Jean-Sebastien Bock (Director of Policy, Minister's Office) + Sandenga Yeba (Senior Policy Advisor, Minister's Office) - Health, Industry, S&T", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2022-06-16", "attendees": ["Stephen Lucas", "Deputy Minister", "Health Canada"], "subject": "Health, Industry, Trade", "description": "Stephen Lucas (Deputy Minister, Health Canada) - Health, Industry, Trade", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2022-06-27", "attendees": ["Stephen Lucas", "Deputy Minister", "Health Canada", "Nancy Hamzawi", "Health Canada"], "subject": "Health, Industry, IP, Trade, S&T", "description": "Stephen Lucas (Deputy Minister, Health Canada) + Nancy Hamzawi (ADM, Health Canada) - Health, Industry, IP, Trade, S&T", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2022-06-28", "attendees": ["Simon Kennedy", "Deputy Minister"], "subject": "Health, Industry, IP, Trade, S&T", "description": "Simon Kennedy (Deputy Minister, ISED) - Health, Industry, IP, Trade, S&T", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2023-01-11", "attendees": ["Patrick Cousineau", "Greg Mc", "Bradley Bekkeheim", "Damien Kurek"], "subject": "Health, Industry, S&T", "description": "Patrick Cousineau (MP Assistant, Greg McLean) + Bradley Bekkeheim (MP Assistant, Damien Kurek) - Health, Industry, S&T", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2023-01-16", "attendees": ["Jamie Kippen", "Sandenga Yeba", "Senior Policy"], "subject": "Health", "description": "Jamie Kippen (Chief of Staff, Minister's Office) + Sandenga Yeba (Senior Policy Advisor, Minister's Office) - Health", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2023-01-27", "attendees": ["Stephen Lucas", "Deputy Minister", "Health Canada"], "subject": "Health, Industry", "description": "Stephen Lucas (Deputy Minister of Health, Health Canada) - Health, Industry", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"},
  {"date": "2023-02-09", "attendees": [], "subject": "Health, Industry, S&T", "description": "Flordeliz (Gigi) Osler (Senator) - Health, Industry, S&T", "lobbying_organization": "Innovative Medicines Canada", "source_document": "LOBBYING_MEETINGS_ANALYSIS.md"}
]

@router.get("/timeline")
async def get_timeline_events() -> Dict[str, Any]:
    """Get timeline events for visualization."""
    return {"events": TIMELINE_EVENTS, "count": len(TIMELINE_EVENTS)}

@router.get("/network")
async def get_network_data() -> Dict[str, Any]:
    """Get network graph data (nodes and edges)."""
    edges = []
    for flow in FINANCIAL_FLOWS:
        edges.append({
            "source": flow["source"].lower().replace(" ", "_"),
            "target": flow["target"].lower().replace(" ", "_"),
            "type": "funding",
            "amount": flow["amount"],
            "category": flow["category"]
        })
    return {"nodes": NETWORK_NODES, "edges": edges, "node_count": len(NETWORK_NODES), "edge_count": len(edges)}

@router.get("/financial-flow")
async def get_financial_flows() -> Dict[str, Any]:
    """Get financial flow data for Sankey diagram."""
    return {"flows": FINANCIAL_FLOWS, "count": len(FINANCIAL_FLOWS)}

@router.get("/lobbying")
async def get_lobbying_meetings() -> Dict[str, Any]:
    """Get lobbying meeting data for heatmap."""
    return {"meetings": LOBBYING_MEETINGS, "count": len(LOBBYING_MEETINGS)}

@router.get("/all")
async def get_all_visualization_data() -> Dict[str, Any]:
    """Get all visualization data in single response."""
    return {
        "timeline_events": TIMELINE_EVENTS,
        "network_nodes": NETWORK_NODES,
        "financial_flows": FINANCIAL_FLOWS,
        "lobbying_meetings": LOBBYING_MEETINGS,
        "metadata": {
            "extracted_at": "2026-06-30",
            "total_events": len(TIMELINE_EVENTS),
            "total_nodes": len(NETWORK_NODES),
            "total_flows": len(FINANCIAL_FLOWS),
            "total_meetings": len(LOBBYING_MEETINGS)
        }
    }

@router.get("/vaccine-waste")
async def get_vaccine_waste_data() -> Dict[str, Any]:
    """Get vaccine waste data for bar chart."""
    # Static data from evidence files
    return {
        "purchased": 169000000,
        "administered": 85000000,
        "wasted": 40000000,
        "expired": 13600000,
        "donated": 15300000,
        "waste_cost_billion": 1.2,
        "per_dose_cost": 25,
        "source": "Auditor General Report 6 (Nov 2022), Report 1 (May 2023)"
    }

@router.get("/revolving-door")
async def get_revolving_door_data() -> Dict[str, Any]:
    """Get revolving door personnel data."""
    # Static data from ethics disclosures investigation
    return {
        "individuals": [
            {
                "name": "Pamela Fralick",
                "from": "Innovative Medicines Canada",
                "to": "Government Advisor",
                "date": "2021",
                "conflict_score": 85
            }
        ],
        "source": "ETHICS_DISCLOSURES_INVESTIGATION.md"
    }
