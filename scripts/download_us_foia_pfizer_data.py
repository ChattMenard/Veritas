#!/usr/bin/env python3
"""
Download US FOIA Pfizer Data
PHMPT v. FDA forced release of Pfizer vaccine documents.
This script provides guidance on accessing these documents.
"""

import requests
from pathlib import Path
import json

# US FDA FOIA documents are publicly available
# PHMPT v. FDA, No. 1:21-cv-01592 (D.D.C. 2022)

FDA_FOIA_BASE_URL = "https://fda.gov/files"
PHMPT_DOCKET_URL = "https://www.courtlistener.com/docket/60876556/public-health-and-medical-professionals-for-transparency-v-fda/"

class USFOIADownloader:
    def __init__(self):
        self.output_dir = Path("/home/x99/Desktop/FUCK/EVIDENCE_COLLECTED/US_FOIA_DATA")
        self.output_dir.mkdir(exist_ok=True)
    
    def get_document_urls(self):
        """
        PHMPT v. FDA released documents include:
        - Pfizer-BioNTech COVID-19 Vaccine product information
        - Adverse event reports
        - Clinical trial data
        - Manufacturing documents
        """
        documents = {
            "pfizer_product_monograph": "https://www.pfizer.com/files/products/US_Comirnaty_Prescribing_Information.pdf",
            "fda_briefing_document": "https://www.fda.gov/media/153793/download",
            "clinical_trial_protocol": "https://clinicaltrials.gov/ct2/show/NCT04368728",
            "phmpt_docket": PHMPT_DOCKET_URL
        }
        return documents
    
    def download_document(self, url, filename):
        """Download a document from URL"""
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
            
            filepath = self.output_dir / filename
            with open(filepath, 'wb') as f:
                f.write(response.content)
            
            print(f"Downloaded: {filename}")
            return True
        except Exception as e:
            print(f"Failed to download {url}: {e}")
            return False
    
    def create_research_guide(self):
        """Create a guide for accessing US FOIA data"""
        guide = {
            "case": "PHMPT v. FDA",
            "docket_number": "1:21-cv-01592 (D.D.C. 2022)",
            "court": "United States District Court for the District of Columbia",
            "outcome": "Court ordered FDA to release Pfizer vaccine documents at 55,000 pages/month",
            
            "key_documents_available": [
                "Pfizer-BioNTech COVID-19 Vaccine Prescribing Information",
                "FDA Advisory Committee Briefing Documents",
                "Clinical Trial Protocols and Results",
                "Adverse Event Reports (VAERS)",
                "Manufacturing and Quality Control Documents"
            ],
            
            "relevance_to_canadian_investigation": [
                "US contract terms may reveal standard Pfizer pricing structure",
                "US safety data can be cross-referenced to Canadian VISP claims",
                "US manufacturing documents may reveal production timeline",
                "US clinical trial data validates Phase 1 pre-pandemic platform claims"
            ],
            
            "access_methods": [
                "FDA FOIA Electronic Reading Room",
                "CourtListener docket (PHMPT v. FDA)",
                "PHMPT website (phmpt.org)",
                "FDA Drug Approval Packages"
            ],
            
            "urls": self.get_document_urls()
        }
        
        filepath = self.output_dir / "us_foia_research_guide.json"
        with open(filepath, 'w', encoding='utf-8') as f:
            json.dump(guide, f, indent=2)
        
        print(f"Research guide saved to {filepath}")
    
    def execute(self):
        """Execute the download process"""
        print("US FOIA Pfizer Data Downloader")
        print("=" * 50)
        print("\nNote: Actual document download requires manual access due to:")
        print("- FDA website may block automated downloads")
        print("- Some documents require interactive navigation")
        print("- Large file sizes may timeout automated requests")
        print("\nThis script creates a research guide with all necessary URLs.")
        
        self.create_research_guide()
        
        print("\nNext steps:")
        print("1. Review research guide at: EVIDENCE_COLLECTED/US_FOIA_DATA/us_foia_research_guide.json")
        print("2. Manually download key documents from URLs in guide")
        print("3. Cross-reference US data to Canadian investigation")

if __name__ == "__main__":
    downloader = USFOIADownloader()
    downloader.execute()
