#!/usr/bin/env python3
"""
Google Dork Scanner - A tool to automate Google dork searches using Custom Search API
Author: Security Researcher
"""

import requests
import time
import argparse
from typing import List, Optional

# Configuration
API_KEYS = ["AIzaSyD9lm1qSklTSIYA0cgHICIjjklkjklklklk",  # Replace with your keys
            "AIzaSyBXs7SDTmA2tp2Ee-Nq41klhjhjhjhjhj"]    # Multiple keys for rotation
CX = "a7ec3ab4254ghjhgh"  # Replace with your Custom Search Engine ID
MAX_RESULTS = 100  # Maximum results per query
DELAY = 1  # Seconds between requests to avoid rate limiting

# Domains to exclude (false positives)
EXCLUDE_DOMAINS = [
    "bugs.mysql.com",
    "forum.glpi-project.org",
    "piwigo.org",
    "example.com"
]

class GoogleDorkScanner:
    def __init__(self):
        self.session = requests.Session()
        self.session.headers.update({"User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64)"})

    def google_dork(self, query: str, max_results: int = MAX_RESULTS) -> List[str]:
        """Execute Google dork query and return results"""
        results = []
        api_index = 0
        
        try:
            for start in range(1, min(max_results, 100) + 1, 10):
                url = (f"https://www.googleapis.com/customsearch/v1?"
                      f"q={query}&key={API_KEYS[api_index]}&cx={CX}&start={start}")
                
                response = self.session.get(url)
                
                if response.status_code == 200:
                    data = response.json()
                    for item in data.get("items", []):
                        link = item.get('link', '')
                        if not any(domain in link for domain in EXCLUDE_DOMAINS):
                            results.append(f"{item.get('title', 'No title')}\n{link}\n")
                else:
                    print(f"[!] API Error (Status {response.status_code}): {response.text}")
                    api_index = (api_index + 1) % len(API_KEYS)
                    time.sleep(DELAY)
                
                if len(results) >= max_results:
                    break
                
                time.sleep(DELAY)
                
        except Exception as e:
            print(f"[!] Error processing query '{query}': {str(e)}")
            
        return results

def read_dorks_from_file(file_path: str) -> List[str]:
    """Read Google Dork queries from file"""
    try:
        with open(file_path, "r") as f:
            return [line.strip() for line in f if line.strip()]
    except Exception as e:
        print(f"[!] Error reading dorks file: {str(e)}")
        return []

def save_results(results: List[str], output_file: str) -> bool:
    """Save results to output file"""
    try:
        with open(output_file, "w", encoding="utf-8") as f:
            for i, result in enumerate(results, start=1):
                f.write(f"{i}. {result}\n")
        return True
    except Exception as e:
        print(f"[!] Error saving results: {str(e)}")
        return False

def main():
    parser = argparse.ArgumentParser(
        description="🔍 Google Dork Scanner - Automated Google hacking tool",
        formatter_class=argparse.ArgumentDefaultsHelpFormatter
    )
    parser.add_argument(
        "--dorks",
        required=True,
        help="Path to file containing Google Dork queries (one per line)"
    )
    parser.add_argument(
        "--output",
        default="dork_results.txt",
        help="Output file to save results"
    )
    parser.add_argument(
        "--max-results",
        type=int,
        default=MAX_RESULTS,
        help="Maximum results per query"
    )
    args = parser.parse_args()

    print("[*] Starting Google Dork Scanner")
    
    dork_queries = read_dorks_from_file(args.dorks)
    if not dork_queries:
        print("[!] No valid dork queries found")
        return

    scanner = GoogleDorkScanner()
    all_results = []
    
    print(f"[*] Processing {len(dork_queries)} dork queries...")
    for query in dork_queries:
        print(f"[*] Running query: '{query}'")
        results = scanner.google_dork(query, args.max_results)
        all_results.extend(results)
        print(f"[+] Found {len(results)} results for this query")
        time.sleep(DELAY)

    if save_results(all_results, args.output):
        print(f"[+] Saved {len(all_results)} total results to {args.output}")
    else:
        print("[!] Failed to save results")

if __name__ == "__main__":
    main()
