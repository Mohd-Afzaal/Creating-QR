import segno
import os
from urllib.parse import urlparse

file_path = "Urls.txt"  # Make sure it's saved as UTF-8

# Read URLs
with open(file_path, "r", encoding="utf-8") as f:
    urls = [line.strip() for line in f if line.strip()]

if not urls:
    print("❌ No URLs found in", file_path)
    exit()

# Create output folder
os.makedirs("qr_codes", exist_ok=True)
domain_count = {}

for i, url in enumerate(urls, 1):
    parsed = urlparse(url)
    domain = parsed.netloc.replace("www.", "") or "qr"

    # Keep track of duplicates
    domain_count[domain] = domain_count.get(domain, 0) + 1

    # Simple filename: domain + counter
    filename = os.path.join("qr_codes", f"{domain}_{domain_count[domain]}.png")

    qr = segno.make_qr(url)
    qr.save(filename, scale=10, border=2, light="#2F3961", dark="#FFFFFF")

    print(f"✅ Saved: {filename}")
