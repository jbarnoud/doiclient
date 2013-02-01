#!/usr/bin/env python

#import requests
from .exceptions import *

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
    """
    Normalize a DOI

    A DOI can be formated on several ways. This function aims to translate the
    into a canonical one that look like <prefix>/<sufix>. Extra spacing
    characters is removed so as "doi", "DOI", "doi:", or "DOI:" strings.

    >>> normalize("10.1073/pnas.1009362108")
    10.1073/pnas.1009362108
    >>> normalize("doi:10.1073/pnas.1009362108")
    10.1073/pnas.1009362108
    >>> normalize("  DOI: 10.1073/pnas.1009362108 ")
    10.1073/pnas.1009362108
    """
    return doi

def resolve(doi, format):
    pass

def json(doi):
    pass

def _format_content_type(format):
    pass
