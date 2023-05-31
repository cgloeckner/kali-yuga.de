import unittest

import controller

from .ServerMock import ServerMock


class TestPresskitModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = ServerMock()
        self.presskit = controller.Presskit(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.presskit.build()
