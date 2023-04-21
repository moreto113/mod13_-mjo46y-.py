import unittest


class TestInputs(unittest.TestCase):
    def test_symbol_valid(self):
        symbol = "GOOGL"
        self.assertTrue(symbol.isalpha() and symbol.isupper() and len(symbol) >= 1 and len(symbol) <= 7)

    def test_chart_type_valid(self):
        chart_type = "2"
        self.assertTrue(chart_type.isdigit() and (chart_type == "1" or chart_type == "2"))

    def test_time_series_valid(self):
        time_series = "3"
        self.assertTrue(time_series.isdigit() and len(time_series) == 1 and int(time_series) >= 1 and int(time_series) <= 4)

    def test_start_date_valid(self):
        start_date = "2002-01-13"
        self.assertTrue(len(start_date) == 10 and start_date[4] == start_date[7] == "-" and start_date[:4].isdigit() and start_date[5:7].isdigit() and start_date[8:].isdigit())

    def test_end_date_valid(self):
        end_date = "2023-01-13"
        self.assertTrue(len(end_date) == 10 and end_date[4] == end_date[7] == "-" and end_date[:4].isdigit() and end_date[5:7].isdigit() and end_date[8:].isdigit())
        
if __name__ == "__main__":
    unittest.main()