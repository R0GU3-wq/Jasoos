# Jasoos
Jasoos is a versatile reconnaissance tool designed to perform various types of information gathering on websites. Built with Kali Linux in mind, this tool can perform DNS reconnaissance, harvest emails, discover documents, and more.

## Features

- **DNS Reconnaissance**: Perform DNS lookups to gather information about domain names.
- **Email Harvesting**: Scrape a webpage for email addresses.
- **Document Discovery**: Find and list documents available on a webpage (e.g., `.pdf`, `.doc`, `.xls`, `.ppt`).
- Directory Enumeration, Subdomain Scanning, Port Scanning.
- Diectory bruteforcing : Using given wordlist

## Installation

### Prerequisites

Before installing **Jasoos**, ensure you have the following installed:

- Python 3.11 or higher
- pip (Python package installer)
- `git` for cloning the repository
- Selenium WebDriver (e.g., geckodriver for Firefox)

### Step-by-Step Installation

1. **Clone the Repository**:
   ```sh
   git clone https://github.com/YOUR_USERNAME/jasoos.git
   cd jasoos

Install the Required Python Packages:

```sh
   pip install -r requirements.txt
```
Install a WebDriver (e.g., for Firefox):

```sh
   sudo apt-get install firefox-geckodriver
```
Manual Download: Download geckodriver from here and place it in your PATH.
Update the Script Permissions:

```sh
   chmod +x jasoos
```
Move the Script to a Directory in Your PATH (optional):

```sh
   sudo mv jasoos /usr/local/bin/
```
### Usage
**Basic Commands**
Jasoos comes with several commands that you can use to gather different types of information.

1. DNS Reconnaissance
Perform DNS lookups on a domain:
```sh
jasoos dns <domain_name>
```
2. Email Harvesting
Scrape a webpage for email addresses:
```sh
jasoos harvest <url>
```
3. Document Discovery
Find and list documents available on a webpage:
```sh
jasoos discover <url>
```
4. Directory Enumeration
Enumerate directories on a target URL using a wordlist.
```sh
jasoos dir <url> -w <path_to_wordlist>
```
5. Subdomain Scanning
Scan for subdomains of a target domain.
```sh
jasoos subdomains <target_domain>
