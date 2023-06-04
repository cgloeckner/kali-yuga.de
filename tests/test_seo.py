import unittest
import pathlib
import tempfile

import controller


class TestSeo(unittest.TestCase):

    def test_sidemap(self):
        sitemap = controller.Sitemap()
        sitemap.append('https://www.example.com')
        sitemap.append('https://www.example.com/')
        sitemap.append('https://www.example.com/foo')
        sitemap.append('https://www.example.com/bar')

        expected = '''<?xml version='1.0' encoding='utf-8'?>
<urlset xmlns="http://www.sitemaps.org/schemas/sitemap/0.9"><url><loc>https://www.example.com</loc></url><url><loc>https://www.example.com/</loc></url><url><loc>https://www.example.com/foo</loc></url><url><loc>https://www.example.com/bar</loc></url></urlset>'''

        with tempfile.NamedTemporaryFile() as tmpfile:
            sitemap.save_to_xml(pathlib.Path(tmpfile.name))

            with open(tmpfile.name, 'r') as h:
                content = h.read()
                self.assertEqual(expected, content)
