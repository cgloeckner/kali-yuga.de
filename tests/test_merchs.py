import unittest
import pathlib
import datetime

import controller


class TestMerchModule(unittest.TestCase):

    def setUp(self) -> None:
        self.merch = controller.Merch(root=pathlib.Path('./'), email='foo@bar.com')

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        for value_str in controller.MerchCategory:
            enum_value = controller.MerchCategory(value_str)
            self.merch.load_from_file(enum_value)

        self.merch.render(contact_email=self.merch.email)
        self.assertIsNotNone(self.merch.template)
