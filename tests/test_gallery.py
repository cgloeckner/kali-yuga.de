import unittest
import pathlib

import controller


class TestGalleryModule(unittest.TestCase):

    def setUp(self) -> None:
        self.gallery = controller.Gallery(root=pathlib.Path('./'), email='foo@bar.com')

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.gallery.load_from_disc()
        self.gallery.render(contact_email=self.gallery.email)

        self.assertIsNotNone(self.gallery.template)
