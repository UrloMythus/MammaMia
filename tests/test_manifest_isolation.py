"""Route-logic regression tests without provider imports or network access."""
import ast
import base64
import copy
from pathlib import Path
import unittest


def routes():
    source = ast.parse((Path(__file__).parents[1] / 'run.py').read_text())
    functions = [node for node in source.body if isinstance(node, ast.FunctionDef)
                 and node.name in {'addon_manifest', 'manifest'}]
    for node in functions:
        node.decorator_list = []
    namespace = {'base64': base64, 'copy': copy, 'RT': '1',
                 'respond_with': lambda obj: obj,
                 'RedirectResponse': lambda **kwargs: kwargs['url'],
                 'MANIFEST': {'resources': ['catalog', 'stream'],
                              'catalogs': [{'id': 'tv_channels'}, {'id': 'realtime'}]}}
    exec(compile(ast.Module(body=functions, type_ignores=[]), 'run.py', 'exec'), namespace)
    return namespace


class ManifestTests(unittest.TestCase):
    def test_default_redirect_is_base64_encoded(self):
        ns = routes()
        path = ns['manifest']()
        self.assertEqual(base64.b64decode(path.split('/')[1]).decode(), '|SC|LC|')
        ns['addon_manifest'](path.split('/')[1])

    def test_request_cannot_remove_other_users_catalogs(self):
        ns = routes()
        original = copy.deepcopy(ns['MANIFEST'])
        ns['addon_manifest'](base64.b64encode(b'|SC|LC|').decode())
        self.assertEqual(ns['MANIFEST'], original)
        enabled = ns['addon_manifest'](base64.b64encode(b'|LIVETV|RT|').decode())
        self.assertEqual(enabled['catalogs'], original['catalogs'])


if __name__ == '__main__':
    unittest.main()
