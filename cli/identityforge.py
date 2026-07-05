import sys
import requests

BASE_URL = "https://identity-forge.adi7ya.workers.dev"


def show_banner():
    print("""
======================================
        IdentityForge CLI
======================================

Synthetic Identity Generator
OPSEC • Testing • Mock Data
======================================
""")


def show_help():
    print("""
IdentityForge CLI

Usage:
  identityforge              Show help
  identityforge countries    List supported countries
  identityforge generate <country_code>

Examples:
  identityforge generate us
  identityforge generate in
  identityforge countries
""")


def get_countries():
    try:
        res = requests.get(f"{BASE_URL}/countries")
        data = res.json()

        print("\nAvailable Countries:\n")

        for c in data["data"]["countries"]:
            print(f"- {c}")

    except Exception as e:
        print(f"Error fetching countries: {e}")


def generate_identity(country):
    if not country:
        print("""
[ERROR] Missing country code

Usage:
  identityforge generate <country_code>

Example:
  identityforge generate us

Tip:
  Run 'identityforge countries' to see all supported codes.
""")
        return

    try:
        res = requests.get(f"{BASE_URL}/generate?country={country}")
        data = res.json()["data"][0]

        print("\n[+] Identity Generated\n")
        print(f"[+] Full Name     : {data.get('Full Name')}")
        print(f"[+] Gender        : {data.get('Gender')}")
        print(f"[+] Email         : {data.get('Email')}")
        print(f"[+] Phone         : {data.get('Phone Number')}")
        print(f"[+] Country       : {data.get('Country')}")
        print(f"[+] Country Code  : {data.get('Country Code')}")
        print(f"[+] City          : {data.get('City/Town')}")
        print(f"[+] Currency      : {data.get('Currency')}")
        print(f"[+] Time Zone     : {data.get('Time Zone')}")
        print(f"[+] Blood Group   : {data.get('Blood Group')}")
        print("\n======================================\n")

    except Exception as e:
        print(f"Error generating identity: {e}")


def main():
    args = sys.argv

    if len(args) == 1:
        show_banner()
        show_help()
        return

    command = args[1]

    if command == "--help":
        show_help()

    elif command == "countries":
        get_countries()

    elif command == "generate":
        country = args[2] if len(args) > 2 else None
        generate_identity(country)

    else:
        print("Unknown command. Use --help")


if __name__ == "__main__":
    main()
