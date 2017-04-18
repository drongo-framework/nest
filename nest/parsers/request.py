import ast
import asyncio
import io
import os
import socket
import uuid

import urllib.parse


class RequestParser(object):
    VALID_METHODS = set(['GET', 'POST', 'PUT', 'DELETE'])

    def __init__(self):
        self._buffer = b''
        self.complete = False

    def feed(self, data, env):
        initial_size = len(self._buffer)

        self._buffer += data
        try:
            idx = self._buffer.index(b'\r\n')
        except Exception as _:
            return len(data)

        line = self._buffer[:idx]
        try:
            method, request, version = line.decode('ascii').split()
        except Exception as _:
            raise Exception('Invalid request!')

        if method not in self.VALID_METHODS:
            raise Exception('Invalid request!')

        if '?' in request:
            path, qs = request.split('?', 1)
        else:
            path, qs = request, ''

        env['REQUEST_METHOD'] = method.upper()
        env['PATH_INFO'] = path
        env['QUERY_STRING'] = qs
        env['QUERY'] = urllib.parse.parse_qs(qs)
        self.complete = True
        return idx + 2 - initial_size