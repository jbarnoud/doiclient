#!/usr/bin/env python

import requests
from .exceptions import *

__all__ = ['request', 'resolve', 'json']

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


def request(doi, content_type):
    """
    Request doi resolution using content-type negociation and returns the
    requests module response object.
    """
    header = {"Accept": _format_content_type(content_type}
    url = DOI_URL + doi
    query = requests.get(url, headers=header)
    if query.status_code == 204:
        raise NoMetadataError
    elif query.status_code == 404:
        raise NoDOIError
    elif query.status_code == 406:
        raise ContentTypeError
    return query


def resolve(doi, content_type):
    """
    Request doi resolution using content-type negociation and returns the
    response as a text string.
    """
    return request(doi, content_type).text


def json(doi):
    """
    Request doi resolution using content-type negociation and returns the
    response as a json disctionnary.
    """
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
    if isinstance(content_type, str):
        return SHORTCUTS.get(content_type, content_type)
    if hasattr(content_type, "items"):
        expended_content_type = {SHORTCUTS.get(key, key): weight
                                 for key, weight in content_type.items()}
        return ", ".join([";q=".join((key, str(value)))
                          for key, value in expended_content_type.items()])
    return ", ".join(SHORTCUTS.get(value, value) for value in content_type)
