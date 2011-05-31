import csv

class CSVParser:
	def parse(self, file_content):
		reader = csv.reader(file_content)
		column_names = reader.next()
		lines = []
		for line in reader:
			names_with_lines = zip(column_names, line)
			lines.append(map(lambda name_with_line: Column(name_with_line[0], name_with_line[1]), names_with_lines))
		return lines

class Column:
	def __init__(self, name, *citations):
		self.name = name
		self.citations = citations

	def __repr__(self):
		return self.name + ': "' + ', '.join(["'" + repr(citation) + "'" for citation in self.citations]) + '"'

class Citation:
	def __init__(self, name):
		self.name = name

	def __repr__(self):
		return self.name
