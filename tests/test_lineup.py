import unittest

import controller


class TestLineupModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = controller.BaseWebServer()
        self.lineup = controller.Lineup(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.lineup.load_from_file()
        self.lineup.render()

        self.assertIsNotNone(self.lineup.template)
