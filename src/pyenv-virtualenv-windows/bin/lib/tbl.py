##
#  @package tbl
#  @file tbl.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Library to output colored tables in "pyenv-virtualenv".
#

# --- IMPORTS ----------------------------------------------------------

# Python
import re

# Community
# (None)

# My
try:
	# noinspection PyUnresolvedReferences
	import lib.log as log
except ImportError():
	try:
		# noinspection PyUnresolvedReferences
		import log
	except ImportError():
		# noinspection PyUnresolvedReferences
		import log


# --- CONSTANTS --------------------------------------------------------

HEADER: int = 1
SEPARATOR: int = 2
DATA: int = 3

ROW_TYPES: list[int] = [HEADER, SEPARATOR, DATA]

# --- HELPER -----------------------------------------------------------

## Calculate the length of cell content skipping ANSI ESC sequences
#  (e.g. for color).
#
#  @param cell_content Raw cell content including ANSI ESC sequences.
#  @return Length of readable cell content without ANSI ESC sequences.
#  @see https://stackoverflow.com/questions/14693701/how-can-i-remove-the-ansi-escape-sequences-from-a-string-in-python
def readableLen(cell_content: str) -> int:
	ansi_escape = re.compile(r'\x1B(?:[@-Z\\-_]|\[[0-?]*[ -/]*[@-~])')
	result = ansi_escape.sub('', cell_content)
	return len(result)


# --- CLASSES ----------------------------------------------------------

class SimpleTable:

	## CONSTRUCTOR.
	#
	#  @param data List of data row lists to define the table.
	#  @param headline Text of the headline shown above the table.
	#  Default: Empty str = No headline.
	#  @param headline_color ANSI color ESC sequence for the headline.
	#  Default: "\x1b[37m". = blue on black background
	#  @param header_color ANSI color ESC sequence for the column headers.
	#  Default: "\x1b[104m" = white on blue background.
	def __init__(
			self,
			data: list[list],
			headline: str='',
			headline_color: str='\x1b[37m',
			header_color: str='\x1b[104m'
	):
		# Initialize
		self.data = data
		self.headline=headline
		self.headline_color=headline_color
		self.header_color = header_color
		# Check for completeness
		if len(self.data) < 3:
			log.warning('Data table length is less than 3.')
			log.info('To fulfill the table design, it must have header row, separator row and a final separator row.')
			raise ValueError()
		if not isinstance(self.data[0][0], int):
			log.warning('The first column of first row is not as "int".')
			log.info('To fulfill the table design, each row must start with a row type integer constant.')
		if self.data[0][0] != HEADER:
			log.warning('First data row is not the table header.')
			log.info('To fulfil the table design, the table header must be sorted to the first index position.')
		# Check row data and add aesthetical spaces
		row_lengths: list[int] = []
		for i in range(len(self.data)):
			row = self.data[i]
			if self.data[i][0] not in ROW_TYPES:
				log.warning(f'Found not implemented value "{self.data[i][0]}" in row type column.')
				log.info(f'The first value in each row must be in "{ROW_TYPES}" = "[tbl.HEADER, tbl.SEPARATOR, tbl.DATA]".')
				raise NotImplementedError()
			if self.data[i][0] is SEPARATOR:
				self.data[i] = (
					[self.data[i][0]]
					+
					[None for _ in range(len(self.data[0]) - 1)]
				)
			row_lengths.append(len(self.data[i]))
			if (row[0] != SEPARATOR) and (row_lengths[-1] < 2):
				log.warning('Data row length is less than 2.')
				log.info('Each data and header row must have a row type column and min. 1 data cell column.')
				raise ValueError()
			for j in range(len(row)):
				if j == 0: continue  # Skip row type
				cell = str(data[i][j])
				# Add aesthetical spaces to cell,
				# clone and force as "str".
				if cell is not None:
					if not cell.startswith(' '):
						cell = ' ' + str(cell)
					if not cell.endswith(' '):
						cell += ' '
				data[i][j] = cell
			# End For
		# End for
		# Check if all rows have the same number of cells
		if not all(item == row_lengths[0] for item in row_lengths):
			log.warning(
				f'Length of each row is not identical (see {row_lengths}).')
			log.info('Check/repair the deviating rows.')
			raise ValueError()

	## Two-dimensional data table.
	#  Default: None.
	data: (list[list], None) = None

	## Column width list.
	#  Default: None.
	cw: (list[int], None) = None

	## Headline, which is printed before the table.
	headline: (str, None) = None

	## ANSI ESC-sequence for the header color.
	#  Default: "\x1b[37m".
	headline_color: str = '\x1b[37m'

	## ANSI ESC-sequence for the header color.
	#  Default: "\x1b[104m".
	header_color: str = '\x1b[104m'

	## Calculate width of each column except the row type column.
	# Store the results in the "self.cw" property.
	def calculateColumnWidth(self):
		self.cw = [int(0) for _ in range(len(self.data[0]))]
		# Calculate column with
		for item in self.data:
			if not isinstance(item[0], int):
				log.warning(f'First item in this row "{item}" is not as "int".')
				log.info('The first column in each row defines the row type as "int".')
				raise ValueError()
			if item[0] in [1, 3]:
				for i in range(len(self.cw)):
					if i == 0:
						continue  # Skip row type
					else:
						cc: str = item[i]
						l = readableLen(cc)
						if l > self.cw[i]:
							self.cw[i] = l
	## Display the data table.
	def run(self):
		print(f'\n{self.headline_color}{self.headline}\x1b[0m\n')
		self.calculateColumnWidth()
		for row in self.data:
			if row[0] == HEADER:
				row_str = ''
				for i in range(len(row)):
					if i == 0:
						continue  # Skip row type
					else:
						row_str += '{}{}{}\x1b[0m'.format(
							self.header_color,
							row[i],
							' ' * (self.cw[i] - len(row[i])),
						)
						if i < len(row) - 1:
							row_str += ' '
				# End for
				print(row_str)
			elif row[0] == SEPARATOR:
				row_width = sum(self.cw[1:]) + len(self.cw) - 2
				row_str = '-' * row_width
				print(row_str)
			elif row[0] == DATA:
				row_str = ''
				for i in range(len(row)):
					if i == 0:
						continue  # Skip row type
					else:
						row_str += '{}{}'.format(
							row[i],
							' ' * (self.cw[i] - readableLen(row[i])),
						)
						if i < len(row) - 1:
							row_str += ' '
				# End for
				print(row_str)
			# End if
		# End for


# --- END OF CODE ------------------------------------------------------

