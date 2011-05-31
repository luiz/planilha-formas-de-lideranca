import unittest
from lideranca import CSVParser, Column, Citation

class CSVParserTest(unittest.TestCase):
	header = 'A Column,"Nice, nice column",Just another column,One more column,Owner'

	def test_detects_columns_in_a_line(self):
		line = '"Gui, Lucas, Ceci","Paulo, Sr. Saude",Sr. Saude,Gui,Erich Egert'
		csv = self.build_csv_with_lines(line)
		result = CSVParser().parse(csv)
		self.assertEqual(1, len(result))
		self.assertEqual(5, len(result[0]))

	def test_detects_columns_in_many_lines(self):
		first_line = '"Gui, Lucas, Ceci","Paulo, Sr. Saude",Sr. Saude,Gui,Erich Egert'
		second_line = 'Ceci,Gui,Sr. Saude,Gui,Paulo'
		csv = self.build_csv_with_lines(first_line, second_line)
		result = CSVParser().parse(csv)
		self.assertEqual(2, len(result))
		self.assertEqual(5, len(result[0]))
		self.assertEqual(5, len(result[1]))
		
	def test_parses_one_line_csv(self):
		line = '"Gui, Lucas, Ceci","Paulo, Sr. Saude",Sr. Saude,Gui,Erich Egert'
		csv = self.build_csv_with_lines(line)
		expected = [Column('A Column', Citation('Gui'), Citation('Lucas'), Citation('Ceci')),
					Column('Nice, nice column', Citation('Paulo'), Citation('Sr. Saude')),
					Column('Just another column', Citation('Sr. Saude')),
					Column('Owner', Citation('Erich Egert'))]
		self.assertEqual(expected, CSVParser().parse(csv))

	def build_csv_with_lines(self, *lines):
		return [self.header] + [line for line in lines]

if __name__ == "__main__":
	unittest.main()
