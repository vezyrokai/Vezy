from utils.validate import clean_domain
from utils.net import fetch_json

def run():
    try:
        domain = clean_domain(input("Domain: "))
    except ValueError as exc:
        print(exc)
        return
    print(f"\nDomain: {domain}")
    try:
        status, data, final = fetch_json(f"https://rdap.org/domain/{domain}")
        print(f"RDAP response: HTTP {status}")
        print(f"Registry source: {final}")
        print(f"Handle: {data.get('handle', 'Not provided')}")
        print(f"Status: {', '.join(data.get('status', [])) or 'Not provided'}")
        print(f"Registrar/organization: {extract_registrar(data) or 'Not provided'}")
        for event in data.get("events", []):
            action = event.get("eventAction", "event")
            date = event.get("eventDate", "")
            if date:
                print(f"{action.title()}: {date}")
        nameservers = [n.get("ldhName") for n in data.get("nameservers", []) if n.get("ldhName")]
        if nameservers:
            print("Nameservers: " + ", ".join(nameservers))
        entities = data.get("entities", [])
        emails = []
        for entity in entities:
            for item in entity.get("vcardArray", [None, []])[1] if entity.get("vcardArray") else []:
                if item and item[0] == "email" and len(item) > 3:
                    emails.append(item[3])
        if emails:
            print("Public RDAP contact email(s): " + ", ".join(sorted(set(emails))))
        print("\nNote: registries may redact personal contact details.")
    except Exception as exc:
        print(f"RDAP lookup unavailable: {exc}")

def extract_registrar(data):
    for entity in data.get("entities", []):
        if "registrar" in entity.get("roles", []):
            for item in entity.get("vcardArray", [None, []])[1] if entity.get("vcardArray") else []:
                if item and item[0] == "fn" and len(item) > 3:
                    return item[3]
    return None
