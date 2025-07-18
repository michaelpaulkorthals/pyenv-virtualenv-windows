##
#  @package pyenv-virtualenv-props
#  @file pyenv-virtualenv-props.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Utility application to configure the project properties
#  in "pyenv-virtualenv".
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
#  @param args Parsed command line arguments of this application.
#  @return RC = 0 or other values in case of error.
def run(args: argparse.Namespace) -> int:
	rc: int = 0
	cwd = os.getcwd()
	# noinspection PyBroadException
	try:
		while True:
			if args.__contains__('select_set'):
				log.verbose('Setting project properties ...')
				rc = hlp.setProjectProperties(args.version, args.name)
				if rc == 0:
					log.verbose('Project properties successfully set.')
				else:
					log.error('Cannot set project properties.')
			elif args.__contains__('select_unset'):
				log.verbose('Unsetting project properties ...')
				rc = hlp.unsetProjectProperties()
				if rc == 0:
					log.verbose('Project properties successfully unset.')
				else:
					log.error('Cannot unset project properties.')
			elif args.__contains__('select_list'):
				log.verbose('Showing list of project properties ...')
				rc = hlp.listProjectProperties()
				if rc == 0:
					log.verbose(
						'Project properties list successfully shown.'
					)
				else:
					log.error('Cannot show project properties.')
			# End if
			log.verbose(f'Done (RC = {rc}).')
			# Go on
			break
		# End while
	except:
		log.error(sys.exc_info())
		rc = 1
	finally:
		os.chdir(cwd)
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
def parseCliArguments() -> tuple[(argparse.Namespace, None), int]:
	rc: int = 0
	# noinspection PyBroadException
	try:
		# Create main parser
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv-props',
			description='Manage virtual environment-related project ' +
			'properties.'
		)
		# Create subparsers collection
		subparsers = parser.add_subparsers(help='subcommand help')
		# Add 1st subparser
		parser_set = subparsers.add_parser(
			'set',
			aliases=['s'],
			description='Set project properties inside CWD = project folder.'
		)
		# Add positional str argument to SET subparser
		parser_set.add_argument(
			'version',
			help='Number of Python version, already installed in "pyenv".'
		)
		# Add positional str argument to SET subparser
		parser_set.add_argument(
			'name',
			help='Short name of required Python virtual environment.'
		)
		# Add hidden flag
		parser_set.add_argument(
			'select_set',
			action='store_true',
			help=argparse.SUPPRESS  # Don't show in --help
		)
		# Add 2nd subparser
		parser_unset = subparsers.add_parser(
			'unset',
			aliases=['u', 'unset', 'unlink', 'd', 'del', 'delete', 'r', 'rm', 'remove'],
			description='Unset project properties inside CWD = project folder.'
		)
		# Add hidden flag
		parser_unset.add_argument(
			'select_unset',
			action='store_true',
			help=argparse.SUPPRESS  # Don't show in --help
		)
		# Add 3rd subparser
		parser_list = subparsers.add_parser(
			'list',
			aliases=['l', 'ls'],
			description='Read and list local project properties.',
			help='Read and list local project properties.'
		)
		# Add flag
		parser_list.add_argument(
			'select_list',
			action='store_true',
			help=argparse.SUPPRESS  # Don't show in --help
		)
# --- END CHANGE -------------------------------------------------------
		return parser.parse_args(), rc
	except SystemExit:
		return None, 0  # -h, --help
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
			log.verbose('Parsing arguments ...')
			args, rc = parseCliArguments()
			if rc != 0:
				break
			if args is None:  # -h, --help
				break
			log.debug(f'Arguments: {args}')
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

