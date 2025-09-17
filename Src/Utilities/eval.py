#Adapted for use in MammaMia from:
#https://github.com/einars/js-beautify/blob/master/python/jsbeautifier/unpackers/packer.py
# Unpacker for Dean Edward's p.a.c.k.e.r, a part of javascript beautifier
# by Einar Lielmanis <einar@beautifier.io>
#
#     written by Stefano Sanfilippo <a.little.coder@gmail.com>
#
# usage:
#
# if detect(some_string):
#     unpacked = unpack(some_string)
#
from fake_headers import Headers  
"""Unpacker for Dean Edward's p.a.c.k.e.r"""
import re
from bs4 import BeautifulSoup, SoupStrainer
import logging
import Src.Utilities.config as config
from Src.Utilities.config import setup_logging
level = config.LEVEL
logger = setup_logging(level)

def detect(source):
    if "eval(function(p,a,c,k,e,d)" in source:
        mystr = "smth"
        return mystr is not None


def unpack(source):
    """Unpacks P.A.C.K.E.R. packed js code."""
    payload, symtab, radix, count = _filterargs(source)

    if count != len(symtab):
        raise UnpackingError("Malformed p.a.c.k.e.r. symtab.")

    try:
        unbase = Unbaser(radix)
    except TypeError:
        raise UnpackingError("Unknown p.a.c.k.e.r. encoding.")

    def lookup(match):
        """Look up symbols in the synthetic symtab."""
        word = match.group(0)
        return symtab[unbase(word)] or word

    payload = payload.replace("\\\\", "\\").replace("\\'", "'")
    source = re.sub(r"\b\w+\b", lookup, payload)
    return _replacestrings(source)


def _filterargs(source):
    """Juice from a source file the four args needed by decoder."""
    juicers = [
        (r"}\('(.*)', *(\d+|\[\]), *(\d+), *'(.*)'\.split\('\|'\), *(\d+), *(.*)\)\)"),
        (r"}\('(.*)', *(\d+|\[\]), *(\d+), *'(.*)'\.split\('\|'\)"),
    ]
    for juicer in juicers:
        args = re.search(juicer, source, re.DOTALL)
        if args:
            a = args.groups()
            if a[1] == "[]":
                a = list(a)
                a[1] = 62
                a = tuple(a)
            try:
                return a[0], a[3].split("|"), int(a[1]), int(a[2])
            except ValueError:
                raise UnpackingError("Corrupted p.a.c.k.e.r. data.")

    # could not find a satisfying regex
    raise UnpackingError(
        "Could not make sense of p.a.c.k.e.r data (unexpected code structure)"
    )


def _replacestrings(source):
    """Strip string lookup table (list) and replace values in source."""
    match = re.search(r'var *(_\w+)\=\["(.*?)"\];', source, re.DOTALL)

    if match:
        varname, strings = match.groups()
        startpoint = len(match.group(0))
        lookup = strings.split('","')
        variable = "%s[%%d]" % varname
        for index, value in enumerate(lookup):
            source = source.replace(variable % index, '"%s"' % value)
        return source[startpoint:]
    return source 


class Unbaser(object):
    """Functor for a given base. Will efficiently convert
    strings to natural numbers."""

    ALPHABET = {
        62: "0123456789abcdefghijklmnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ",
        95: (
            " !\"#$%&'()*+,-./0123456789:;<=>?@ABCDEFGHIJKLMNOPQRSTUVWXYZ"
            "[\\]^_`abcdefghijklmnopqrstuvwxyz{|}~"
        ),
    }

    def __init__(self, base):
        self.base = base

        # fill elements 37...61, if necessary
        if 36 < base < 62:
            if not hasattr(self.ALPHABET, self.ALPHABET[62][:base]):
                self.ALPHABET[base] = self.ALPHABET[62][:base]
        # attrs = self.ALPHABET
        # print ', '.join("%s: %s" % item for item in attrs.items())
        # If base can be handled by int() builtin, let it do it for us
        if 2 <= base <= 36:
            self.unbase = lambda string: int(string, base)
        else:
            # Build conversion dictionary cache
            try:
                self.dictionary = dict(
                    (cipher, index) for index, cipher in enumerate(self.ALPHABET[base])
                )
            except KeyError:
                raise TypeError("Unsupported base encoding.")

            self.unbase = self._dictunbaser

    def __call__(self, string):
        return self.unbase(string)

    def _dictunbaser(self, string):
        """Decodes a  value to an integer."""
        ret = 0
        for index, cipher in enumerate(string[::-1]):
            ret += (self.base**index) * self.dictionary[cipher]
        return ret
class UnpackingError(Exception):
    """Badly packed source or general error. Argument is a
    meaningful description."""

    pass

random_headers = Headers()


async def eval_solver(stream_link,proxies, ForwardProxy, client):
    try:
        headers = random_headers.generate()
        headers["User-Agent"] = "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/139.0.0.0 Safari/537.36"
        headers["accept-language"] = 'en-US,en;q=0.5'
        response = await client.get( ForwardProxy + stream_link,  allow_redirects=True, timeout=30, headers = headers, proxies = proxies, impersonate = "chrome124")
        logger.debug("Eval:",response.status_code)
        soup = BeautifulSoup(response.text, "lxml",parse_only=SoupStrainer("script"))
        script_all = soup.find_all("script")
        for i in script_all:
            if detect(i.text):
                unpacked_code = unpack(i.text)
                if "mixdrop" in stream_link:
                     pattern = r'MDCore.wurl ?= ?"(.*?)"'
                     
                else:
                    pattern = r'file:"(.*?)"'
                match = re.search(pattern, unpacked_code)
                if match:
                    m3u8_url = match.group(1)
                    return m3u8_url
    except Exception as e:
        logger.debug("Eval solver error\n",e)
        raise Exception("Error in eval_solver")


#Testing
async def test_animeworld():
    from curl_cffi.requests import AsyncSession
    async with AsyncSession() as client:
        results = await eval_solver("https://mixdrop.cv/e/l6kqxrm4t4l4or",{},"",client)

if __name__ == "__main__":
    import asyncio
    asyncio.run(test_animeworld())  
    #python3 -m Src.Utilities.eval
