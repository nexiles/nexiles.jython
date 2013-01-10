# -*- coding: utf-8 -*-
#
# File: monkey.py
#
# Copyright (c) nexiles GmbH
#

__author__    = """Stefan Eletzhofer <se@nexiles.de>"""
__docformat__ = 'plaintext'

__all__ = ["patch"]

import logging
logger = logging.getLogger("nexilesmonkey")

def patch_socket():
    logger.debug("patching socket module for missing SOL_TCP")
    import socket
    socket.SOL_TCP = 6

def patch_encodings():
    logger.debug("patching encodings module for missing 'idna' encoding")
    import encodings
    def idna(name):
        if name == "idna":
            return encodings.codecs.lookup("utf8")
    encodings.codecs.register(idna)

def patch_mimetypes():
    logger.debug("adding default mimetypes")
    import mimetypes
    mimetypes.add_type("application/json", ".json")


def patch():
    patch_socket()
    patch_encodings()
    patch_mimetypes()

# vim: set ft=python ts=4 sw=4 expandtab :

