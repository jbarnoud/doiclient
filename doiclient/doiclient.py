#!/usr/bin/env python

import requests
from .exception import *

SHORTCUTS = {
    "xml": "application/rdf+xml",
    "turtle": "text/turtle",
    "json": "application/vnd.citationstyles.csl+json",
    "formatted": "text/x-bibliography",
    "ris": "application/x-research-info-systems",
    "bibtex": "application/x-bibtex",
    "crossref": "application/vmd.crossref.unixref+xml",
    "datacite": "application/vmd.datacite.datacite+xml",
}


def normalize(doi):
    return doi

def resolve(doi, format):
    pass

def json(doi):
    pass

def _format_content_type(format):
    pass
