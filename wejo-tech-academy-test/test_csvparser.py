import unittest
from unittest.mock import Mock
import csvparser


class TestParser(unittest.TestCase):
    # Define Method
    def test_read_row(self):
        file = Mock()
        file.configure_mock(
            **{'readline.return_value': '\'Vehicle1\',\'Vehicle2\''})

        # Expected
        expected = ("'Vehicle1' - 'Vehicle2'")

        # Result
        result = csvparser.read_row(file)
        print(result)

        # Assertion
        assert result == expected

    # def test_parse_row():
    #     expected = ['VehicleD' , 'Driver Side Window', 'Down,'']
    #     actual = csvparser.parse_row('"Kacie","Holland","Principal Consultant",""')
    #     assert expected == actual


if __name__ == "__main__":
    unittest.main()
