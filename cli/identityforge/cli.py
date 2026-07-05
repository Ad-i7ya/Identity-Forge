import sys
from identityforge.core import get_countries, generate_identity


def show_help():
    print("""
====================================
     IdentityForge CLI
====================================

Commands:
  identityforge              Show help
  identityforge countries    List countries
  identityforge generate <code>

Examples:
  identityforge countries
  identityforge generate us
====================================
""")


def show_countries():
    data = get_countries()

    if not data.get("success"):
        print("[ERROR] Failed to fetch countries")
        return

    print("\nAvailable Countries:\n")

    for c in data["data"]["countries"]:
        print("-", c)


def generate(country):
    if not country:
        print("""
[ERROR] Missing country code

Usage:
  identityforge generate <country_code>

Example:
  identityforge generate us
""")
        return

    data = generate_identity(country)

    if not data.get("success"):
        print("[ERROR] Failed to generate identity")
        return

    user = data["data"][0]

    print("\n[+] Identity Generated\n")
    print(f"[+] Full Name   : {user.get('Full Name')}")
    print(f"[+] Gender      : {user.get('Gender')}")
    print(f"[+] Email       : {user.get('Email')}")
    print(f"[+] Phone       : {user.get('Phone Number')}")
    print(f"[+] Country     : {user.get('Country')}")
    print(f"[+] Country Code: {user.get('Country Code')}")
    print(f"[+] City        : {user.get('City/Town')}")
    print(f"[+] Currency    : {user.get('Currency')}")
    print(f"[+] Time Zone   : {user.get('Time Zone')}")
    print("\n")


def main():
    args = sys.argv

    if len(args) == 1:
        show_help()
        return

    cmd = args[1]

    if cmd == "--help":
        show_help()

    elif cmd == "countries":
        show_countries()

    elif cmd == "generate":
        country = args[2] if len(args) > 2 else None
        generate(country)

    else:
        print("[ERROR] Unknown command. Use --help")


if __name__ == "__main__":
    main()
