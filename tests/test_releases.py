import unittest

import controller


class TestReleasesModule(unittest.TestCase):

    def setUp(self) -> None:
        self.server = controller.BaseWebServer()
        self.merch = controller.Merch(self.server)

        for category_str in controller.MerchCategory:
            self.merch.load_from_file(controller.MerchCategory(category_str))

        self.releases = controller.Releases(self.server)

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.releases.load_from_merch(self.merch)
        self.releases.render()

        self.assertIsNotNone(self.releases.template)
