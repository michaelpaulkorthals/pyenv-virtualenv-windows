##
#  @package pyenv-virtualenv-init
#  @file pyenv-virtualenv-init.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Utility to reconfigure 'pyenv-virtualenv' for Windows
#  after upgrading 'pyenv'
#

# --- IMPORTS ----------------------------------------------------------

# Python
import argparse
import os
import subprocess
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

# noinspection PyUnusedLocal

## Sub routine to run the application.
#
#  @param args Parsed command line arguments of this application.
#  (e.g. for CMD or PowerShell).
#  @return RC = 0 or other values in case of error.
def run(args: argparse.Namespace) -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		while True:
			corrected: bool = False
			log.info('Checking operation environment.')
			# Check if path to 'shims' directory of the plugin has
			# higher priority than 'bin' and 'shims' folders of 'pyenv'.
			log.verbose('Checking PYENV_ROOT ...')
			if not 'PYENV_ROOT' in os.environ:
				log.error('Cannot find "PYENV_ROOT" in the environment variables.')
				log.info('Possibly "pyenv" for Windows has been uninstalled or damaged.')
				log.info('Possibly you need to install the newest versions of "pyenv" and "pyenv-virtualenv" for Windows.')
				break
			log.verbose('"PYENV_ROOT" environment variable exists.')
			pyenv_root_dir = os.environ['PYENV_ROOT'].strip()
			log.verbose(f'Checking existence of directory "{pyenv_root_dir}" ...')
			if not os.path.isdir(pyenv_root_dir):
				log.error(f'Cannot find directory "{pyenv_root_dir}".')
				log.info('Possibly "pyenv" for Windows has been uninstalled or damaged.')
				log.info('Possibly you need to install the newest versions of "pyenv" and "pyenv-virtualenv" for Windows.')
				break
			log.verbose(f'Directory "{pyenv_root_dir}" exists.')
			log.verbose('Managing PATH priorities ...')
			pve_path1 = os.path.join(
				pyenv_root_dir,
				'plugins',
				'pyenv-virtualenv',
				'shims'
			)
			pve_index = []
			pve_paths = []
			paths = os.environ['PATH'].split(';')
			pev_path1 = os.path.join(
				pyenv_root_dir,
				'bin'
			)
			pev_path2 = os.path.join(
				pyenv_root_dir,
				'shims'
			)
			pev_index = []
			pev_paths = []
			for i in range(len(paths)):
				path = paths[i]
				path = path.strip()
				if not os.path.isdir(path):
					log.warning(f'Directory "{path}" in PATH is not available.')
					log.info(f'Please manually correct this deviation afterward, if necessary.')
				if path == pve_path1:
					pve_index.append(i)
					pve_paths.append(path)
				if path == pev_path1:
					pev_index.append(i)
					pev_paths.append(path)
				if path == pev_path2:
					pev_index.append(i)
					pev_paths.append(path)
			# End for
			if len(pev_index) == 0:
				log.error('Cannot recognize "pyenv" in PATH.')
				log.info('Possibly "pyenv" for Windows has been uninstalled or damaged.')
				log.info('Possibly you need to install the newest versions of "pyenv" and "pyenv-virtualenv" for Windows.')
				break
			if len(pve_paths) > 1:
				# Auto-remove multiple 'pyenv-virtualenv' 'shims'
				# entries. There must only be one.
				# The one with the highest priority.
				for j in reversed(range(len(pve_index[1:]))):
					removal_index = pve_index[j]
					path = paths.pop(removal_index)
					log.warning(f'Obsolete clone of path "{path}" found in PATH.')
					log.info(f'This entry has been automatically removed.')
					# Taking account of this removal,
					# correct the 'pyenv' PATH indices.
					for k in range(len(pev_index)):
						index = pev_index[k]
						if index < removal_index:
							pev_index[k] -= 1
						# End if
					# End for
				# End for
				pve_index = pve_index[0:1]
			# End if
			min_pev_index = min(pev_index)
			if len(pve_paths) == 0:
				corrected = True
				# Prepend the missing 'shims' directory to PATH
				cmd = [
					'setx',
					'PATH',
					'{};{}'.format(pve_path1, os.environ['PATH']),
					'/m'
				]
				log.verbose(f'Execute: {cmd}')
				cp = subprocess.run(
					cmd,
					shell=True
				)
				rc = cp.returncode
				if rc != 0:
					log.error(f'Cannot permanently prepend "{pve_path1}" to the PATH environment variable. (RC = {rc}.')
					log.info('Open new console terminal as "Administrator", in which you want to try again.')
					break
			elif min_pev_index < pve_index[0]:
				corrected = True
				# Remove the existing 'shims"
				paths.pop(pve_index[0])
				# Prepend the missing 'shims' directory to PATH.
				# This command needs 'Administrator' privileges.
				cmd = [
					'setx',
					'PATH',
					'{};{}'.format(pve_path1, os.environ['PATH']),
					'/m'
				]
				log.verbose(f'Execute: {cmd}')
				cp = subprocess.run(
					cmd,
					shell=True
				)
				rc = cp.returncode
				if rc != 0:
					log.error(f'Cannot permanently prepend "{pve_path1}" to the PATH environment variable. (RC = {rc}.')
					log.info('Open new console terminal as "Administrator", in which you want to try again.')
					break
				# End if
			# Endif
			log.verbose('PATH priorities managed.')
			if corrected:
				log.success(f'Operation environment checked and corrected.')
			else:
				log.success(f'Operation environment checked.')
			log.success(f'"pyenv-virtualenv" should work as expected.')
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
def parseCliArguments() -> tuple[(argparse.Namespace, None), int]:
	rc: int = 0
	# noinspection PyBroadException
	try:
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv-init',
			description='Initialize the terminal shell to work on Python virtual environment in "pyenv".'
		)
		# Add optional argument
		parser.add_argument(
			'-s', '--shell',
			dest='shell',
			type=str,
			default='',
			help='Command string to call a shell command or batch in the shell like you would prefer. Default: "%%COMSPEC%% /K" = Windows CMD.'
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

