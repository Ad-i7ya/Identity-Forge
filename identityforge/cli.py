import sys
from colorama import Fore, Style, init
from identityforge.core import get_countries, generate_identity

init(autoreset=True)


def show_help():
    print(Fore.CYAN + """
====================================
        IdentityForge CLI
====================================

Commands:
  identityforge countries
  identityforge generate <code>

Examples:
  identityforge countries
  identityforge generate us
====================================
""")


def countries():
    data = get_countries()

    if not data.get("success"):
        print(Fore.RED + "[ERROR] Failed to fetch countries")
        return

    print(Fore.GREEN + "\n[+] Available Countries:\n")

    countries_list = data.get("data", {}).get("countries", [])

    for c in countries_list:
        # SAFE PARSE (handles string or dict)
        if isinstance(c, dict):
            name = c.get("name") or c.get("country") or str(c)
        else:
            name = str(c)

        print(Fore.YELLOW + "- " + name)
def generate_cmd(country):
    if not country:
        print(Fore.RED + """
[ERROR] Missing country code

Usage:
  identityforge generate <country_code>

Example:
  identityforge generate us
""")
        return

    data = generate_identity(country)

    if not data.get("success"):
        print(Fore.RED + "[ERROR] API request failed")
        return

    user = data["data"][0]

    print(Fore.GREEN + "\n[+] Identity Generated\n")

    print(Fore.CYAN + f"[+] Full Name   : {user.get('Full Name')}")
    print(f"[+] Gender      : {user.get('Gender')}")
    print(f"[+] Email       : {user.get('Email')}")
    print(f"[+] Phone       : {user.get('Phone Number')}")
    print(f"[+] Country     : {user.get('Country')}")
    print(f"[+] Country Code: {user.get('Country_Code')}")
    print(f"[+] City        : {user.get('City/Town')}")
    print(f"[+] Currency    : {user.get('Currency')}")
    print(f"[+] Time Zone   : {user.get('Time Zone')}")


def main():
    args = sys.argv

    if len(args) == 1:
        show_help()
        return

    cmd = args[1]

    if cmd in ["--help", "-h"]:
        show_help()

    elif cmd == "countries":
        countries()

    elif cmd == "generate":
        country = args[2] if len(args) > 2 else None
        generate_cmd(country)

    else:
        print(Fore.RED + "[ERROR] Unknown command")
        show_help()


if __name__ == "__main__":
    main()
