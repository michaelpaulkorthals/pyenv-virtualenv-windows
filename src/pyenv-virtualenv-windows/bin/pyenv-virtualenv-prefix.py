##
#  @package pyenv-virtualenv-prefix
#  @file pyenv-virtualenv-prefix.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Utility application to output the virtual environment path prefix.
#

# --- IMPORTS ----------------------------------------------------------

# Python
import argparse
import os
import sys

# Avoid colored output problems
os.system('')

# Community
try:
	import virtualenv
except ImportError():
	print(
		'\x1b[101mCRITICAL %s\x1b[0m'
		%
		'Cannot find package "%s".'
		%
		'virtualenv'
	)
	print(
		'\x1b[37mINFO     %s\x1b[0m'
		 %
		'Install it using "pip". Then try again.')
	import virtualenv

# My
import lib.hlp as hlp
import lib.log as log


# --- RUN ---------------------------------------------------------------

## Sub routine to run the application.
#
#  @param args Given command line arguments.
#  @return RC = 0 or other values in case of error.
def run(args: argparse.Namespace) -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		while True:
			log.verbose(
				'Display "real_prefix" for a Python virtual environment version.'
			)
			try:
				# Use the given "version" argument
				version: str = args.name
				name_given = True
			except AttributeError:
				name_given = False
			if name_given:
				result = ''
				filtered_envs = hlp.getAllEnvs(
					args.name,
					as_paths=True
				)
				if len(filtered_envs) > 0:
					for env in filtered_envs:
						pl = env.split(os.sep)
						for i in range(len(pl)):
							item = pl[i]
							if item == 'versions':
								if len(result) > 0:
									result += '\r\n'
								result += os.sep.join(pl[:i + 2])
					print(result)
				else:
					log.warning(f'Cannot find virtual environments like "{args.name}".')
					log.info('Try again with another filter by name. Wildcards are implemented.')
			else:
				# Check if the path to Python executable
				# passes into a virtual environment.
				log.debug(f'Python executable: "{sys.executable}".')
				pl = sys.executable.split(os.sep)
				if (
					('envs' in pl)
					and
					('Scripts' in pl)
					and
					(os.path.isfile(
						os.path.join(
							os.path.dirname(sys.executable),
							'..',
							'pyvenv.cfg'
						)
					))
				):
					# Virtual environment detected
					result = ''
					for i in range(len(pl)):
						item = pl[i]
						if item == 'versions':
							result = os.sep.join(pl[:i + 2])
							break
					if result == '':
						log.error('Cannot determine Python version for this virtual environment.')
						rc = 1
						break
					print(result)
				else:
					# Not in virtual environment
					version = sys.version.split(' ')[0]
					log.warning(f'"pyenv-virtualenv": Version`{version}` is not a virtual environment.')
					rc = 5
					break
			# End if
			# Go on
			break
		# End while
	except:
		log.error(sys.exc_info())
		rc = 1
	return rc


# --- MAIN --------------------------------------------------------------

## Parse CLI arguments for this application.<br>
#  <br>
#  Implement this as required, but don't touch the interface definition
#  for input and output.
#
#  @return A tuple of:
#    * Namespace to read arguments in "dot" notation or None
#    in case of help or error.
#    * RC = 0 or another value in case of error.
def parseCliArguments0() -> tuple[(argparse.Namespace, None), int]:
	rc: int = 0
	# noinspection PyBroadException
	try:
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv-prefix',
			description='Display "real_prefix" for a Python virtual environment version.'
		)
# --- END CHANGE -------------------------------------------------------
		return parser.parse_args(), rc
	except SystemExit:
		return None, 0
	except:
		log.error(sys.exc_info())
		return None, 1

## Parse CLI arguments for this application.<br>
#  <br>
#  Implement this as required, but don't touch the interface definition
#  for input and output.
#
#  @return A tuple of:
#    * Namespace to read arguments in "dot" notation or None
#    in case of help or error.
#    * RC = 0 or another value in case of error.
def parseCliArguments1() -> tuple[(argparse.Namespace, None), int]:
	rc: int = 0
	# noinspection PyBroadException
	try:
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv-prefix',
			description='Display "real_prefix" for a Python virtual environment version.'
		)
		# Add positional str argument
		parser.add_argument(
			'name',
			help='Short name of an installed Python virtual environment. Default: Empty string = analyze the CWD.'
		)
# --- END CHANGE -------------------------------------------------------
		return parser.parse_args(), rc
	except SystemExit:
		return None, 0
	except:
		log.error(sys.exc_info())
		return None, 1

## Main routine of the application.
#
#  @return RC = 0 or other values in case of error.
def main() -> int:
	# noinspection PyBroadException
	try:
		while True:
			# Audit the operating system platform
			rc = hlp.auditPlatform('Windows')
			if rc != 0:
				# Deviation: Reject unsupported platform
				break
			# Audit the global Python version number
			rc = hlp.auditGlobalPythonVersion('3.6')
			if rc != 0:
				# Deviation: Reject unsupported Python version
				break
			# Initialize the colored logging to console
			log.initLogging()
			# Audit the "pyenv" version number
			rc = hlp.auditPyEnv('3')
			if rc != 0:
				# Deviation: Reject unsupported "pyenv" version
				break
			# Parse arguments
			# NOTE: Sorry, this is a complicated workaround to
			# bypass the lack of applicability of Python "ArgumentParser"
			# class. This simple use case to set required = False for
			# positional argument is not included and must be patched
			# away here.
			log.verbose('Parsing arguments ...')
			args = None
			args_list = sys.argv.copy()  # Clone
			# Strip program executable path
			args_list.pop(0)
			# Detect and remove all optional arguments,
			# which are not related to the positional arguments
			help_requested = False
			for i in reversed(range(len(args_list))):
				arg = args_list[i]
				if arg in ['-h', '--help']:
					help_requested = True
					args_list.pop(i)
			# Calculate the count of positional arguments
			positional_count = len(args_list)
			if (
					help_requested
					or
					(positional_count not in [0, 1])
			):
				text = ("""
Usage: pyenv virtualenv-prefix [-h] [name]

Display "real_prefix" for a Python virtual environment version.

Positional arguments (can be omitted):
  [name]      Short name of an installed Python virtual environment.
              Default: Empty string = analyze the CWD.
Options:
  -h, --help  Show this help message and exit
				""").strip()
				print(text)
			elif positional_count == 0:
				# Case 1: single positional argument must be "Name"
				args, rc = parseCliArguments0()
			elif positional_count == 1:
				# Case 2: duo positional arguments must be "Version" and "Name"
				args, rc = parseCliArguments1()
			if rc != 0:
				break
			if args is None:  # -h, --help
				break
			# Run this application
			log.verbose('Running application ...')
			rc = run(args)
			if rc != 0:
				break
			# Go on
			break
		# End while
	except Exception as exc:
		if log.isInitialized():
			log.error(sys.exc_info())
		else:
			print(
				'\x1b[91mERROR: Unexpected error "%s".\x1b[0m'
				%
				str(exc)
			)
		rc = 1
	return rc


if __name__ == "__main__":
	sys.exit(main())

# --- END OF CODE ------------------------------------------------------

