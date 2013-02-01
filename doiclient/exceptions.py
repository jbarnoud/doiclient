#!/usr/bin/env python
class DOIException(Exception):
    pass


class NoMetadataError(DOIException):
    pass


class NoDOIError(DOIException):
    pass


class ContentTypeError(DOIException):
    pass
