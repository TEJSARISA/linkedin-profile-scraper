# LinkedIn Profile Scraper

[![Python 3.8+](https://img.shields.io/badge/python-3.8+-blue.svg)](https://www.python.org/downloads/)
[![License: MIT](https://img.shields.io/badge/License-MIT-yellow.svg)](https://opensource.org/licenses/MIT)

A demonstration project of web scraping best practices with ethical guidelines, user-agent rotation, request rate limiting, and proper error handling.

## ⚠️ IMPORTANT LEGAL NOTICE

**This project is for EDUCATIONAL PURPOSES ONLY.**

### LinkedIn Terms of Service
LinkedIn explicitly prohibits automated scraping in their [Terms of Service](https://www.linkedin.com/legal/user-agreement). Section 8.2 states:
> "You agree that you will not...scrape or copy through our site via automated means (such as harvesting bots, robots, spiders, or scrapers) without our prior express written permission."

### Legal Implications
- **Direct Violation**: Scraping LinkedIn violates their Terms of Service and can result in:
  - Account suspension or permanent ban
  - Legal action from LinkedIn
  - CFAA (Computer Fraud and Abuse Act) violations
  - Civil liability claims

### Ethical Use
This project should only be used:
1. **For Learning**: Understanding web scraping concepts and best practices
2. **On Permitted Websites**: Only scrape sites where you have explicit permission
3. **With Respect**: Always check `robots.txt` and Terms of Service
4. **With Rate Limiting**: Don't overload servers
5. **As a Framework**: Adapt techniques for authorized data collection

## 📋 Project Overview

This project demonstrates:
- ✅ User-Agent rotation
- ✅ Request headers management
- ✅ Rate limiting and delays
- ✅ Error handling and logging
- ✅ CSV and JSON export
- ✅ Session management
- ✅ Retry strategies
- ✅ Professional code structure

**Note**: The scraper currently returns **simulated/mock data** for demonstration purposes. It does NOT actually scrape LinkedIn profiles.

## 🚀 Installation

### Prerequisites
- Python 3.8+
- pip or conda

### Setup

1. **Clone the repository:**
   ```bash
   git clone https://github.com/TEJSARISA/linkedin-profile-scraper.git
   cd linkedin-profile-scraper
   ```

2. **Create virtual environment:**
   ```bash
   python -m venv venv
   source venv/bin/activate  # On Windows: venv\Scripts\activate
   ```

3. **Install dependencies:**
   ```bash
   pip install -r requirements.txt
   ```

## 📖 Usage

### Basic Example

```python
from linkedin_scraper import LinkedInScraper

# Initialize scraper
scraper = LinkedInScraper(
    output_csv='profiles.csv',
    min_delay=2.0,  # Minimum seconds between requests
    max_delay=5.0   # Maximum seconds between requests
)

# Define profile URLs
profiles = [
    'linkedin.com/in/john-doe',
    'linkedin.com/in/jane-smith',
    'linkedin.com/in/bob-wilson',
]

# Scrape profiles (returns simulated data)
profiles_data = scraper.scrape_profiles(profiles)

# Export results
csv_file = scraper.save_to_csv()
json_file = scraper.save_to_json()

# Get statistics
stats = scraper.get_stats()
print(f"Profiles scraped: {stats['total_profiles']}")
print(f"Average connections: {stats['average_connections']:.2f}")
```

### Command Line Usage

```bash
python linkedin_scraper.py
```

This will process the sample profiles and generate CSV and JSON outputs.

## 🏗️ Project Structure

```
linkedin-profile-scraper/
├── linkedin_scraper.py      # Main scraper module
├── requirements.txt         # Project dependencies
├── README.md                # This file
├── .gitignore              # Git ignore rules
└── profiles.csv            # Output file (generated)
```

## 🔧 Configuration

### Rate Limiting
Adjust delays between requests:
```python
scraper = LinkedInScraper(
    min_delay=3.0,   # Wait at least 3 seconds
    max_delay=7.0    # Wait at most 7 seconds
)
```

### User-Agent Rotation
The scraper includes multiple User-Agent strings and rotates them automatically:
- Chrome on Windows
- Chrome on macOS
- Chrome on Linux
- Firefox on Windows
- Safari on macOS

### Custom Headers
The `get_headers()` method returns customized headers including:
- User-Agent (rotated)
- Accept types
- Language preferences
- Encoding support
- Security headers

## 📊 Output Formats

### CSV Export
Generates a CSV file with columns:
- profile_url
- username
- name
- title
- company
- location
- about
- skills
- connections
- endorsements
- scraped_at
- data_type

### JSON Export
Structured JSON output with all profile data and timestamps.

## 🔍 Logging

The scraper creates a `scraper.log` file with detailed information:
- Initialization events
- Processing status
- Errors and warnings
- Success confirmations
- Timing information

## 🛡️ Best Practices Implemented

1. **Rate Limiting**: Random delays between requests
2. **User-Agent Rotation**: Avoid detection patterns
3. **Error Handling**: Graceful exception handling
4. **Logging**: Comprehensive activity logging
5. **Session Management**: Proper HTTP session handling
6. **Retry Logic**: Automatic retry on failures
7. **Type Hints**: Full Python type annotations
8. **Documentation**: Detailed docstrings

## 🔗 Alternatives for Legal Data Collection

### Authorized APIs
- LinkedIn's official APIs (for enterprise clients)
- Public data exports
- Dataset marketplaces

### Other Sources
- GitHub profiles (with permission)
- Stack Overflow profiles (public data)
- Twitter/X profiles (with API)
- Personal websites

## 📝 Limitations & Disclaimers

- **This project uses SIMULATED DATA** for demonstration
- **Does NOT perform actual LinkedIn scraping**
- **Educational purposes only**
- **Scraping LinkedIn without permission violates ToS**
- **User assumes all legal responsibility**

## 🚨 Risks of Actual LinkedIn Scraping

- Account termination (temporary or permanent)
- IP address blocking
- Legal action
- CFAA charges (federal crime)
- Civil lawsuits
- Fines and damages

## 💡 Learning Outcomes

By studying this project, you'll learn:
- Web scraping fundamentals
- HTTP request handling
- Data export techniques
- Rate limiting strategies
- Error handling patterns
- Professional Python practices
- Ethical scraping guidelines

## 📚 Additional Resources

- [Requests Documentation](https://docs.python-requests.org/)
- [Beautiful Soup 4](https://www.crummy.com/software/BeautifulSoup/)
- [Web Scraping Ethics](https://blog.apify.com/is-web-scraping-legal/)
- [LinkedIn API Documentation](https://docs.microsoft.com/en-us/linkedin/)
- [robots.txt Specification](https://www.robotstxt.org/)

## 📄 License

MIT License - See LICENSE file for details

## ⚖️ Disclaimer

**THE SOFTWARE IS PROVIDED "AS IS", WITHOUT WARRANTY OF ANY KIND**

The author assumes no responsibility for misuse or violations of terms of service, intellectual property rights, or applicable laws. Users are solely responsible for ensuring their use complies with all applicable laws and regulations.

## 🤝 Contributing

Contributions are welcome! Focus areas:
- Enhanced error handling
- Additional export formats
- Improved logging
- Documentation
- Test coverage

Please ensure any contributions do not facilitate illegal scraping.

## 📧 Contact

For questions or concerns, please open an issue on the repository.

---

**Remember**: With great technical power comes great ethical responsibility. Use these tools responsibly.
