import ipaddress
import re
from urllib.parse import urlparse

def clean_domain(value):
    value = value.strip().lower()
    if "://" in value:
        value = urlparse(value).hostname or ""
    value = value.rstrip(".")
    if not value or len(value) > 253 or "/" in value or " " in value:
        raise ValueError("Enter a valid hostname such as example.com.")
    try:
        value = value.encode("idna").decode("ascii")
    except UnicodeError:
        raise ValueError("Invalid international domain name.")
    labels = value.split(".")
    if len(labels) < 2 or any(not re.fullmatch(r"[a-z0-9](?:[a-z0-9-]{0,61}[a-z0-9])?", x) for x in labels):
        raise ValueError("Enter a valid domain name.")
    return value

def clean_ip(value):
    return ipaddress.ip_address(value.strip())
