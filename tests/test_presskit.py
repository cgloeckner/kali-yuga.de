import unittest

import controller


class TestPresskitModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = controller.BaseWebServer()
        self.presskit = controller.Presskit(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.presskit.build()
