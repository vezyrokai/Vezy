from urllib.parse import quote

# Opens public profile/search locations for manual review; does not scrape accounts.
SITES = {
    "GitHub": "https://github.com/",
    "Instagram": "https://www.instagram.com/",
    "Reddit": "https://www.reddit.com/user/",
    "TikTok": "https://www.tiktok.com/@",
    "YouTube": "https://www.youtube.com/@",
    "X": "https://x.com/",
    "Pinterest": "https://www.pinterest.com/",
}

def run():
    username = input("Public username: ").strip().lstrip("@")
    if not username or len(username) > 64 or any(c.isspace() for c in username):
        print("Enter one username (up to 64 characters, no spaces).")
        return
    print("\nPublic profile URLs for manual checking:")
    for name, base in SITES.items():
        print(f"{name:10} {base}{quote(username, safe='')}")
    print("\nA URL is only a starting point; it does not prove the profile exists")
    print("or that profiles on different services belong to the same person.")
