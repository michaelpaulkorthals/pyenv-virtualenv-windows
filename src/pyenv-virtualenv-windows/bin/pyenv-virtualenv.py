##
#  @package pyenv-virtualenv
#  @file pyenv-virtualenv.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Utility application to create a new named virtual environment,
#  which depends on an installed Python version.
#

# --- IMPORTS ----------------------------------------------------------

# Python
import argparse
import os
import shutil
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
		'\x1b[37mINFO      %s\x1b[0m'
		 %
		'Install it using "pip". Then try again.')
	import virtualenv

# My
import lib.log as log
import lib.hlp as hlp

# --- RUN ---------------------------------------------------------------

## Sub routine to run the application.
#
#  @param args Parsed command line arguments of this application.
#  @return RC = 0 or other values in case of error.
def run(args: argparse.Namespace) -> int:
	cwd = os.getcwd()
	# noinspection PyBroadException
	try:
		while True:
			# Force to select the "Version" argument,
			# even if it is not given.
			try:
				# Use the given "version" argument
				version: str = args.version
				realm = 'argument'
			except AttributeError:
				# Use the "pyenv" python version
				version, realm = hlp.getPythonVersion()
			if version == '':
				log.error('Cannot determine the version number of the "pyenv" Python version.')
				log.info('Trying next, set the version number explicitly. See --help.')
				rc = 1
				break
			# Optimize arguments
			version = version.strip()
			name: str = hlp.fName(args.name)
			props: bool = args.props
			# Output actual arguments
			log.info('Creating Python virtual environment in "pyenv":')
			log.info(f'  * Version: {version} ({realm})')
			log.info(f'  * Name:    {name}')
			log.info(f'  * Set project properties: {props}')
			# Filter/select best virtual environment capable version
			selected_version_dir, rc = hlp.selectVersionDir(
				version,
				realm,
				venv_capable=True
			)
			if rc != 0:
				break
			selected_version = os.path.basename(selected_version_dir)
			# Check and make directories
			envs_dir = os.path.join(selected_version_dir, 'envs')
			if not os.path.isdir(envs_dir):
				log.verbose(f'Creating "{envs_dir}" folder ...')
				os.mkdir(envs_dir)
			# Create Python virtual environment
			venv_dir = os.path.join(envs_dir, name)
			if os.path.isdir(venv_dir):
				# Remove existing directory
				log.verbose(f'Overriding folder "{venv_dir}" ...')
				shutil.rmtree(venv_dir)
			else:
				log.verbose(f'Creating folder "{venv_dir}" ...')
			# Get executable path for the selected Python version
			python_exe_path = os.path.join(
				selected_version_dir,
				'python.exe'
			)
			# Generate Python virtual environment
			cmd = [
				python_exe_path,
				'-m',
				'venv',
				venv_dir
			]
			log.verbose(f'Execute: {python_exe_path}')
			log.info('This will take some seconds ...')
			# noinspection SpellCheckingInspection
			cp = subprocess.run(
				cmd,
				stdout=subprocess.DEVNULL,
				stderr=subprocess.DEVNULL,
				shell=True
			)
			rc = cp.returncode
			if rc != 0:
				log.error(
					'Unexpectedly cannot create ' +
					'Python virtual environment.'
				)
				log.info('Check/repair Python and "pyenv". Then try again.')
				rc = 1
				break
			# Create junction to virtual environment directory
			# within the Python versions directory.
			venv_version_dir = os.path.join(
				os.environ['PYENV_ROOT'],
				'versions',
				f'{name}-{selected_version}'
			)
			if hlp.isJunction(venv_version_dir):
				# Remove existing junction
				log.verbose(
					'Overriding junction "{}" ...'.format(
						venv_version_dir
					)
				)
				os.remove(venv_version_dir)
			else:
				log.verbose(
					'Creating junction "{}" ...'.format(
						venv_version_dir
					)
				)
			# noinspection SpellCheckingInspection
			cmd = [
				'mklink',
				'/J',
				venv_version_dir,
				venv_dir
			]
			log.verbose(f'Execute: {cmd}')
			cp = subprocess.run(
				cmd,
				stdout=subprocess.DEVNULL,
				stderr=subprocess.DEVNULL,
				shell=True
			)
			rc = cp.returncode
			if rc != 0:
				log.error(
					'Unexpectedly cannot create junction to ' +
					'Python virtual environment directory.'
				)
				log.info(
					'Check/repair security properties ' +
					'of the junction. Then try again.'
				)
				rc = 1
				break
			if props:
				log.verbose('Setting project properties ...')
				rc = hlp.setProjectProperties(selected_version, name)
				if rc == 0:
					log.verbose('Project properties successfully set.')
				else:
					log.error('Cannot set project properties.')
			# Log success message
			log.success(
				f'Virtual environment "{name}" is installed ' +
				f'in "pyenv", depending on "Python {selected_version}".'
			)
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
def parseCliArguments1() -> tuple[(argparse.Namespace, None), int]:
	rc: int = 0
	# noinspection PyBroadException
	try:
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv',
			description='Create a version-assigned and named ' +
						'Python virtual environment in "pyenv".'
		)
		# Add flag
		parser.add_argument(
			'-p', '--props',
			dest='props',
			action=argparse.BooleanOptionalAction,
			help='As project properties, add the files ' +
				 '`.python-version` and `.python-env` to CWD. Default: --no_props.'
		)
		# Add positional str argument
		parser.add_argument(
			'name',
			help='Short name of the new Python virtual environment.'
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
def parseCliArguments2() -> tuple[(argparse.Namespace, None), int]:
	rc: int = 0
	# noinspection PyBroadException
	try:
		parser = argparse.ArgumentParser(
# --- BEGIN CHANGE -----------------------------------------------------
			prog='pyenv virtualenv',
			description='Create a version-assigned and named ' +
						'Python virtual environment in "pyenv".'
		)
		# Add flag
		parser.add_argument(
			'-p', '--props',
			dest='props',
			action=argparse.BooleanOptionalAction,
			help='As project properties, add the files ' +
				 '`.python-version` and `.python-env` to CWD. Default: --no_props.'
		)
		# Add positional str argument
		parser.add_argument(
			'version',
			help='Python version, which must be already installed ' +
				 'in "pyenv".'
		)
		# Add positional str argument
		parser.add_argument(
			'name',
			help='Short name of the new Python virtual environment.'
		)
# --- END CHANGE -------------------------------------------------------
		return parser.parse_args(), rc
	except SystemExit:
		return None, 0
	except:
		log.error(sys.exc_info())
		return None, 1

## Display the version number and generating procedure for "pyenv-virtualenv" for Windows.
#
#  @return RC = 0 or another value in case of error
def displayDocumentation() -> int:
	# noinspection PyBroadException
	try:
		cmd = os.path.join(
			os.environ['PYENV_ROOT'],
			'plugins',
			'pyenv-virtualenv',
			'docs',
			'open_doxygen_docs.bat'
		)
		log.verbose(f'Execute: {cmd}')
		cp = subprocess.run(
			cmd,
			shell=True
		)
		rc = cp.returncode
		if rc != 0:
			log.error(f'Displaying Doxygen documentation failed (RC = {rc}.')
			log.info('Check/reinstall "pyenv-virtualenv". Then try again. ')
			log.notice('CANCELED.')
			rc = 130
	except:
		log.error(sys.exc_info())
		rc = 1
	return rc

## Display the version number and generating procedure for "pyenv-virtualenv" for Windows.
#
#  @return RC = 0 or another value in case of error
def displayVersionNumber() -> int:
	# noinspection PyBroadException
	try:
		file_path = os.path.join(
			os.environ['PYENV_ROOT'],
			'plugins',
			'pyenv-virtualenv',
			'.version'
		)
		if not os.path.isfile(file_path):
			log.error('Cannot display version number.')
			log.info(f'Reinstall the missing file "{file_path}".')
			log.notice('CANCELED.')
			return 130
		with open(file_path, 'r') as f:
			version = f.read().strip()
			# noinspection SpellCheckingInspection
			print(f'"\x1b[92mpyenv-virtualenv\x1b[0m" for Windows \x1b[96m{version}\x1b[0m (\x1b[93mpython -m venv\x1b[0m).')
		return 0
	except:
		log.error(sys.exc_info())
		return 1

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
			version_requested = False
			docs_requested = False
			for i in reversed(range(len(args_list))):
				arg = args_list[i]
				if arg in ['-h', '--help']:
					help_requested = True
					args_list.pop(i)
				elif arg in ['-v', '--version']:
					version_requested = True
					args_list.pop(i)
				elif arg in ['-d', '--docs']:
					docs_requested = True
					args_list.pop(i)
			# Calculate the count of positional arguments
			positional_count = len(args_list)
			if docs_requested:
				rc = displayDocumentation()
				break
			elif version_requested:
				rc = displayVersionNumber()
				break
			elif (
				help_requested
				or
				(positional_count not in [1, 2])
			):
				text = ("""
Usage: pyenv virtualenv [-h] [-v] [-p | --props | --no-props ] [version] [name]

Create a version-assigned and named Python virtual environment in "pyenv".

Positional arguments (which can be omitted):
  [version]             Python version, which must be already installed in 
                        "pyenv". Default: The global Python version.
  [name]                Short name of the new Python virtual environment.

Options:
  -h, --help            Show this help message and exit.
  -p, --props, --no-props
                        Add the files `.python-version` and `.python-env` 
                        as project properties to CWD. Default: --no_props.
  -v, --version         Display the version number of this "pyenv-virtualenv" 
                        release and ignore all other arguments.
						""").strip()
				print(text)
			elif positional_count == 1:
				# Case 1: single positional argument must be "Name"
				args, rc = parseCliArguments1()
			elif positional_count == 2:
				# Case 2: duo positional arguments must be "Version" and "Name"
				args, rc = parseCliArguments2()
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

