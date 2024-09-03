#!/usr/bin/env python3

import argparse
from recon import get_dns_records, enumerate_subdomains, enumerate_directories
from scann import scan_ports
from harvestt import print_harvested_emails
from discover import find_documents


def main():

    

    parser = argparse.ArgumentParser(description="Jasoos: Your Cybersecurity Sleuth")
    
    subparsers = parser.add_subparsers(dest="command")

    # DNS Records
    dns_parser = subparsers.add_parser("dns", help="Retrieve DNS records")
    dns_parser.add_argument("domain", help="Domain to retrieve DNS records for")

    # Subdomain Enumeration
    subdomain_parser = subparsers.add_parser("subdomains", help="Enumerate subdomains")
    subdomain_parser.add_argument("domain", help="Domain to enumerate subdomains for")

    # Directory Enumeration
    dir_parser = subparsers.add_parser('dir', help='Enumerate directories')
    dir_parser.add_argument('url', type=str, help='URL to enumerate directories for')
    dir_parser.add_argument('-w', '--wordlist', type=str, default='path/to/your/wordlist.txt', help='Path to the wordlist file')

    # Port Scanning
    scan_parser = subparsers.add_parser("scan", help="Scan ports")
    scan_parser.add_argument("target", help="Target IP for port scanning")

    # Email Harvesting
    email_parser = subparsers.add_parser("harvest", help="Harvest emails")
    email_parser.add_argument("url", help="URL to harvest emails from")

    # Document Discovery
    doc_parser = subparsers.add_parser("discover", help="Discover documents")
    doc_parser.add_argument("url", help="URL to discover documents from")

    args = parser.parse_args()

    if args.command == "dns":
        records = get_dns_records(args.domain)
        print(records)

    elif args.command == "subdomains":
        subdomains = enumerate_subdomains(args.domain)
        print(subdomains)

    elif args.command == "dir":
        directories = enumerate_directories(args.url, args.wordlist)
        if directories:
            print(f"Directories found for {args.url}:")
            for directory in directories:
                print(f"- {directory}")
        else:
            print(f"No directories found for {args.url}")

    elif args.command == "scan":
        scan_result = scan_ports(args.target)
        print(scan_result)

    elif args.command == "harvest":
        emails = print_harvested_emails(args.url)
        print(emails)

    elif args.command == "discover":
        documents = find_documents(args.url)
        print(documents)

if __name__ == "__main__":
    main()
