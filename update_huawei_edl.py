import requests

ASNS = [
    "AS136907",
    "AS55990",
    "AS141180",
    "AS131444"
]

prefixes = set()

for asn in ASNS:

    url = f"https://stat.ripe.net/data/announced-prefixes/data.json?resource={asn}"

    r = requests.get(url)

    data = r.json()

    for prefix in data['data']['prefixes']:
        prefixes.add(prefix['prefix'])

with open("huawei-ipv4.txt", "w") as f:
    for p in sorted(prefixes):
        f.write(p + "\n")

print("Done.")
