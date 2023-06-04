import pathlib
import xml.etree.ElementTree as et

from typing import List

from .modules import ServerApi


class Sitemap(List[str]):
    def save_to_xml(self, filename: pathlib.Path) -> None:
        root = et.Element('urlset')
        root.set('xmlns', "http://www.sitemaps.org/schemas/sitemap/0.9")

        for url in self:
            url_element = et.SubElement(root, 'url')
            loc_element = et.SubElement(url_element, 'loc')
            loc_element.text = url

        tree = et.ElementTree(root)
        tree.write(filename, encoding='utf-8', xml_declaration=True)


class RobotsTxt:
    def __init__(self, api: ServerApi, path_to_sitemap: str) -> None:
        self.api = api
        self.path_to_sitemap = path_to_sitemap

    def save_to_txt(self, filename: pathlib.Path) -> None:
        content = f'''User-agent: *
Disallow: 
Sitemap: ''' + self.path_to_sitemap

        with open(filename, 'w') as h:
            h.write(content)
