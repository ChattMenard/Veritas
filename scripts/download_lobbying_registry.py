#!/usr/bin/env python3
"""
Download Lobbying Registry Data
Canadian Office of the Lobbying Commissioner provides public access to lobbying data.
This script provides guidance on accessing and processing lobbying registry data.
"""

import requests
from pathlib import Path
import json
import csv

LOBBYING_REGISTRY_BASE_URL = "https://lobbycanada.gc.ca"
LOBBYING_SEARCH_URL = "https://lobbycanada.gc.ca/eic/site/lob-lob.nsf/eng/home"

class LobbyingRegistryDownloader:
    def __init__(self):
        self.output_dir = Path("/home/x99/Desktop/FUCK/EVIDENCE_COLLECTED/LOBBYING_DATA")
        self.output_dir.mkdir(exist_ok=True)
    
    def get_target_organizations(self):
        """Organizations to search in lobbying registry"""
        return {
            "innovative_medicines_canada": "Innovative Medicines Canada",
            "pfizer": "Pfizer Canada",
            "moderna": "Moderna Therapeutics Canada",
            "biontech": "BioNTech",
            "brookfield_asset_management": "Brookfield Asset Management",
            "brookfield_infrastructure": "Brookfield Infrastructure Partners",
            "brookfield_renewable": "Brookfield Renewable Partners",
            "irving": "Irving Shipbuilding",
            "intelcom": "Intelcom Courrier Canada"
        }
    
    def get_search_urls(self):
        """Generate search URLs for target organizations"""
        urls = {}
        for key, name in self.get_target_organizations().items():
            # Lobbying registry uses search parameters
            urls[key] = f"{LOBBYING_SEARCH_URL}?search={name.replace(' ', '+')}"
        return urls
    
    def create_search_guide(self):
        """Create a guide for accessing lobbying registry data"""
        guide = {
            "source": "Office of the Lobbying Commissioner of Canada",
            "website": LOBBYING_SEARCH_URL,
            
            "target_organizations": self.get_target_organizations(),
            
            "search_methods": [
                {
                    "method": "Online Search",
                    "url": LOBBYING_SEARCH_URL,
                    "steps": [
                        "Navigate to lobbying registry website",
                        "Use advanced search function",
                        "Search by organization name",
                        "Filter by date range (2015-2026)",
                        "Download results as CSV"
                    ]
                },
                {
                    "method": "Open Data Portal",
                    "url": "https://open.canada.ca/data/en/dataset/2b4228a3-1c38-4c76-9a8d-6887f455c8e1",
                    "description": "Lobbying registry data available as open data"
                }
            ],
            
            "data_fields_available": [
                "Organization name",
                "Client/Registrant",
                "Subject matter",
                "Date of communication",
                "Government institution lobbied",
                "Public office holder lobbied",
                "Lobbyist name",
                "Communication method"
            ],
            
            "analysis_targets": {
                "innovative_medicines_canada": {
                    "focus": "PMPRB regulatory changes",
                    "key_dates": "2021-2026 (PMPRB guideline changes)",
                    "expected_pattern": "High meeting frequency before regulatory delays"
                },
                "brookfield_entities": {
                    "focus": "CIB/Canada Growth Fund decisions",
                    "key_dates": "2024-2026 (Maple Fund proposal)",
                    "expected_pattern": "Meetings correlate to budget announcements"
                }
            },
            
            "export_formats": ["CSV", "PDF"],
            "recommended_format": "CSV for automated analysis",
            
            "processing_script": "Use scripts/timeline_analyzer.py on downloaded CSV data"
        }
        
        filepath = self.output_dir / "lobbying_registry_search_guide.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(guide, f, indent=2)
        
        print(f"Lobbying registry search guide saved to {filepath}")
    
    def create_csv_template(self):
        """Create a template CSV structure for lobbying data"""
        template = [
            ["Organization", "Client", "Subject", "Date", "Institution", "Public_Office_Holder", "Lobbyist", "Method"]
        ]
        
        filepath = self.output_dir / "lobbying_data_template.csv"
        with open(filepath, 'w', newline='', encoding='utf-8') as f:
            writer = csv.writer(f)
            writer.writerows(template)
        
        print(f"CSV template saved to {filepath}")
    
    def execute(self):
        """Execute the download process"""
        print("Lobbying Registry Data Downloader")
        print("=" * 50)
        print("\nNote: Actual data download requires manual access due to:")
        print("- Lobbying registry may require interactive navigation")
        print("- Search results may need manual filtering")
        print("- Large datasets may timeout automated requests")
        print("\nThis script creates a search guide and CSV template.")
        
        self.create_search_guide()
        self.create_csv_template()
        
        print("\nNext steps:")
        print("1. Review search guide at: EVIDENCE_COLLECTED/LOBBYING_DATA/lobbying_registry_search_guide.json")
        print("2. Manually download lobbying data from registry website")
        print("3. Fill CSV template or use downloaded CSV directly")
        print("4. Run scripts/timeline_analyzer.py on the data")

if __name__ == "__main__":
    downloader = LobbyingRegistryDownloader()
    downloader.execute()
