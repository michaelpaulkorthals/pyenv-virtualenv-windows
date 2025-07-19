##
#  @package pyenv-virtualenvs
#  @file pyenv-virtualenvs.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Utility application to list the installed Python versions and
#  virtual environments. In addition the Project properties will
#  be listed and its locations will be displayed in a folder tree.
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
import lib.tbl as tbl


# --- RUN ---------------------------------------------------------------

## Sub routine to run the application.
#
#  @return RC = 0 or other values in case of error.
def run() -> int:
	rc: int = 0
	cwd = os.getcwd()
	# noinspection PyBroadException
	try:
		while True:
			log.verbose(
				'Listing Python virtual environments in "pyenv".'
			)
			log.verbose('Determining Python versions ...')
			# Determine Python version, which is capable
			# to install Python virtual environment.
			versions_dir = os.path.join(
				os.environ['PYENV_ROOT'],
				'versions'
			)
			if not os.path.isdir(versions_dir):
				log.error('Cannot find any Python version in "pyenv".')
				log.info('Install a Python version 3.3+ into "pyenv".')
				rc = 1
				break
			vers = hlp.getPythonVersions(
				'*',
				venv_capable=False,
				as_paths=True
			)
			if len(vers) == 0:
				log.error('Cannot find a Python version in "pyenv".')
				log.info('Install a Python version 3.3+ into "pyenv".')
				rc = 1
				break
			per = os.environ['PYENV_ROOT']
			# Pass 1: Collect the Python versions.
			pyts = [
				[tbl.HEADER, 'G', 'Venv-Capable', 'Version', '"pyenv" Location'],
				[tbl.SEPARATOR]
			]
			for ver in vers:
				pyts_item = [
					tbl.DATA,
					hlp.getGlobalStar(ver),
					hlp.getColoredVenvCapability(ver),
					os.path.basename(ver),
					'%PYENV_ROOT%' + os.sep + ver[len(per):]
				]
				pyts.append(pyts_item)
			# End for
			pyts.append([tbl.SEPARATOR])
			# Pass 2: Collect the virtual environments.
			pves = [
				[tbl.HEADER, 'A', 'Version', 'Name', '"pyenv" Location'],
				[tbl.SEPARATOR]
			]
			for ver in vers:
				venvs = hlp.getEnvs(ver,'*', as_paths=True)
				for venv in venvs:
					act = ' '
					if (
						('PROMPT' in os.environ)
						and
						(f'({os.path.basename(venv)})' in os.environ['PROMPT'])
					):
						act = '*'
					pves.append([
						tbl.DATA,
						act,
						os.path.basename(ver),
						os.path.basename(venv),
						'%PYENV_ROOT%' + os.sep + venv[len(per):]
					])
			# End for
			pves.append([tbl.SEPARATOR])
			# Pass 3: Output list of Python versions.
			table_pyts = tbl.SimpleTable(
				pyts,
				headline='INSTALLED PYTHON VERSIONS (G = global):'
			)
			table_pyts.run()
			# Pass 4: Output list of virtual environments.
			table_pves = tbl.SimpleTable(
				pves,
				headline='AVAILABLE PYTHON VIRTUAL ENVIRONMENTS (A = active):'
			)
			table_pves.run()
			# Output list of project properties (if exists)
			hlp.listProjectProperties()
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
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenvs',
			description='Output lists of Python versions, virtual environments and related project properties.'
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
			# Run this application
			log.verbose('Running application ...')
			rc = run()
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

