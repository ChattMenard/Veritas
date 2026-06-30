#!/usr/bin/env python3
"""
Evidence Cross-Reference Mapper
Automatically cross-references evidence across investigation files to identify connections.
"""

import os
import re
from pathlib import Path
from collections import defaultdict
import json

EVIDENCE_DIR = Path("/home/x99/Desktop/FUCK/EVIDENCE_COLLECTED")

class EvidenceMapper:
    def __init__(self):
        self.entities = defaultdict(list)
        self.dates = defaultdict(list)
        self.documents = defaultdict(list)
        self.companies = defaultdict(list)
        
    def extract_entities(self, text, filename):
        """Extract person names from text"""
        # Common patterns for Canadian political figures
        patterns = [
            r'(Jean-Yves Duclos|Duclos)',
            r'(Mark Carney|Carney)',
            r'(Chrystia Freeland|Freeland)',
            r'(Mélanie Joly|Joly)',
            r'(Dominic LeBlanc|LeBlanc)',
            r'(Pamela Fralick|Fralick)',
            r'(Bettina Hamelin|Hamelin)',
            r'(Thomas Digby|Digby)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                self.entities[match].append(filename)
    
    def extract_companies(self, text, filename):
        """Extract company names from text"""
        patterns = [
            r'(Pfizer|Pfizer Inc\.|Pfizer-BioNTech)',
            r'(Moderna)',
            r'(BioNTech)',
            r'(Brookfield|Brookfield Asset Management)',
            r'(Innovative Medicines Canada|IMC)',
            r'(Intelcom|Intelcom Courrier)',
            r'(Irving|Irving Shipbuilding)',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                self.companies[match].append(filename)
    
    def extract_dates(self, text, filename):
        """Extract dates from text"""
        # Match various date formats
        patterns = [
            r'(\d{4})',  # Years
            r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+\d{1,2},?\s+\d{4}',
            r'\d{4}-\d{2}-\d{2}',
        ]
        
        for pattern in patterns:
            matches = re.findall(pattern, text, re.IGNORECASE)
            for match in matches:
                self.dates[match].append(filename)
    
    def scan_directory(self):
        """Scan all markdown files in evidence directory"""
        md_files = list(EVIDENCE_DIR.glob("*.md"))
        
        for md_file in md_files:
            with open(md_file, 'r', encoding='utf-8') as f:
                text = f.read()
                filename = md_file.name
                
                self.extract_entities(text, filename)
                self.extract_companies(text, filename)
                self.extract_dates(text, filename)
    
    def generate_report(self):
        """Generate cross-reference report"""
        report = {
            "entities": dict(self.entities),
            "companies": dict(self.companies),
            "dates": dict(self.dates),
            "summary": {
                "total_files_scanned": len(list(EVIDENCE_DIR.glob("*.md"))),
                "unique_entities": len(self.entities),
                "unique_companies": len(self.companies),
                "unique_dates": len(self.dates)
            }
        }
        
        return report
    
    def save_report(self, output_path):
        """Save report to JSON file"""
        report = self.generate_report()
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"Cross-reference report saved to {output_path}")
        print(f"Summary: {report['summary']}")

if __name__ == "__main__":
    mapper = EvidenceMapper()
    mapper.scan_directory()
    mapper.save_report(EVIDENCE_DIR / "evidence_cross_reference_report.json")
