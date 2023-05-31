import unittest
import pathlib

import controller

from .ServerMock import ServerMock


class TestMerchModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = ServerMock()
        self.merch = controller.Merch(self.server)

    def test_MerchCategory_caption(self):
        c = controller.MerchCategory.CDS
        self.assertEqual(c.caption, 'CDs')

        c = controller.MerchCategory.CLOTHS
        self.assertEqual(c.caption, 'Kleidung')

        c = controller.MerchCategory.MISC
        self.assertEqual(c.caption, 'Sonstiges')

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        for value_str in controller.MerchCategory:
            enum_value = controller.MerchCategory(value_str)
            self.merch.load_from_file(enum_value)

        self.merch.render()
        self.assertIsNotNone(self.merch.template)
