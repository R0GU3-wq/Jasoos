import nmap

def scan_ports(target):
    nm = nmap.PortScanner()
    
    print(f"Starting port scan on {target}...")
    
    try:
        # Perform the scan
        nm.scan(hosts=target, arguments='-p-')
        print("\nPort scan completed.\n")
        
        # Prepare structured output
        print(f"Scan results for {target}:")
        
        for host in nm.all_hosts():
            print(f"Host: {host}")
            print(f"Hostname: {nm[host].hostname()}")
            print(f"Protocol: {', '.join(nm[host].all_protocols())}")
            for protocol in nm[host].all_protocols():
                print(f"  Protocol: {protocol}")
                ports = nm[host][protocol].keys()
                for port in sorted(ports):
                    state = nm[host][protocol][port]['state']
                    print(f"    Port: {port}\tState: {state}")
    
    except Exception as e:
        print(f"Error: {e}")
