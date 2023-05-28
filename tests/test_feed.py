import unittest
import pathlib

import controller


class TestFeedModule(unittest.TestCase):

    def setUp(self) -> None:
        self.feed = controller.Feed(root=pathlib.Path('./'), email='foo@bar.com')

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.feed.load_from_file()
        self.feed.render(contact_email=self.feed.email)

        self.assertIsNotNone(self.feed.template)
