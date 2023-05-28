import unittest
import pathlib

import controller


class TestLineupModule(unittest.TestCase):

    def setUp(self) -> None:
        self.lineup = controller.Lineup(root=pathlib.Path('./'), email='foo@bar.com')

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.lineup.load_from_file()
        self.lineup.render(contact_email=self.lineup.email)

        self.assertIsNotNone(self.lineup.template)
