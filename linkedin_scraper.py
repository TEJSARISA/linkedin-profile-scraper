#!/usr/bin/env python3
"""
LinkedIn Profile Scraper
A demonstration of web scraping best practices with ethical guidelines.

WARNING: This scraper is for educational purposes only.
Scraping LinkedIn violates their Terms of Service.
LinkedIn has explicit prohibitions against automated scraping.
Use this code only on sites where you have permission to scrape.
"""

import csv
import json
import logging
import random
import time
from datetime import datetime
from typing import List, Dict, Optional
import os

try:
    import requests
    from requests.adapters import HTTPAdapter
    from urllib3.util.retry import Retry
except ImportError:
    print("Please install required packages: pip install -r requirements.txt")
    exit(1)


class LinkedInScraper:
    """
    LinkedIn Profile Scraper with ethical practices.
    
    Features:
    - User-agent rotation
    - Request rate limiting
    - Header rotation
    - Error handling and logging
    - CSV export functionality
    """
    
    # User agents for rotation
    USER_AGENTS = [
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/91.0.4472.124 Safari/537.36',
        'Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:89.0) Gecko/20100101 Firefox/89.0',
        'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/14.1.1 Safari/605.1.15',
    ]
    
    def __init__(self, output_csv: str = 'profiles.csv', min_delay: float = 2.0, max_delay: float = 5.0):
        """
        Initialize the scraper.
        
        Args:
            output_csv: Path to output CSV file
            min_delay: Minimum delay between requests (seconds)
            max_delay: Maximum delay between requests (seconds)
        """
        self.output_csv = output_csv
        self.min_delay = min_delay
        self.max_delay = max_delay
        self.profiles = []
        
        # Setup logging
        logging.basicConfig(
            level=logging.INFO,
            format='%(asctime)s - %(name)s - %(levelname)s - %(message)s',
            handlers=[
                logging.FileHandler('scraper.log'),
                logging.StreamHandler()
            ]
        )
        self.logger = logging.getLogger(__name__)
        self.logger.info('LinkedInScraper initialized')
    
    def get_random_user_agent(self) -> str:
        """Return a random user agent from the list."""
        return random.choice(self.USER_AGENTS)
    
    def get_headers(self) -> Dict[str, str]:
        """Generate request headers with rotating user-agent."""
        return {
            'User-Agent': self.get_random_user_agent(),
            'Accept': 'text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8',
            'Accept-Language': 'en-US,en;q=0.5',
            'Accept-Encoding': 'gzip, deflate',
            'DNT': '1',
            'Connection': 'keep-alive',
            'Upgrade-Insecure-Requests': '1',
            'Cache-Control': 'max-age=0',
        }
    
    def add_rate_limiting(self, session: requests.Session) -> requests.Session:
        """Add retry strategy and rate limiting to session."""
        retry_strategy = Retry(
            total=3,
            status_forcelist=[429, 500, 502, 503, 504],
            allowed_methods=["HEAD", "GET", "OPTIONS"],
            backoff_factor=1
        )
        adapter = HTTPAdapter(max_retries=retry_strategy)
        session.mount("http://", adapter)
        session.mount("https://", adapter)
        return session
    
    def simulate_profile_data(self, profile_url: str) -> Optional[Dict]:
        """
        Simulate scraping profile data.
        
        NOTE: This returns mock data for demonstration purposes.
        Actual LinkedIn scraping is not performed due to ToS restrictions.
        
        Args:
            profile_url: LinkedIn profile URL
            
        Returns:
            Dictionary with simulated profile data or None if failed
        """
        try:
            # Respect rate limiting
            delay = random.uniform(self.min_delay, self.max_delay)
            self.logger.info(f'Rate limiting: waiting {delay:.2f} seconds')
            time.sleep(delay)
            
            self.logger.info(f'Processing: {profile_url}')
            
            # Extract username from URL
            username = profile_url.split('/in/')[-1].rstrip('/')
            
            # Simulate profile data (mock data only)
            profile_data = {
                'profile_url': profile_url,
                'username': username,
                'name': f'Professional {username.title()}',
                'title': 'Job Title Example',
                'company': 'Company Example',
                'location': 'City, Country',
                'about': 'Professional summary example',
                'skills': 'Python, Web Scraping, Data Analysis',
                'connections': random.randint(100, 5000),
                'endorsements': random.randint(0, 500),
                'scraped_at': datetime.now().isoformat(),
                'data_type': 'SIMULATED - FOR DEMONSTRATION ONLY'
            }
            
            self.profiles.append(profile_data)
            self.logger.info(f'Successfully processed: {username}')
            return profile_data
            
        except Exception as e:
            self.logger.error(f'Error processing {profile_url}: {str(e)}')
            return None
    
    def scrape_profiles(self, profile_urls: List[str]) -> List[Dict]:
        """
        Scrape multiple LinkedIn profiles.
        
        Args:
            profile_urls: List of LinkedIn profile URLs
            
        Returns:
            List of scraped profile data
        """
        self.logger.info(f'Starting to scrape {len(profile_urls)} profiles')
        
        for url in profile_urls:
            self.simulate_profile_data(url)
        
        self.logger.info(f'Scraping complete. Total profiles: {len(self.profiles)}')
        return self.profiles
    
    def save_to_csv(self) -> str:
        """
        Save scraped profiles to CSV file.
        
        Returns:
            Path to saved CSV file
        """
        if not self.profiles:
            self.logger.warning('No profiles to save')
            return None
        
        try:
            fieldnames = list(self.profiles[0].keys())
            
            with open(self.output_csv, 'w', newline='', encoding='utf-8') as csvfile:
                writer = csv.DictWriter(csvfile, fieldnames=fieldnames)
                writer.writeheader()
                writer.writerows(self.profiles)
            
            self.logger.info(f'Profiles saved to {self.output_csv}')
            return self.output_csv
            
        except Exception as e:
            self.logger.error(f'Error saving to CSV: {str(e)}')
            return None
    
    def save_to_json(self, filename: str = 'profiles.json') -> str:
        """
        Save scraped profiles to JSON file.
        
        Args:
            filename: Output JSON filename
            
        Returns:
            Path to saved JSON file
        """
        if not self.profiles:
            self.logger.warning('No profiles to save')
            return None
        
        try:
            with open(filename, 'w', encoding='utf-8') as jsonfile:
                json.dump(self.profiles, jsonfile, indent=2, ensure_ascii=False)
            
            self.logger.info(f'Profiles saved to {filename}')
            return filename
            
        except Exception as e:
            self.logger.error(f'Error saving to JSON: {str(e)}')
            return None
    
    def get_stats(self) -> Dict:
        """Get statistics about scraped profiles."""
        if not self.profiles:
            return {'total_profiles': 0}
        
        return {
            'total_profiles': len(self.profiles),
            'average_connections': sum(p.get('connections', 0) for p in self.profiles) / len(self.profiles),
            'total_skills_fields': len([p for p in self.profiles if p.get('skills')])
        }


if __name__ == '__main__':
    # Sample LinkedIn profile URLs (replace with actual profiles)
    sample_profiles = [
        'linkedin.com/in/sample-profile-1',
        'linkedin.com/in/sample-profile-2',
        'linkedin.com/in/sample-profile-3',
        'linkedin.com/in/sample-profile-4',
        'linkedin.com/in/sample-profile-5',
        'linkedin.com/in/sample-profile-6',
        'linkedin.com/in/sample-profile-7',
        'linkedin.com/in/sample-profile-8',
        'linkedin.com/in/sample-profile-9',
        'linkedin.com/in/sample-profile-10',
        'linkedin.com/in/sample-profile-11',
        'linkedin.com/in/sample-profile-12',
        'linkedin.com/in/sample-profile-13',
        'linkedin.com/in/sample-profile-14',
        'linkedin.com/in/sample-profile-15',
        'linkedin.com/in/sample-profile-16',
        'linkedin.com/in/sample-profile-17',
        'linkedin.com/in/sample-profile-18',
        'linkedin.com/in/sample-profile-19',
        'linkedin.com/in/sample-profile-20',
    ]
    
    # Initialize scraper
    scraper = LinkedInScraper(output_csv='profiles.csv')
    
    # Scrape profiles
    profiles = scraper.scrape_profiles(sample_profiles)
    
    # Save results
    csv_file = scraper.save_to_csv()
    json_file = scraper.save_to_json()
    
    # Print statistics
    stats = scraper.get_stats()
    print("\n=== Scraping Statistics ===")
    print(f"Total Profiles Scraped: {stats['total_profiles']}")
    print(f"Average Connections: {stats['average_connections']:.2f}")
    print(f"\nResults saved to:")
    print(f"  CSV: {csv_file}")
    print(f"  JSON: {json_file}")
    print("\nNote: This is simulated data for demonstration purposes.")
    print("Actual LinkedIn scraping violates their ToS.")
