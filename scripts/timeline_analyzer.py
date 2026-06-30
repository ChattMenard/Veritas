#!/usr/bin/env python3
"""
Timeline Analyzer
Analyzes correlations between lobbying meetings, policy decisions, and contract awards.
"""

import re
from pathlib import Path
from collections import defaultdict
from datetime import datetime
import json

EVIDENCE_DIR = Path("/home/x99/Desktop/FUCK/EVIDENCE_COLLECTED")

class TimelineAnalyzer:
    def __init__(self):
        self.events = []
        
    def extract_dates(self, text, filename, event_type):
        """Extract dates and associated events from text"""
        # Match date patterns
        patterns = [
            (r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{1,2}),?\s+(\d{4})', '%B %d %Y'),
            (r'(\d{4})-(\d{2})-(\d{2})', '%Y-%m-%d'),
            (r'(January|February|March|April|May|June|July|August|September|October|November|December)\s+(\d{4})', '%B %Y'),
        ]
        
        for pattern, date_format in patterns:
            matches = re.finditer(pattern, text, re.IGNORECASE)
            for match in matches:
                try:
                    if date_format == '%B %d %Y':
                        date_str = f"{match.group(1)} {match.group(2)} {match.group(3)}"
                        date_obj = datetime.strptime(date_str, date_format)
                    elif date_format == '%Y-%m-%d':
                        date_str = match.group(0)
                        date_obj = datetime.strptime(date_str, date_format)
                    elif date_format == '%B %Y':
                        date_str = f"{match.group(1)} {match.group(2)}"
                        date_obj = datetime.strptime(date_str, date_format)
                    
                    # Extract context around the date
                    start = max(0, match.start() - 100)
                    end = min(len(text), match.end() + 100)
                    context = text[start:end].strip()
                    
                    self.events.append({
                        'date': date_obj.isoformat(),
                        'date_str': date_str,
                        'event_type': event_type,
                        'file': filename,
                        'context': context
                    })
                except ValueError:
                    continue
    
    def scan_file(self, filepath):
        """Scan a single file for timeline events"""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            filename = filepath.name
            
            # Determine event type based on filename
            if 'lobbying' in filename.lower():
                event_type = 'lobbying_meeting'
            elif 'contract' in filename.lower():
                event_type = 'contract_award'
            elif 'policy' in filename.lower() or 'regulation' in filename.lower():
                event_type = 'policy_change'
            elif 'parliamentary' in filename.lower():
                event_type = 'parliamentary_action'
            else:
                event_type = 'general'
            
            self.extract_dates(text, filename, event_type)
    
    def scan_directory(self):
        """Scan all markdown files"""
        md_files = list(EVIDENCE_DIR.glob("*.md"))
        for md_file in md_files:
            self.scan_file(md_file)
        
        # Sort events by date
        self.events.sort(key=lambda x: x['date'])
    
    def analyze_correlations(self, days_window=30):
        """Find events that occur within a time window of each other"""
        correlations = []
        
        for i, event1 in enumerate(self.events):
            for event2 in self.events[i+1:]:
                date1 = datetime.fromisoformat(event1['date'])
                date2 = datetime.fromisoformat(event2['date'])
                
                delta = abs((date2 - date1).days)
                
                if delta <= days_window:
                    correlations.append({
                        'event1': event1,
                        'event2': event2,
                        'days_apart': delta,
                        'correlation_type': f"{event1['event_type']} -> {event2['event_type']}"
                    })
        
        return correlations
    
    def generate_report(self):
        """Generate timeline analysis report"""
        correlations = self.analyze_correlations()
        
        report = {
            'total_events': len(self.events),
            'total_correlations': len(correlations),
            'events_by_type': self._count_by_type(),
            'timeline': self.events,
            'correlations': correlations[:50]  # Limit to first 50 correlations
        }
        
        return report
    
    def _count_by_type(self):
        """Count events by type"""
        counts = defaultdict(int)
        for event in self.events:
            counts[event['event_type']] += 1
        return dict(counts)
    
    def save_report(self, output_path):
        """Save report to JSON file"""
        self.scan_directory()
        report = self.generate_report()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(report, f, indent=2)
        
        print(f"Timeline analysis report saved to {output_path}")
        print(f"Total events: {report['total_events']}")
        print(f"Total correlations found: {report['total_correlations']}")

if __name__ == "__main__":
    analyzer = TimelineAnalyzer()
    analyzer.save_report(EVIDENCE_DIR / "timeline_analysis_report.json")
