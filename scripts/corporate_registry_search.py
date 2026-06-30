#!/usr/bin/env python3
"""
Corporate Registry Search
Search federal and provincial corporate registries for ownership structures.
This script provides guidance on accessing corporate registry data.
"""

import requests
from pathlib import Path
import json
import csv

FEDERAL_REGISTRY_URL = "https://ised-isde.canada.ca/site/ised/en/doing-business-with-canada/corporate-canada/corporations-canada"

class CorporateRegistrySearch:
    def __init__(self):
        self.output_dir = Path("/home/x99/Desktop/FUCK/EVIDENCE_COLLECTED/CORPORATE_REGISTRY_DATA")
        self.output_dir.mkdir(exist_ok=True)
    
    def get_target_entities(self):
        """Entities to search in corporate registries"""
        return {
            "federal": {
                "intelcom_courrier_canada": "Intelcom Courrier Canada Inc.",
                "corporation_number": "1259515-0"
            },
            "provincial": {
                "nova_scotia": {
                    "irving_shipbuilding": "Irving Shipbuilding Inc.",
                    "registry": "Nova Scotia Registry of Joint Stock Companies"
                },
                "new_brunswick": {
                    "irving_entities": "Irving",
                    "registry": "New Brunswick Corporate Registry"
                }
            }
        }
    
    def get_search_guide(self):
        """Create guide for corporate registry searches"""
        guide = {
            "federal_registry": {
                "source": "Corporations Canada",
                "website": FEDERAL_REGISTRY_URL,
                "database": "Corporations Canada Online Database",
                "search_url": "https://ised-isde.canada.ca/site/ised/en/corporations-canada-online-database-search",
                
                "target_entities": {
                    "intelcom_courrier_canada": {
                        "federal_corporation_number": "1259515-0",
                        "status": "Active",
                        "amalgamation_date": "January 1, 2021",
                        "key_info_needed": ["Directors", "Shareholders", "Ownership structure"]
                    }
                },
                
                "data_fields_available": [
                    "Corporation name",
                    "Corporation number",
                    "Status",
                    "Incorporation date",
                    "Directors",
                    "Shareholders (if public)",
                    "Registered office address"
                ]
            },
            
            "provincial_registries": {
                "nova_scotia": {
                    "registry": "Nova Scotia Registry of Joint Stock Companies",
                    "website": "https://novascotia.ca/snsmr/access/nsr/",
                    "target": "Irving Shipbuilding"
                },
                "new_brunswick": {
                    "registry": "New Brunswick Corporate Registry",
                    "website": "https://snb.ca/en/corporate-registry",
                    "target": "Irving entities"
                },
                "quebec": {
                    "registry": "Registraire des entreprises du Québec",
                    "website": "https://www.registreentreprises.gouv.qc.ca/",
                    "target": "Brookfield entities"
                }
            },
            
            "search_methods": [
                {
                    "method": "Online Database Search",
                    "steps": [
                        "Navigate to corporate registry website",
                        "Search by corporation number or name",
                        "Download corporate profile",
                        "Extract director and shareholder information"
                    ]
                },
                {
                    "method": "ATIP Request",
                    "description": "If information is not publicly available",
                    "target": "Innovation, Science and Economic Development Canada"
                }
            ],
            
            "investigation_targets": {
                "intelcom_joly_connection": {
                    "objective": "Identify Mélanie Joly's brother's role in Intelcom",
                    "search": "Intelcom Courrier Canada Inc. directors and shareholders",
                    "cross_reference": "Joly's recusal disclosures"
                },
                "irving_leblanc_connection": {
                    "objective": "Map Irving family ownership structure",
                    "search": "Irving Shipbuilding and related entities",
                    "cross_reference": "Dominic LeBlanc's recusal timeline"
                },
                "brookfield_carney_connection": {
                    "objective": "Identify Brookfield entities in Carney ethics screens",
                    "search": "Brookfield subsidiaries and related entities",
                    "cross_reference": "Carney's blind trust mechanism"
                }
            },
            
            "processing_script": "Use scripts/evidence_cross_reference_mapper.py on extracted data"
        }
        
        filepath = self.output_dir / "corporate_registry_search_guide.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(guide, f, indent=2)
        
        print(f"Corporate registry search guide saved to {filepath}")
    
    def create_csv_template(self):
        """Create CSV template for corporate data"""
        template = [
            ["Entity_Name", "Jurisdiction", "Corporation_Number", "Status", "Directors", "Shareholders", "Registered_Address"]
        ]
        
        filepath = self.output_dir / "corporate_registry_data_template.csv"
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(template)
        
        print(f"CSV template saved to {filepath}")
    
    def execute(self):
        """Execute the search process"""
        print("Corporate Registry Search")
        print("=" * 50)
        print("\nNote: Actual data search requires manual access due to:")
        print("- Corporate registries may require interactive navigation")
        print("- Some information may not be publicly available")
        print("- Shareholder information may be private")
        print("\nThis script creates a search guide and CSV template.")
        
        self.get_search_guide()
        self.create_csv_template()
        
        print("\nNext steps:")
        print("1. Review search guide at: EVIDENCE_COLLECTED/CORPORATE_REGISTRY_DATA/corporate_registry_search_guide.json")
        print("2. Manually search corporate registries for target entities")
        print("3. Fill CSV template with extracted data")
        print("4. Run scripts/evidence_cross_reference_mapper.py to analyze connections")

if __name__ == "__main__":
    searcher = CorporateRegistrySearch()
    searcher.execute()
