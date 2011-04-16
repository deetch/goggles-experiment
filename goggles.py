#!/usr/bin/env python

import random
import urllib2 as ul
from protobufparser import pprint

def to_varint(value):
    ret = []
    bits = value & 0x7f
    value >>= 7
    while value:
        ret.append(chr(0x80|bits))
        bits = value & 0x7f
        value >>= 7
    ret.append(chr(bits))
    return ''.join(ret)

def encode_image(image):
    size = len(image)
    a = to_varint(size + 401)
    b = to_varint(size + 14)
    c = to_varint(size + 10)
    size = to_varint(size)
    return "\n%s\n%s\n%s\n%s%s" % (a,b,c,size,image)

def gen_cssid():
    return "".join([random.choice(['0','1','2','3','4','5','6','7','8','9','a','b','c','d','e','f']) for i in xrange(16)])

class Goggles:
    def __init__(self):
        self.headers = {"Content-Type": "application/x-protobuffer", "Pragma": "no-cache"}
        self.url = "http://www.google.com/goggles/container_proto?cssid=%s"
        self.activation_magic = "\x22\x00\x62\x3C\x0A\x13\x22\x02\x65\x6E\xBA\xD3\xF0\x3B\x0A\x08\x01\x10\x01\x28\x01\x30\x00\x38\x01\x12\x1D\x0A\x09\x69\x50\x68\x6F\x6E\x65\x20\x4F\x53\x12\x03\x34\x2E\x31\x1A\x00\x22\x09\x69\x50\x68\x6F\x6E\x65\x33\x47\x53\x1A\x02\x08\x02\x22\x02\x08\x01"
        self.init_cssid()

    def init_cssid(self):
        self.cssid = gen_cssid()
        req =  ul.Request(self.url % self.cssid, self.activation_magic, self.headers)
        try:
            ul.urlopen(req)
        except ul.HTTPError, e:
            if e.code==400:
                print "maybe google doesn't like cssid", self.cssid
                print "trying again..."
                self.init_cssid()
            else:
                raise e
                
    def send_image(self, image):
        req = ul.Request(self.url % self.cssid, encode_image(image), self.headers)
        try:
            result = ul.urlopen(req)
        except ul.HTTPError, e:
            if e.code==400:
                print "something's wrong, i'll try a new cssid...maybe that fixes it :)"
                self.init_cssid()
                self.send_image(image)
            else:
                raise e
        return result.read()

if __name__ == "__main__":
    from optparse import OptionParser
    import sys, re
    parser = OptionParser()
    (options, args) = parser.parse_args()
    if len(args)==0:
        print "url of jpeg needed"
        sys.exit(1)
    img = ul.urlopen(args[0]).read()
    if len(img)>140000:
        print "jpeg should be smaller than 140KB"
        sys.exit(1)
    g = Goggles()
    res = g.send_image(img)
    pprint(res)
    sys.exit()
