import unittest

import controller


class TestGalleryModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = controller.BaseWebServer()
        self.gallery = controller.Gallery(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.gallery.load_from_disc()
        self.gallery.render()

        self.assertIsNotNone(self.gallery.template)
