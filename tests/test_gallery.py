import unittest
import pathlib

import controller

from .ServerMock import ServerMock


class TestGalleryModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = ServerMock()
        self.gallery = controller.Gallery(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.gallery.load_from_disc()
        self.gallery.render()

        self.assertIsNotNone(self.gallery.template)
