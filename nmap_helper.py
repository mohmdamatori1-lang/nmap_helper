#lib
import nmap
import sys

# فقط لونين بسيطين
GREEN = '\033[92m'
BLUE = '\033[94m'
RESET = '\033[0m'

scanner = nmap.PortScanner()

def menu():
    print("Select scan type:")
    print("  1. Fast Scan (common ports)")
    print("  2. Full Scan (all ports)")
    print("  3. OS Detection")
    print("  4. Service & Version Detection")
    print("  5. Network Discovery (ping sweep)")
    print("  6. Custom Scan")
    print("  7. Exit")

def show_banner():
    print("""
╔══════════════════════════════════════════╗
║          NMAP HELPER TOOL v1.0           ║
║        Simplify Your Nmap Scans          ║
╚══════════════════════════════════════════╝
    
    welcom to nmap helper tool v1.0!!

          """)

def nmap(target, options):
    print(f"\n{BLUE}[*] Scanning {target} with options: {options}{RESET}")
    print("-" * 50)
    
    scanner.scan(target, arguments=options)

    for host in scanner.all_hosts():
        print(f"Host: {host}")
        print(f"State: {GREEN if scanner[host].state() == 'up' else BLUE}{scanner[host].state()}{RESET}")
        for protocol in scanner[host].all_protocols():
            print(f"Protocol: {protocol}")
            ports = scanner[host][protocol].keys()
            for port in ports:
                print(f"Port: {port} State: {scanner[host][protocol][port]['state']}")  

def main():
    show_banner()
    target = input("Enter Target ip   ")
    while True:
        menu()
        choice = input("Enter choice  ")
        if choice == "1":
            options = "-F -T4 -n"
            nmap(target, options)
        if choice == "2":
            options = "-p-"
            nmap(target, options)
        if choice == "3":
            options = "-O"
            nmap(target, options)
        if choice == "4":
            options = "-sV"
            nmap(target, options)
        if choice == "5":
            options = "-sn"
            nmap(target, options)
        if choice == "6":
            options = input("Enter options: ")
            nmap(target, options)
        if choice == "7":
            break
        
main()