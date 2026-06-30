#!/usr/bin/env python3
"""
Task Checklist Generator
Generates actionable checklists from incomplete tasks in investigation files.
"""

import re
from pathlib import Path
import json

EVIDENCE_DIR = Path("/home/x99/Desktop/FUCK/EVIDENCE_COLLECTED")

class TaskChecklistGenerator:
    def __init__(self):
        self.tasks = []
        
    def extract_tasks_from_file(self, filepath):
        """Extract tasks from NEXT STEPS or similar sections"""
        with open(filepath, 'r', encoding='utf-8') as f:
            text = f.read()
            filename = filepath.name
            
        # Find NEXT STEPS sections
        next_steps_match = re.search(r'## 🎯 NEXT STEPS\s+(.*?)(?=##|$)', text, re.DOTALL | re.IGNORECASE)
        
        if next_steps_match:
            section_text = next_steps_match.group(1)
            
            # Extract priority sections
            priority_matches = re.finditer(r'### Priority \d+:\s*(.*?)\n(.*?)(?=###|$)', section_text, re.DOTALL)
            
            for match in priority_matches:
                priority_title = match.group(1).strip()
                tasks_text = match.group(2)
                
                # Extract individual tasks (bullet points or numbered lists)
                task_matches = re.finditer(r'[-*]\s*(.*?)(?=\n[-*]|\n\n|$)', tasks_text)
                for task_match in task_matches:
                    task_text = task_match.group(1).strip()
                    if task_text:
                        self.tasks.append({
                            'source_file': filename,
                            'priority_section': priority_title,
                            'task': task_text,
                            'status': 'pending'
                        })
        
        # Also look for "Investigation Needed" sections
        investigation_matches = re.finditer(r'### Investigation Needed\s*\n(.*?)(?=###|$)', text, re.DOTALL)
        for match in investigation_matches:
            tasks_text = match.group(1)
            task_matches = re.finditer(r'[-*]\s*(.*?)(?=\n[-*]|\n\n|$)', tasks_text)
            for task_match in task_matches:
                task_text = task_match.group(1).strip()
                if task_text:
                    self.tasks.append({
                        'source_file': filename,
                        'priority_section': 'Investigation Needed',
                        'task': task_text,
                        'status': 'pending'
                    })
    
    def scan_directory(self):
        """Scan all markdown files for tasks"""
        md_files = list(EVIDENCE_DIR.glob("*.md"))
        for md_file in md_files:
            self.extract_tasks_from_file(md_file)
    
    def generate_checklist(self):
        """Generate organized checklist"""
        # Group by priority section
        organized = {}
        for task in self.tasks:
            section = task['priority_section']
            if section not in organized:
                organized[section] = []
            organized[section].append(task)
        
        return {
            'total_tasks': len(self.tasks),
            'by_priority': organized,
            'all_tasks': self.tasks
        }
    
    def save_checklist(self, output_path):
        """Save checklist to JSON file"""
        self.scan_directory()
        checklist = self.generate_checklist()
        
        with open(output_path, 'w', encoding='utf-8') as f:
            json.dump(checklist, f, indent=2)
        
        print(f"Task checklist saved to {output_path}")
        print(f"Total tasks extracted: {checklist['total_tasks']}")
        
        # Also generate a markdown version
        md_output = output_path.with_suffix('.md')
        with open(md_output, 'w', encoding='utf-8') as f:
            f.write("# Investigation Tasks Checklist\n\n")
            f.write(f"**Total Tasks:** {checklist['total_tasks']}\n\n")
            f.write("---\n\n")
            
            for section, tasks in checklist['by_priority'].items():
                f.write(f"## {section}\n\n")
                for i, task in enumerate(tasks, 1):
                    f.write(f"{i}. [ ] {task['task']}\n")
                    f.write(f"   - *Source: {task['source_file']}*\n\n")
        
        print(f"Markdown checklist saved to {md_output}")

if __name__ == "__main__":
    generator = TaskChecklistGenerator()
    generator.save_checklist(EVIDENCE_DIR / "task_checklist.json")
