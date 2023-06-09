import unittest

import controller


class TestFeedModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = controller.BaseWebServer()
        self.feed = controller.Feed(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.feed.load_from_file()
        self.feed.render()

        self.assertIsNotNone(self.feed.template)
