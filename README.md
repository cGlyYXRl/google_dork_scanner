🔍 Google Dork Scanner
📝 Description

A powerful tool for performing automated Google Dork searches to find potentially vulnerable websites or exposed information. The script uses Google's Custom Search JSON API to execute search queries and collect results.
✨ Features

    🔑 Multiple Google API key rotation to bypass query limits

    🔎 Custom search engine integration

    🚫 Exclusion of known false positive domains

    📂 Batch processing of dork queries from a file

    💾 Results saving to output file

    ⏳ Rate limiting avoidance

⚙️ Requirements

    🐍 Python 3.x

    📦 requests library

    🔑 Valid Google API keys

    🔍 Google Custom Search Engine ID (CX)

🛠️ Installation

    Ensure Python 3.x is installed

    Install required package:

    pip install requests

    Configure your Google API keys in the script

⚙️ Configuration

Edit the following variables in the script:

    API_KEYS: Add your Google API keys

    CX: Set your Custom Search Engine ID

    EXCLUDE_DOMAINS: Add domains to exclude from results

🚀 Usage
Copy

python dork_scanner.py --dorks DORKS_FILE [--output OUTPUT_FILE]

Arguments:
  --dorks FILE    Path to file containing Google Dork queries (one per line)
  --output FILE   Output file to save results (default: dork_results.txt)

💡 Example

    Create a file dorks.txt with queries:
    
    inurl:".php?id=" "You have an error in your SQL syntax"
    inurl:"/product.php?id="
    inurl:"article.php?id=" "You have an error in your SQL syntax"
    inurl:"news.php?id="
    inurl:"item.php?id=" "mysql_fetch"
    inurl:"view.php?id="
    inurl:"page.php?id=" "SQL syntax error"
    inurl:".php?id=" "Warning: mysql_connect()"
    inurl:".php?id=" "mysql_fetch_array()"
    inurl:".php?id=" "Warning: mysql_query()"
    inurl:".php?id=" "database error"
    inurl:".php?id=" "ODBC SQL Server Driver"
    inurl:".php?id=" "PostgreSQL query failed"


    Run the scanner:

    python dork_scanner.py --dorks dorks.txt --output results.txt

📄 Output

Results are saved in the specified output file with the following format:

1. Page Title
   http://example.com/path
   
2. Another Page Title
   http://another.com/path

⚠️ Important Notes

    Google API has daily query limits

    Respect robots.txt and website terms of service

    Use only for authorized security research

    The script includes a 1-second delay between requests to avoid rate limiting

🛑 Disclaimer

This tool is intended for legitimate security research purposes only. Unauthorized scanning of websites may violate laws and terms of service. Always obtain proper authorization before conducting security testing. Not to be used for malicious purposes.
