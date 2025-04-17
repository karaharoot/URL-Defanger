import re

def defang_url(url):
    url = url.replace("http://", "hxxp://").replace("https://", "hxxps://")

    domain_match = re.match(r'(hxxps?://)([^/]+)', url)
    if domain_match:
        protocol, domain = domain_match.groups()
        defanged_domain = domain.replace(".", "[.]")
        url = url.replace(domain, defanged_domain, 1)
        return url
    else:
        return None


if __name__ == "__main__":
    while True:
        user_input = input("Enter a URL to defang: ")
        result = defang_url(user_input)

        if result:
            print("Defanged URL:", result)
            break
        else:
            print("Invalid URL – please enter a valid URL (e.g: https://example.com)")

    print("Defanger written by Harout Karakossian")