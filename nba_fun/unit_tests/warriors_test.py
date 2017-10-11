from unittest import TestCase
from nba_fun.warriors import get_roster_stats


class WarriorTest(TestCase):
    def test_get_roster_status(self):
        valid_roster_stats = {'Andre Iguodala': 0,
                              'Damian Jones': 0,
                              'David West': 0,
                              'Draymond Green': 0,
                              'Ian Clark': 0,
                              'JaVale McGee': 4,
                              'James Michael McAdoo': 2,
                              'Kevin Durant': 15,
                              'Kevon Looney': 0,
                              'Klay Thompson': 3,
                              'Matt Barnes': 0,
                              'Patrick McCaw': 4,
                              'Shaun Livingston': 0,
                              'Stephen Curry': 9,
                              'Zaza Pachulia': 6}
        self.assertDictEqual(get_roster_stats(), valid_roster_stats)
