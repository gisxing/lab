#!/usr/bin/env python
#-*- coding: utf-8 -*-
from base64 import b64encode, b64decode
from M2Crypto.EVP import Cipher
import logging

ENC=1
DEC=0

class algorithm():
    def __init__(self, key, iv=None):
        self.key = key
        self.cipher = None
        if iv is None:
            self.iv = '\0' * 32
        else:
            self.iv = b64decode(iv)

    def build_cipher(self, op=ENC):
        return Cipher(alg='aes_256_cbc', key=self.key, iv=self.iv, op=op, key_as_bytes=1 ,i=1, d='sha1')

    def encrypt(self, data):
        cipher = self.build_cipher(ENC)
        v = cipher.update(data)
        v = v + cipher.final()
        del cipher
        return b64encode(v)

    def decrypt(self, data):
        cipher = self.build_cipher(DEC)
        data = b64decode(data)
        try:
            v = cipher.update(data)
            v = v + cipher.final()
        except:
            logging.error('decrypt data may be invalid')
            return ''
        del cipher
        return v
