##
#  @package log
#  @file log.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Library to output colored logging in "pyenv-virtualenv".
#

# --- IMPORTS ----------------------------------------------------------

# Python
import collections
import os
import platform
import traceback

# Community
# (None)

# My
# (None)


# --- CONSTANTS --------------------------------------------------------

## List of log level attributes for comprehensive logging.
#  NOTE: Color of level 20 is default color in terminals with
#  black background like e.g. the cmd.exe window in Windows.
#  @see Logging
LOG_LEVELS =  [
	{'level': 50, 'name': 'critical', 'color': '\x1b[101m'},
	{'level': 40, 'name': 'error',    'color': '\x1b[91m'},
	{'level': 35, 'name': 'success',  'color': '\x1b[92m'},
	{'level': 30, 'name': 'warning',  'color': '\x1b[93m'},
	{'level': 25, 'name': 'notice',   'color': '\x1b[95m'},
	{'level': 20, 'name': 'info',     'color': '\x1b[37m'},
	{'level': 15, 'name': 'verbose',  'color': '\x1b[94m'},
	{'level': 10, 'name': 'debug',    'color': '\x1b[32m'},
	{'level':  5, 'name': 'spam',     'color': '\x1b[90m'}
]

## Actual log level. It could be overridden by environment variable.
#  Default: 20 (name: 'info')
LOG_LEVEL: int = 20

## Width of the column, which shows the log level name.
#  Default: 0. It will be calculated automatically.
LEVEL_COLUMN_WIDTH: int = 0

# --- VARIABLES -------------------------------------------------------

## Flag, which states, that the logging is initialized for this program.
_is_initialized: bool = False

# --- CLASSES ----------------------------------------------------------

## Named tuple definition of unexpected exception.
UnexpExcInfo = collections.namedtuple(
	'ExceptionInfo',
	['typ', 'val', 'fil', 'lin', 'qnm', 'tbk']
)


# --- HELPER -----------------------------------------------------------

## Initialize the logging.
def initLogging():
	# Define global variables
	global LOG_LEVEL
	global LEVEL_COLUMN_WIDTH
	# Automatically calculate LEVEL_COLUMN_WIDTH
	for item in LOG_LEVELS:
		lln = len(item['name'])
		if LEVEL_COLUMN_WIDTH < lln:
			LEVEL_COLUMN_WIDTH = lln
	# Override LOG_LEVEL by environment variable
	if 'LOG_LEVEL' in os.environ:
		LOG_LEVEL = int(os.environ['LOG_LEVEL'])
	# Set logging is initialized
	global _is_initialized
	_is_initialized = True

# Check if logging is initialized.
#
#  return Flag, which states that logging is initialized.
def isInitialized() -> bool:
	return _is_initialized

## Parse the exception data for human-readable information.
#  This allows the developer to identify and locate
#  the exception.
#
#  @param exc_info Output of sys.exc_info().
#  @return Human-readable information or empty string if
def getExcInfoStr(exc_info: tuple) -> str:
	maj, mno, _ = platform.python_version_tuple()
	maj = int(maj)
	mno = int(mno)
	ty, va, tb = exc_info
	if (maj > 3) or ((maj == 3) and (mno >= 11)):
		qnm = tb.tb_frame.f_code.co_qualname
	else:
		qnm = tb.tb_frame.f_code.co_name
	i = UnexpExcInfo(
		ty.__name__,
		va,
		tb.tb_frame.f_code.co_filename,
		tb.tb_lineno,
		qnm,
		tb
	)
	tbs =''.join(traceback.extract_tb(i.tbk).format())
	return (
		f'Unexpected {i.typ}, "{i.val}"\n' +
		f'\x20\x20File: "{i.fil}:{i.lin}"\n' +
		f'\x20\x20Pos.: {i.qnm}, line {i.lin}\n' +
		f'Traceback (most recent call last):\n' +
		f'{tbs}'
	)

## Get text string from "msg" object argument.
#
#  @param msg Message as str or result of "sys.exc_info()" as tuple.
#  @return Human-readable message.
def getMsgText(msg: (str, tuple)) -> str:
	if isinstance(msg, str):
		return msg
	elif isinstance(msg, tuple):
		return getExcInfoStr(msg)
	else:
		raise NotImplementedError

## Log leveled and colored message to console only.
#
#  @param level ID of logging level.
#  @see LOG_LEVELS
#  @param msg Message as str or result of "sys.exc_info()" as tuple.
def printLogToConsole(level: int, msg: (str, tuple)):
	for item in LOG_LEVELS:
		if (
			(level == item['level'])
			and
			(level >= LOG_LEVEL)
		):
			# Print colorized and immediately flush the output
			print(
				'{}{}{}{}\x1b[0m'.format(
					item['color'],
					item['name'].upper(),
					' ' * (
						LEVEL_COLUMN_WIDTH
						-
						len(item['name'])
						+
						1
					),
					getMsgText(msg)
				),
				flush=True
			)
			return


# --- LOGING FUNCTIONS -------------------------------------------------

## Log critical error message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def critical(msg: (str, tuple)):
	printLogToConsole(50, msg)

## Log error message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def error(msg: (str, tuple)):
	printLogToConsole(40, msg)

## Log success message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def success(msg: (str, tuple)):
	printLogToConsole(35, msg)

## Log warning message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def warning(msg: (str, tuple)):
	printLogToConsole(30, msg)

## Log notice message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def notice(msg: (str, tuple)):
	printLogToConsole(25, msg)

## Log info message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def info(msg: (str, tuple)):
	printLogToConsole(20, msg)

## Log verbose message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def verbose(msg: (str, tuple)):
	printLogToConsole(15, msg)

## Log debug message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def debug(msg: (str, tuple)):
	printLogToConsole(10, msg)

## Log spam message colored to console only.
#
# @param msg Message as str or result of sys.exc_info().
def spam(msg: (str, tuple)):
	printLogToConsole(5, msg)


# --- END OF CODE ------------------------------------------------------

