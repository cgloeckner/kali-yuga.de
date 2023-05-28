import unittest
import pathlib
import datetime

import controller


class TestGigsModule(unittest.TestCase):

    def setUp(self) -> None:
        self.gigs = controller.Gigs(root=pathlib.Path('./'), email='foo@bar.com')

    def test_process_gigs(self):
        raw = {
            'second-gig': {
                'title': 'The same month',
                'date': datetime.date(2000, 10, 24),
                'location': 'random town festival'
            },
            'first-gig': {
                'title': 'The first gig ever',
                'date': datetime.date(2000, 10, 22),
                'location': 'Mom"s basement'
            },
            'third-gig': {
                'title': 'later that year',
                'date': datetime.date(2000, 12, 7),
                'location': 'somewhere outdoors'
            },
            'last-gig': {
                'title': 'sucking in front of 20 people',
                'date': datetime.date(2002, 2, 13),
                'location': 'small club'
            }
        }

        grouped = controller.Gigs.process_gigs(raw)

        self.assertEqual(len(grouped.keys()), 2)
        self.assertEqual(len(grouped[2000]), 3)
        self.assertEqual(len(grouped[2002]), 1)

        self.assertEqual(grouped[2000][0], raw['first-gig'])
        self.assertEqual(grouped[2000][1], raw['second-gig'])
        self.assertEqual(grouped[2000][2], raw['third-gig'])
        self.assertEqual(grouped[2002][0], raw['last-gig'])

    def test_data_validation(self):
        # NOTE: loads from the files provided in this repository
        # hence this is kind of a data validation test
        self.gigs.load_from_file()
        self.gigs.render(contact_email=self.gigs.email)

        self.assertIsNotNone(self.gigs.template)
