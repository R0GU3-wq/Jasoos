import dns.resolver
import sublist3r
import subprocess
import json
import requests
import sys

def get_dns_records(domain):
    records = {}
    try:
        records['A'] = [r.to_text() for r in dns.resolver.resolve(domain, 'A')]
        records['NS'] = [r.to_text() for r in dns.resolver.resolve(domain, 'NS')]
        records['MX'] = [r.to_text() for r in dns.resolver.resolve(domain, 'MX')]
        records['TXT'] = [r.to_text() for r in dns.resolver.resolve(domain, 'TXT')]
    except Exception as e:
        print(f"Error retrieving DNS records: {e}")
    print("\nDNS Records:\n")
    for record_type, record_list in records.items():
        print(f"{record_type} Records:")
        for record in record_list:
            print(f"  - {record}")
        print()
    return 

def enumerate_subdomains(domain):
    engines= "bing,baidu,yahoo,google,ask,netcraft,dnsdumpster,virustotal,threatcrowd,ssl,passivedns"

    subdomains = sublist3r.main(domain, 40, False, None, True, True, False, engines)
    print(f"Subdomains found for {domain}:\n")
    for subdomain in subdomains:
        print(f"- {subdomain}")


def enumerate_directories(url, wordlist_path):
    try:
        with open(wordlist_path, 'r') as file:
            directories = file.read().splitlines()
        
        found_directories = []
        total = len(directories)
        print(f"Starting directory enumeration for {url} with {total} directories...")

        for i, directory in enumerate(directories, start=1):
            full_url = f"{url.rstrip('/')}/{directory.lstrip('/')}"
            try:
                response = requests.get(full_url, timeout=5)
                if response.status_code == 200:
                    found_directories.append(full_url)
                    print(f"[+] Found: {full_url}")
                else:
                    print(f"[-] Not Found: {full_url}", end='\r')  # overwrite the line
            except requests.RequestException as e:
                print(f"[!] Error accessing {full_url}: {e}", file=sys.stderr)
            
            # Print progress
            sys.stdout.write(f"\rProgress: {i}/{total} directories checked")
            sys.stdout.flush()
        
        print("\nDirectory enumeration completed.")
        return found_directories
    
    except Exception as e:
        print(f"Error: {e}", file=sys.stderr)
        return []



