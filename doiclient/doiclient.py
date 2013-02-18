#!/usr/bin/env python

import requests
#from .exceptions import *

DOI_URL = 'http://dx.doi.org/'
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

def request(doi, content_type):
    header = {"Accept": content_type}
    url = DOI_URL + doi
    query = requests.get(url, headers=header)
    return query

def resolve(doi, content_type):
    return request(doi, content_type).text

def json(doi):
    return request(doi, "application/vnd.citationstyles.csl+json").json()

def _format_content_type(content_type):
    """
    Convert content type from a python data structure to something usable by
    the server

    Content type negociation accepts 3 different formats:
    - a single mimetype
    - a list of mimetypes
    - a list of weighted mimetypes

    The functions in this module accept:
    - a single mimetype as a string
    - a list of mimetypes
    - a dictionnary with mimetypes as keys and the associated weigth as values

    In addition the functions accept shortcuts for mimetype as defined in the
    SHORTCUTS constant.

    This function returns a string usable as a content type.
    """
    if hasattr(content_type, items):
        return ", ".join([";q=".join(item) for item in content_type.items()])
    
