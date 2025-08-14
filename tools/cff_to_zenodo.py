import yaml, json, sys, os

cff_path = sys.argv[1] if len(sys.argv) > 1 else "CITATION.cff"
zenodo_path = sys.argv[2] if len(sys.argv) > 2 else "zenodo.json"

with open(cff_path, encoding="utf-8") as f:
    cff = yaml.safe_load(f)

zenodo = {
    "title": cff.get("title", ""),
    "upload_type": "software",
    "publication_date": cff.get("date-released", ""),
    "creators": [],
    "description": cff.get("abstract", cff.get("message", "")),
    "keywords": cff.get("keywords", []),
    "version": cff.get("version", ""),
    "license": cff.get("license", ""),
    "access_right": "open",
    "related_identifiers": []
}

for author in cff.get("authors", []):
    name = author.get("name") or f"{author.get('family-names', '')}, {author.get('given-names', '')}".strip(", ")
    creator = {"name": name}
    if "orcid" in author:
        creator["orcid"] = author["orcid"].replace("https://orcid.org/", "")
    if "affiliation" in author:
        creator["affiliation"] = author["affiliation"]
    zenodo["creators"].append(creator)

if "repository-code" in cff:
    zenodo["related_identifiers"].append({
        "relation": "isSupplementTo",
        "identifier": cff["repository-code"]
    })

with open(zenodo_path, "w", encoding="utf-8") as f:
    json.dump(zenodo, f, indent=2)

print(f"Wrote {zenodo_path}")
