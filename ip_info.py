import ipaddress
from utils.net import fetch_json

def run():
    raw = input("IP address (blank = your public IP): ").strip()
    if not raw:
        try:
            _, data, _ = fetch_json("https://api.ipify.org?format=json")
            raw = data["ip"]
        except Exception as exc:
            print(f"Could not detect public IP: {exc}")
            return
    try:
        ip = ipaddress.ip_address(raw)
    except ValueError:
        print("Invalid IP address.")
        return
    print(f"\nAddress: {ip}")
    print(f"IP version: IPv{ip.version}")
    print(f"Global: {ip.is_global}")
    print(f"Private: {ip.is_private}")
    print(f"Loopback: {ip.is_loopback}")
    if not ip.is_global:
        print("Geolocation skipped: this is not a public global IP.")
        return
    try:
        _, info, _ = fetch_json(f"https://ipwho.is/{ip}")
        if not info.get("success", False):
            print("Geolocation provider returned no result.")
            return
        connection = info.get("connection") or {}
        timezone = info.get("timezone") or {}
        fields = {
            "Country": info.get("country"),
            "Region": info.get("region"),
            "City": info.get("city"),
            "Coordinates": (f"{info.get('latitude')}, {info.get('longitude')}"
                            if info.get("latitude") is not None else None),
            "ISP": connection.get("isp"),
            "Organization": connection.get("org"),
            "Timezone": timezone.get("id"),
        }
        for label, value in fields.items():
            if value:
                print(f"{label}: {value}")
        print("\n[!] Approximate network geolocation; not a person's exact location.")
    except Exception as exc:
        print(f"Geolocation lookup unavailable: {exc}")
