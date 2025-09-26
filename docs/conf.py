# docs/conf.py
from __future__ import annotations
import os
import sys
from pathlib import Path
import yaml

# ---- Paths ----
DOCS_DIR = Path(__file__).parent.resolve()
REPO_ROOT = DOCS_DIR.parent
sys.path.insert(0, str(REPO_ROOT))  # if you ever need local modules

# ---- Read CITATION.cff ----
CFF_PATH = REPO_ROOT / "CITATION.cff"
citation = {}
if CFF_PATH.exists():
    try:
        with CFF_PATH.open(encoding="utf-8") as f:
            citation = yaml.safe_load(f) or {}
    except Exception as e:
        print(f"[conf.py] Warning: Failed to parse CITATION.cff: {e}")
else:
    print("[conf.py] Warning: CITATION.cff not found at repo root.")

def get_doi(citation: dict) -> str:
    # Top-level DOI (if present)
    if "doi" in citation:
        return citation["doi"]

    # Or look inside identifiers
    for ident in citation.get("identifiers", []):
        if ident.get("type", "").lower() == "doi":
            return ident.get("value", "")
    return ""

def cff(path, default=""):
    """Small helper to extract nested fields safely."""
    cur = citation
    for key in path.split("."):
        if isinstance(cur, dict) and key in cur:
            cur = cur[key]
        else:
            return default
    return cur

# ---- Project info from CFF (with sensible fallbacks) ----
project = cff("title", "STAMPLATE: SensorThings API Domain Profile — JSON Schemas")
release = cff("version", "")              # shown as “Release” in Sphinx
version = release                    # short X.Y if you prefer to slice it
doi = get_doi(citation)
authors_list = []
for a in citation.get("authors", []):
    given = a.get("given-names") or a.get("given_names") or ""
    family = a.get("family-names") or a.get("family_names") or ""
    name = " ".join([given, family]).strip() or a.get("name", "")
    if name:
        authors_list.append(name)
author = ", ".join(authors_list) or cff("authors[0].name", "HMC STAMPLATE Team")

citation_text = f"{author} ({release}). *{project}*. https://doi.org/{doi}" if doi else "To be assigned"



# ---- General Sphinx config ----
extensions = [
    "myst_parser",
    "sphinx.ext.autosectionlabel",
    "sphinx-jsonschema",   # or: "sphinx_jsonschema"
    "sphinxcontrib.bibtex"
]

myst_enable_extensions = [
    "colon_fence",
    "deflist",
    "substitution",
    # Enable if you installed it: "linkify",
]

# Make CFF metadata available inside Markdown via {{ substitutions }}
myst_substitutions = {
    "project_title": project,
    "project_authors": author,
    "project_version": release,
    "project_doi": f"[{doi}](https://doi.org/{doi})" if doi else "_to be assigned_",
    "project_citation_full": citation_text
}

# Also expose to templates / html pages as {{ project_doi }} etc.
html_context = {
    "project_title": project,
    "project_authors": author,
    "project_version": release,
    "project_doi": doi,
    "citation": citation,  # full dict if you need more fields in custom templates
    "project_citation_full": citation_text
}

templates_path = ["_templates"]
exclude_patterns = ["_build", "Thumbs.db", ".DS_Store"]

# ---- HTML output ----
html_theme = "furo"  # or classic/alabaster
html_theme_options = {
    "sidebar_hide_name": False,   # <- important
}

html_static_path = ["_static"]
html_extra_path = ['../schemas', '../stamplate.jsonld', '.nojekyll']

#release = cff("version", "")
#version = release  # empty so Furo won’t show a version badge in the sidebar

html_title = project
html_short_title = project
html_logo = "_static/images/datahub_logo.png"

# ---- Build output directory (docs/_site) ----
# If you use `make html`, set this in the Makefile; for sphinx-build CLI we set it there.
# Keeping it here as a reference.
# (Sphinx itself doesn't set outdir here; we’ll configure via Makefile below.)

# Optional: nicer JSON rendering (sphinxcontrib-jsonschema options)
jsonschema_options = {
    "lift_description": True,
    "auto_reference": True,
    "collapse_long_descriptions": True,
}

# Reference file
bibtex_bibfiles = ["refs.bib"]

print(f"[conf.py] project={project!r} release={release!r} version={version!r}")