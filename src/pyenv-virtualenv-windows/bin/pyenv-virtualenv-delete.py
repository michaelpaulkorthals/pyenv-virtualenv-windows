##
#  @package pyenv-virtualenv-delete
#  @file pyenv-virtualenv-delete.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Utility application to delete a virtual environment from the
#  related Python version.
#

# --- IMPORTS ----------------------------------------------------------

# Python
import argparse
import os
import shutil
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
		'\x1b[37mINFO      %s\x1b[0m'
		 %
		'Install it using "pip". Then try again.')
	import virtualenv

# My
import lib.log as log
import lib.hlp as hlp
import lib.tbl as tbl

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
			# Optimize arguments
			version: str = args.version.strip()
			name: str = args.name.strip()
			# Filter version (by wildcard in name)
			vers = hlp.getPythonVersions(
				version,
				venv_capable=True,
				as_paths=True
			)
			envs = []
			for ver in vers:
				ver_envs = hlp.getEnvs(
					ver,
					name=name,
					as_paths=True
				)
				for env in ver_envs:
					envs.append(env)
			# End for
			if len(envs) == 0:
				log.warning(f'"Python {version}" virtual environments "{name}" not found.')
				log.info(f'Call "pyenv virtualenvs". Then try "pyenv virtualenvs-delete" again, giving correct arguments.')
				rc = 0
				break
			# Load data for table
			data = [
				[tbl.HEADER, 'Item', 'Version', 'Name', 'Path'],
				[tbl.SEPARATOR]
			]
			for i in range(len(envs)):
				env = envs[i]
				version1, name1, path1 = hlp.parseEnvDir(env)
				data.append(
					[tbl.DATA, i + 1, f'\x1b[92m{version1}\x1b[0m', f'\x1b[91m{name1}\x1b[0m', path1]
				)
			data.append([tbl.SEPARATOR])
			# Ensure correct grammar in all dynamic strings
			plural=''
			plural1 = 'this'
			plural2 = 'has'
			if len(envs) != 1:
				plural = 's'
				plural1 = 'these'
				plural2 = 'have'
			# Output actual arguments
			print('')
			log.notice(f'Deleting {len(envs)} Python virtual environment{plural} from "pyenv":')
			log.notice(f'  * Version: \x1b[0m"\x1b[92m{version}\x1b[0m"')
			log.notice(f'  * Name:    \x1b[0m"\x1b[91m{name}\x1b[0m"')
			# Display list of virtual environments to be deleted
			table: tbl.SimpleTable = tbl.SimpleTable(
				data=data,
				headline=f'\x1b[91mSELECTED PYTHON VIRTUAL ENVIRONMENT{plural.upper()} TO DELETE:\x1b[0m'
			)
			table.run()
			# Let the user decide what to do
			# noinspection SpellCheckingInspection
			s = input(f'\x1b[94mDo you really want to delete {plural1} item{plural}?\x1b[0m [\x1b[91myes\x1b[0m/\x1b[92mNo\x1b[0m]: ').strip().lower()
			if (s == '') or (not s.startswith('y')):
				rc = 130
				log.verbose(f'Cancelled (RC = {rc}).')
				sys.exit(rc)
			# Delete the selected virtual environments
			for env in envs:
				# Remove junctions to this "env"
				junctions = hlp.getEnvJunctions(env)
				for junction in junctions:
					os.remove(junction)
				# Recursive remove this "env"
				shutil.rmtree(env)
			# Log success message
			log.success(
				f'Matching "{name}", {len(envs)} virtual environment{plural} and its junction{plural} {plural2} been deleted from "pyenv".'
			)
			# Go on
			break
		# End while
	except SystemExit:
		pass
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
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv-delete',
			description='Delete existing virtual environment in "pyenv". Wildcards are allowed.'
		)
		# Add positional str argument
		parser.add_argument(
			'version',
			help='Python version, which contains the virtual environment you want to delete.'
		)
		# Add positional str argument
		parser.add_argument(
			'name',
			help='Short name of the Python virtual environment, which you want to delete.'
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
			log.verbose('Parsing arguments ...')
			args, rc = parseCliArguments()
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

