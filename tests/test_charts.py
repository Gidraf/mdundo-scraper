import unittest
from mdundo.charts import Chart
from string import ascii_lowercase
from mdundo import mdundo_url

class ChartTest(unittest.TestCase):

    def test_weekly_to_100(self):
        chart = Chart("ke")
        self.assertEqual(len(chart.weekly_top_100()["result"]),100)
        self.assertEqual(chart.weekly_top_100()["count"],100)


    def test_monthly_top_20(self):
        chart = Chart("ke")
        self.assertEqual(len(chart.monthly_top_20()["result"]),20)
        self.assertEqual(chart.monthly_top_20()["count"],20)

    def test_new_releases(self):
        chart = Chart("ke")
        self.assertNotEqual(chart.new_releases()["result"],[])