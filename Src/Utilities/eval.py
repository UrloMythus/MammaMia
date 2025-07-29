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
        headers["user-agent"] = "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36"
        headers["User-Agent"] = "Mozilla/5.0 (Linux; Android 12) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/103.0.5060.71 Mobile Safari/537.36"
        
        # Try multiple URL configurations to handle proxy issues
        urls_to_try = []
        
        # Add ForwardProxy URL if configured
        if ForwardProxy:
            urls_to_try.append(ForwardProxy + stream_link)
        
        # Add direct URL as fallback
        urls_to_try.append(stream_link)
        
        for url in urls_to_try:
            try:
                # Try with proxies first, then without if it fails
                proxy_configs = [proxies, {}] if proxies else [{}]
                
                for proxy_config in proxy_configs:
                    try:
                        response = await client.get(
                            url, 
                            allow_redirects=True, 
                            timeout=20, 
                            headers=headers, 
                            proxies=proxy_config, 
                            impersonate="chrome124"
                        )
                        
                        print(f"Eval solver - URL: {url}, Status: {response.status_code}")
                        
                        if response.status_code == 200:
                            soup = BeautifulSoup(response.text, "lxml", parse_only=SoupStrainer("script"))
                            script_all = soup.find_all("script")
                            
                            for i in script_all:
                                if detect(i.text):
                                    unpacked_code = unpack(i.text)
                                    match = re.search(r'file:"(.*?)"', unpacked_code)
                                    if match:
                                        m3u8_url = match.group(1)
                                        print(f"Eval solver success: Found m3u8 URL")
                                        return m3u8_url
                        else:
                            print(f"Eval solver - Non-200 status: {response.status_code}")
                            
                    except Exception as proxy_error:
                        print(f"Eval solver proxy error for {url}: {proxy_error}")
                        continue
                        
            except Exception as url_error:
                print(f"Eval solver URL error for {url}: {url_error}")
                continue
        
        print("Eval solver: No valid m3u8 URL found in any attempt")
        raise Exception("Error in eval_solver: All attempts failed")
        
    except Exception as e:
        print("Eval solver error\n",e)
        raise Exception("Error in eval_solver")