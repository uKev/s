# coding: utf8
'''
Created on 17.05.2011

@author: Kevin Zuber

Copyright (c) 2011, Kevin Zuber.
License: MIT (see LICENSE for details)
'''
import sqlite3
import time
import base64
import struct


def id_to_key(id):
    data = struct.pack('<Q', id).rstrip('\x00')
    if len(data) == 0:
        data = '\x00'
    s = base64.urlsafe_b64encode(data).rstrip('=')
    return s


def key_to_id(key):
    data = base64.urlsafe_b64decode(key + '==')
    n = struct.unpack('<Q', data + '\x00' * (8 - len(data)))
    return n[0]


class GetURL(object):
    def __init__(self, connection):
        self.__connection = connection

    def __getitem__(self, key):
        try:
            id = (key_to_id(key), )
        except TypeError:
            raise KeyError
        c = self.__connection.cursor()
        row = c.execute("select url from shorts where id=?", id).fetchone()
        if row:
            return row[0]
        else:
            raise KeyError


class Shortener(object):
    def __init__(self, db_file):
        self.db_file = db_file
        self.__connection = sqlite3.connect(db_file)
        self.url = GetURL(self.__connection)

        c = self.__connection.cursor()
        c.execute("create table if not exists shorts (id INTEGER PRIMARY KEY, url TEXT, ip TEXT, time INTEGER)")
        self.__connection.commit()

    def get_id(self, url):
        c = self.__connection.cursor()
        row = c.execute("select id from shorts where url=?", (url,)).fetchone()
        if row:
            return row[0]
        else:
            return None

    def exists(self, url):
        if self.get_id(url):
            return True
        else:
            return False

    def add(self, url, ip):
        id = self.get_id(url)
        if not id:
            c = self.__connection.cursor()
            v = (url, ip, int(time.time()))
            c.execute("insert into shorts (url, ip, time) values (?, ?, ?)", v)
            id = c.lastrowid
            self.__connection.commit()
        return id_to_key(id)