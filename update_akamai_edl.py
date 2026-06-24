import requests

ASNS = [
    "AS20940",
    "AS16625",
    "AS32787"
]

prefixes = set()

for asn in ASNS:
    url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource={asn}"
    r = requests.get(url)
    data = r.json()

    for p in data["data"]["prefixes"]:
        prefixes.add(p["prefix"])

with open("akamai-ipv4.txt", "w") as f:
    for prefix in sorted(prefixes):
        f.write(prefix + "\n")

print("Akamai prefixes updated")
