from utils.validate import clean_domain
from utils.net import fetch_json

RECORDS = ("A", "AAAA", "MX", "NS", "TXT", "CNAME", "SOA")

def run():
    try:
        domain = clean_domain(input("Domain: "))
    except ValueError as exc:
        print(exc)
        return
    for record in RECORDS:
        try:
            _, data, _ = fetch_json(
                f"https://dns.google/resolve?name={domain}&type={record}"
            )
            answers = data.get("Answer", [])
            print(f"\n{record}:")
            if answers:
                for answer in answers:
                    print("  " + answer.get("data", "(empty)"))
            else:
                print("  No answer returned.")
        except Exception as exc:
            print(f"\n{record}: lookup failed ({exc})")
