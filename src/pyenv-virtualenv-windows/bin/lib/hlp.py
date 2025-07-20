##
#  @package hlp
#  @file hlp.py
#  @author Michael Paul Korthals
#  @date 2025-07-10
#  @version 1.0.0
#  @copyright © 2025 Michael Paul Korthals. All rights reserved.
#  See License details in the documentation.
#
#  Application-specific Helper Library to deliver complex program
#  features as single function calls for all "pyenv-virtualenv"
#  utilities.
#

# --- IMPORTS ----------------------------------------------------------

# Python
import glob
import os
import platform
import re
import sys

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
try:
	# noinspection PyUnresolvedReferences
	import lib.tbl as tbl
except ImportError():
	try:
		# noinspection PyUnresolvedReferences
		import tbl
	except ImportError():
		# noinspection PyUnresolvedReferences
		import tbl
try:
	# noinspection PyUnresolvedReferences
	import lib.tre as tre
except ImportError():
	try:
		# noinspection PyUnresolvedReferences
		import tre
	except ImportError():
		# noinspection PyUnresolvedReferences
		import tre


# --- HELPER -----------------------------------------------------------

## Convert a natural name into stripped functional name, without spaces,
# which is lowercase, is file name safe and is technical safe.
# NOTE: The resulting name is file name safe and also excludes all kind of
# technical used characters, including those to insert variables or HTML tags.
# By this pattern excluded characters are replaced by underscore "_".
#
#  @param natural_name Natural name to convert.
#  @return Safe functional name.
#  @see https://www.regextester.com/
def fName(natural_name: str) -> str:
	return re.sub(
		r"[/\\?$%#+\-*:|\"'<>()\[\]{}\x7F\x00-\x20]",
		"_", natural_name.strip()
	).casefold().strip('_')

## Check if the program in running on the required platform.
#  NOTE: Due the program is possibly started
#  in an outdated Python 3 version, it is not permitted
#  to use the library "log" inside this function.
#  So, the "print" output must be manually leveled and colorized.
#
#  @param name Required platform name.
#  @return RC = 0 or other values in case of error.
def auditPlatform(name: str) -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		while True:
			verbose = (
					('LOG_LEVEL' in os.environ)
					and
					(int(os.environ['LOG_LEVEL']) <= 15)
			)
			if verbose: print(
				f'\x1b[94mVERBOSE  1) Auditing platform is "%s" ...\x1b[0m' % name,
				flush=True
			)
			if not platform.system() == name:
				print(
					'\x1b[91mERROR    Platform "%s" is not supported to execute this program.\x1b[0m' % platform.system(),
					flush=True
				)
				print(
					'\x1b[95mNOTICE   Run this program on "%s" only\x1b[0m' % name,
					flush=True
				)
				rc = 1
				break
			if verbose: print(
				'\x1b[94mVERBOSE  No deviation detected at observation 1.\x1b[0m',
				flush=True
			)
			if verbose: print(
				'\x1b[94mVERBOSE  Audit result: Zero deviations.\x1b[0m',
				flush=True
			)
			# Go on
			break
		# End while
		if rc != 0:
			print(
				'\x1b[91mERROR    Cancelling program.\x1b[0m',
				flush=True
			)
			print(
				'\x1b[37mINFO     See detected deviation and remediation proposals/instructions above.\x1b[0m',
				flush=True
			)
		# End if
	except Exception as exc:
		print(
			'\x1b[91mERROR    Unexpected error "%s".\x1b[0m' % str(exc),
			flush=True
		)
		rc = 1
	return rc

## Check if Python version is greater or equal
#  the given minimal version.
#  NOTE: Due the program is possibly started
#  in an outdated Python 3 version, it is not permitted
#  to use the library "log" inside this function.
#  So, the "print" output must be manually leveled and colorized.
#
#  @param min_ver Minimal permitted version in max. 3 numbers separated by dot (e.g. "3",  "3.6", "3.6.5", etc.).
#  @return RC = 0 or other values in case of error.
def auditGlobalPythonVersion(min_ver: str) -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		while True:
			verbose = (
				('LOG_LEVEL' in os.environ)
				and
				(int(os.environ['LOG_LEVEL']) <= 15)
			)
			if verbose: print(
				f'\x1b[94mVERBOSE  1) Auditing global Python version is %s+ ...\x1b[0m' % min_ver,
				flush=True
			)
			tup_cur = tuple(map(int, platform.python_version_tuple()))
			tup_min = tuple(map(int, tuple(min_ver.split('.'))))
			if tup_cur < tup_min:
				print(
					'\x1b[91mERROR    Using outdated "Python %s".\x1b[0m' % (
						platform.python_version()
					),
					flush=True
				)
				print(
					'\x1b[95mNOTICE   Install "Python %s+" into "pyenv". Then try again.\x1b[0m' % (
						platform.python_version()
					),
					flush=True
				)
				rc = 1
				break
			if verbose: print(
				'\x1b[94mVERBOSE  No deviation detected at observation 1.\x1b[0m',
				flush=True
			)
			if verbose: print(
				'\x1b[94mVERBOSE  Audit result: Zero deviations.\x1b[0m',
				flush=True
			)
			# Go on
			break
		# End while
		if rc != 0:
			print(
				'\x1b[91mERROR    Cancelling program.\x1b[0m',
				flush=True
			)
			print(
				'\x1b[95mNOTICE   See detected deviation and remediation proposals/instructions above.\x1b[0m',
				flush=True
			)
		# End if
	except Exception as exc:
		print(
			'\x1b[91mERROR    Unexpected error "%s".\x1b[0m' % str(exc),
				flush=True
		)
		rc = 1
	return rc

## Check if "pyenv" version is greater or equal
# the given minimal version.
#
#  @param min_ver Minimal permitted version in max. 3 numbers separated by dot (e.g. "3",  "3.6", "3.6.5", etc.).
#  @return RC = 0 or other values in case of error.
def auditPyEnv(min_ver: str) -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		while True:
			log.verbose(f'1) Auditing pyenv and path environment variables are correctly set ...')
			key = 'PYENV_ROOT'
			if not (key in os.environ):
				log.error(f'Cannot find environment variable "{key}".')
				log.notice(
					'Check/install/repair "pyenv". See: "%USERPROFILE%.pyenv". Then try again.'
				)
				rc = 2
				break
			key = 'PATH'
			if not (key in os.environ):
				log.error(f'Cannot find environment variable "{key}".')
				log.notice(
					'Check/restart the terminal shell. Then try again. If this doses not help further on, reboot your computer.'
				)
				rc =  2
				break
			path = os.environ['PATH'].strip()
			if len(path) == 0:
				log.error(f'The PATH environment variable is empty.')
				log.notice(
					'Check/restart the terminal shell. Then try again. If this doses not help further on, reboot your computer.'
				)
				rc =  2
				break
			log.verbose('No deviation detected at observation 1.')
			log.verbose(f'2) Auditing "pyenv" version is {min_ver}+ ...')
			current_version = getPyEnvVersion()
			if len(current_version) == 0:
				log.error('Cannot determine the "pyenv" version.')
				log.notice('Install/configure "pyenv". Then try again.')
				rc = 1
				break
			tup_cur = tuple(map(int, tuple(current_version.split('.'))))
			tup_min = tuple(map(int, tuple(min_ver.split('.'))))
			if tup_cur < tup_min:
				log.error(f'"pyenv {current_version}" is not supported.')
				log.notice(f'Install/configure "pyenv {min_ver}+". Then try again.')
				rc = 1
				break
			log.verbose('No deviation detected at observation 2.')
			log.verbose(f'3) Auditing "pyenv" Python versions are virtual environment capable ...')
			pyenv_root_dir = os.environ['PYENV_ROOT']
			if not os.path.isdir(pyenv_root_dir):
				log.error(
					f'Cannot find "pyenv" root directory "{pyenv_root_dir}".'
				)
				log.info(
					'Check/install/repair "pyenv". See: "%USERPROFILE%.pyenv".'
				)
				rc = 1
				break
			log.verbose('No deviation detected at observation 3.')
			log.verbose('4) Auditing "pyenv" has virtual environment-capable Python versions ...')
			# Determine Python version, which is capable
			# to install Python virtual environment.
			versions_dir = os.path.join(
				os.environ['PYENV_ROOT'],
				'versions'
			)
			if not os.path.isdir(versions_dir):
				log.error('Cannot find any Python version in "pyenv".')
				log.notice('Install a Python version 3.3+ into "pyenv".')
				rc = 1
				break
			vers = getPythonVersions(
				version='*',
				venv_capable=True,
				as_paths = True
			)
			if len(vers) == 0:
				log.error(
					'Cannot find a virtual environment capable version in "pyenv".'
				)
				log.notice('Install a Python version 3.3+ into "pyenv".')
				rc = 1
				break
			log.verbose('No deviation detected at observation 4.')
			log.verbose('Audit result: Zero deviations.')
			# Go on
			break
		# End while
		if rc != 0:
			log.error(
				f'Cancelling program.'
			)
			log.info(
				f'See deviating error messages and remediation proposals/instructions above.'
			)
	except:
		log.error(sys.exc_info())
		rc = 1
	return rc

## Get "pyenv" version.
#
#  @return Version number or empty string in case of error.
def getPyEnvVersion() -> str:
	file_path = os.path.abspath(
		os.path.join(os.environ['PYENV_ROOT'], '..', '.version')
	)
	if not os.path.isfile(file_path):
		return ''
	ver = ''
	with open(file_path, 'r') as f:
		ver = f.read().strip()
	return ver

## Get selected global/local Python version in "pyenv".
#
#  @return Tuple of:
#    * Version number or empty string in case of non-selected or error.
#    * Realm name, which delivers the Python version as element of {"local", "global"}.
def getPythonVersion() -> (str, str):
	# Primary: Find local Python version in local project properties
	realm = "local"
	ver_path = scanCwdAndAncestorsForFile('.python-version')
	if len(ver_path) > 0:
		with open(ver_path, 'r') as f:
			ver = f.read().strip()
		return ver, realm
	# Secondary: Find global Python version in "pyenv"
	realm = "global"
	ver_path = os.path.join(os.environ['PYENV_ROOT'], 'version')
	if not os.path.isfile(ver_path):
		return '', ''
	ver = ''
	with open(ver_path, 'r') as f:
		ver = f.read().strip()
	return ver, realm

## Scan the CWD and its path ancestors for a specific file.
#
#  @param file_name Name of the file to find.
#  @return Path to found file or empty string in case of not found.
def scanCwdAndAncestorsForFile(file_name: str) -> str:
	dir_path: str = os.getcwd()
	while True:
		# Check if file is there
		file_path = os.path.join(dir_path, file_name)
		if os.path.isfile(file_path):
			# Found path
			return file_path
		# Check if finished
		if len(dir_path) <= 3:
			# Not found path
			break
		# Next path ancestor
		dir_path = os.path.dirname(dir_path)
	# End while
	return ''

## Get the "*" marker for this version,
#  if it is the globally selected version in "pyenv".
#
#  @param ver Version to check as directory path or version string.
#  @return A star ("*") or empty string in any other case.
def getGlobalStar(ver: str) -> str:
	ver1 = ver.strip()
	if os.path.isdir(ver1):
		ver2 = os.path.basename(ver1)
	else:
		ver2 = ver1
	ver, realm = getPythonVersion()
	if ver2 == ver:
		return '*'
	else:
		return ''

## Check if the Python version is capable to run virtual environment.
#
#  @param ver Python version string or path to Python version folder to check.
#  @return Flag to state if the version is capable
#  to run virtual environment.
#  It is False in case of error.
def isPythonVenvVersion(ver: str) -> bool:
	# noinspection PyBroadException
	try:
		if os.path.isdir(ver):
			ver1 = os.path.basename(ver)
		else:
			ver1 = ver
		ver2 = re.search(r'\s*([\d.]+)', ver1).group(1)
		if ver2 != ver1:
			return False
		lst = ver2.split('.')
		while len(lst) < 2:
			lst.append('0')
		maj, mno, _ = tuple(lst)
		maj = int(maj)
		mno = int(mno)
		return (
			(maj > 3)
			or
			(
				(maj == 3)
				and
				(mno >= 3)
			)
		)
	except:
		log.error(sys.exc_info())
		return False

## Find the best version, matching the requirements.
#  Select best Python version directory.
#
#  @param ver Number of required version.
#  @param realm Name of the realm, which sources the version number.
#  @param venv_capable Flag to filter for venv-capable versions only. Default: False = no restrictions.
#  @return Tuple of:
#    * Matched Python version directory or None in case of error.
#    * RC = 0 or other values in case of error.
def selectVersionDir(
	ver: str,
	realm: str,
	venv_capable=False
) -> tuple[(str, None), int]:
	# noinspection PyBroadException
	try:
		# Load all versions
		dirs: list[str] = getPythonVersions(
			'*',
			venv_capable=venv_capable,
			as_paths=True
		)
		# Parse required version
		ver1 = re.search(r'\s*([\d.]+)', ver).group(1)
		if ver1 != ver:
			log.error(f'Version number "{ver}" is not matching itself (match = "{ver1}".')
			log.info(f'Check/correct the version sourced from "({realm})". Then try again.')
			return None, 1
		tup1 = tuple(ver1.split('.'))
		# Pass 1: Filter all versions starting with that version
		lst = []
		log.verbose('Filtering Python versions ...')
		for dir1 in dirs:
			log.debug(f'Filtered version: {dir1}')
			ver2 = os.path.basename(dir1)
			tup2 = tuple(ver2.split('.'))
			if tup2[:len(tup1)] == tup1:  # Starting with short version
				lst.append(tup2)
		# Pass 2: From result of pass 1 filter maximum version
		if len(lst) > 0:
			max_tup = max(lst)
			max_nam = '.'.join(list(max_tup))
			for dir2 in dirs:
				if os.path.basename(dir2) == max_nam:
					log.verbose(f'Selected version: {dir2}')
					return dir2, 0
			# End for
		# End if
		log.error(f'Cannot find a Python version, which matches "{ver1}".')
		log.info('Calling "pyenv virtualenvs", ensure that the wanted version is installed. Then try again.')
		return None, 2
	except:
		log.error(sys.exc_info())
		return None, 1

## Get the colored virtual environment capability str for the specific version number or path.
#
#  @param ver Python version number or path to observe.

def getColoredVenvCapability(ver: str) -> str:
	if isPythonVenvVersion(ver):
		return '\x1b[92mTrue\x1b[0m'
	else:
		return'\x1b[93mFalse\x1b[0m'

## Get list of installed Python version directories in "pyenv".
#
#  @param version Exact or wildcard version name.
#  Default: '*' = all.
#  @param venv_capable Flag to filter for venv-capable versions only.
#  Default: False = no restrictions.
#  @param as_paths Flag to permit output as paths.
#  Default: False = output as names.
#  @return List of Python version directory paths.
def getPythonVersions(
		version: str='*',
		venv_capable: bool=False,
		as_paths: bool=False
) -> list[str]:
	result = []
	vers_path = os.path.join(
		os.environ['PYENV_ROOT'],
		'versions',
	)
	vers = glob.glob(os.path.join(vers_path, version))
	if len(vers) > 0:
		for ver in vers:
			if (not venv_capable) or (isPythonVenvVersion(ver)):
				exe_path = os.path.join(ver, 'python.exe')
				cfg_path = os.path.join(ver, 'pyvenv.cfg')
				if (
					(os.path.isfile(exe_path))
					and
					(not os.path.isfile(cfg_path))
				):
					if as_paths:
						item = ver
					else:
						item = os.path.basename(ver)
					result.append(item)
		if len(result) >= 2:
			# Sort resulting versions paths in descending order.
			# NOTE: For a small data amount, the simple 'loop sort' algorythm is sufficient and easy to code.
			for i1 in range(len(result)):
				p1: str = result[i1]
				v1: list = os.path.basename(p1).split('.')
				t1: tuple = tuple(map(int, v1))
				for i2 in range(i1 + 1, len(result)):
					p2: str = result[i2]
					v2: list = os.path.basename(p2).split('.')
					t2: tuple = tuple(map(int, v2))
					if t2 > t1:  # Descending order
						# Exchange version paths
						m: str = f'{result[i1]}' # Clone
						result[i1] = result[i2]
						result[i2] = m
					# End if
				# End for
			# End for
		# End if
	return result

## Check if path is a junction, which has been created
#  e.g. using the "mklink /J" command in Windows.
#
#  @param path The path to the possible junction.
#  @return Flag, which states that the path is a junction.
#  @see https://stackoverflow.com/questions/47469836/how-to-tell-if-a-directory-is-a-windows-junction-in-python
def isJunction(path: str) -> bool:
	try:
		return bool(os.readlink(path))
	except OSError:
		return False

## Scan the Pythons versions in "pyenv" for junctions,
#  which points to a specific virtual environment directory path.
#
#  @param path Specific virtual environment directory path.
#  @return List of paths to junctions.
def getEnvJunctions(path: str) -> list[str]:
	# noinspection PyBroadException
	try:
		result = []
		version_dir = os.path.join(
			os.environ['PYENV_ROOT'],
			'versions'
		)
		vers = glob.glob(os.path.join(
			version_dir,
			'*'
		))
		for ver in vers:
			if isJunction(ver):
				# Get link value
				link = os.readlink(ver)
				# Strip Windows-specific link prefix if exists
				pref = f'{os.sep}{os.sep}?{os.sep}'
				if link.startswith(pref):
					link = link.removeprefix(pref)
				# Compare
				if link == path:
					# Append to result
					result.append(ver)
		return result
	except:
		log.error(sys.exc_info())
		return []

## Get the content of project property file.
#
# @param file_path Path to project property file.
# @return Text, which the file is containing or empty string in case of error.
def getProjectPropertyFileStr(file_path: str) -> str:
	result = ''
	# noinspection PyBroadException
	try:
		with open(file_path, 'r') as f:
			result = f.read().strip()
		return result
	except:
		log.error(sys.exc_info())
		return ''

## Set/override project property files.
#  NOTE: The files are written into CWD.
#
#  @param ver Python version number.
#  @param env Name of Python virtual environment under that version in "pyenv".
#  @return RC = 0 or other values in case of error.
def setProjectProperties(ver: str, env: str) -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		while True:
			log.verbose(
				'Configuring project properties ...'
			)
			# Determine the project property file paths in CWD
			ver_prop_path = os.path.join(
				os.getcwd(),
				'.python-version'
			)
			env_prop_path = os.path.join(
				os.getcwd(),
				'.python-env'
			)
			# --- VERSION ----------------------------------------------
			# Check/correct version string
			ver1 = re.search(r'\s*([\d.]+)', ver.strip()).group(1)
			if ver1 != ver:
				log.notice(f'Automatically corrected version from "{ver}" to "{ver1}".')
			# Check if Python version is installed
			ver_path = os.path.join(
				os.environ['PYENV_ROOT'],
				'versions',
				ver1
			)
			exe_path = os.path.join(
				ver_path,
				'python.exe'
			)
			if not (
				os.path.isdir(ver_path)
				and
				os.path.isfile(exe_path)
			):
				log.error(
					f'"Python "{ver1}" is not installed in "pyenv".'
				)
				log.info(
					'Select version from {}.'.format(
						getPythonVersions(
							version='*',
							venv_capable=True,
							as_paths=False
						)
					)
				)
				rc = 2
				break
			# Write Python version property file
			with open(ver_prop_path, 'w') as ver_f:
				ver_f.write(ver1)
			# --- VIRTUAL ENVIRONMENT ----------------------------------
			# Check/correct "env" string
			env1 = fName(env)
			if env1 != env:
				log.notice(f'Automatically corrected name from "{env}" to "{env1}".')
			# Check if virtual environment exists under that version
			env_path = os.path.join(
				os.environ['PYENV_ROOT'],
				'versions',
				ver1,
				'envs',
				env1
			)
			exe_path = os.path.join(
				env_path,
				'Scripts',
				'python.exe'
			)
			if not (
				os.path.isdir(env_path)
				and
				os.path.isfile(exe_path)
			):
				log.error(f'"Python {ver1}" has no virtual environment "{env1}" in "pyenv".')
				log.info(f'Select version from {getEnvs(ver1)}')
				rc = 2
				break
			# Write virtual environment property file
			with open(env_prop_path, 'w') as ver_f:
				ver_f.write(env1)
			# Go on
			break
		# End while
	except:
		log.error(sys.exc_info())
		rc = 1
	return rc

## Get list of installed virtual environments
#  for a specific Python version in "pyenv".
#  Output as names or paths.
#
#  @param ver Number of required Python version as str
#  or path to Python version.
#  @param name Virtual environment name as str or wildcard str.
#  Default: '*' = all.
#  @param as_paths Flag to permit output as paths.
#  Default: False = output as names.
#  @return List of virtual environment names or paths.
def getEnvs(
	ver: str,
	name: str = '*',
	as_paths: bool=False
) -> list[str]:
	result: list[str] = []
	if os.path.isdir(ver):
		envs_path = os.path.join(
			ver,
			'envs'
		)
	else:
		envs_path = os.path.join(
			os.environ['PYENV_ROOT'],
			'versions',
			ver,
			'envs'
		)
	envs = glob.glob(os.path.join(envs_path, name))
	if len(envs) > 0:
		for env in envs:
			cfg_path = os.path.join(
				env,
				'pyvenv.cfg'
			)
			exe_path = os.path.join(
				env,
				'Scripts',
				'python.exe'
			)
			if (
				(os.path.isfile(cfg_path))
				and
				(os.path.isfile(exe_path))
			):
				if as_paths:
					item = env
				else:
					item = os.path.basename(env)
				result.append(item)
	return result

## Get list of installed virtual environments
#  for a specific Python version in "pyenv".
#  Output as names or paths.
#
#  @param name Virtual environment name as str or wildcard str.
#  Default: '*' = all.
#  @param as_paths Flag to permit output as paths.
#  Default: False = output as names.
#  @return List of virtual environment names or paths.
def getAllEnvs(
	name: str = '*',
	as_paths: bool=False
) -> list[str]:
	result: list[str] = []
	vers = getPythonVersions(
		venv_capable=True,
		as_paths=True
	)
	for ver in vers:
		if os.path.isdir(ver):
			envs_path = os.path.join(
				ver,
				'envs'
			)
		else:
			envs_path = os.path.join(
				os.environ['PYENV_ROOT'],
				'versions',
				ver,
				'envs'
			)
		envs = glob.glob(os.path.join(envs_path, name))
		if len(envs) > 0:
			for env in envs:
				cfg_path = os.path.join(
					env,
					'pyvenv.cfg'
				)
				exe_path = os.path.join(
					env,
					'Scripts',
					'python.exe'
				)
				if (
					(os.path.isfile(cfg_path))
					and
					(os.path.isfile(exe_path))
				):
					if as_paths:
						item = env
					else:
						item = os.path.basename(env)
					result.append(item)
	return result

## Parse virtual environment directory path.
#
#  @param env_dir Path to version-based virtual environment directory
#  in "pyenv".
#  @return Tuple of:
#    * Python version string
#    * Virtual environment name.
#    * Path to virtual environment directory beginning with "%USERPROFILE%".
def parseEnvDir(env_dir: str) -> tuple[str, str, str]:
	items: list[str] = os.path.abspath(env_dir).split(os.sep)
	version = items[6]
	name = items[8]
	items1 = ['%USERPROFILE%'] + items[3:]
	path = os.sep.join(items1)
	return version, name, path

## Set project property files.
#  NOTE: The files will be removed from CWD.
#
#  @return RC = 0 or other values in case of error.
def unsetProjectProperties() -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		log.verbose(
			'Configuring project properties ...'
		)
		ver_path = os.path.join(
			os.getcwd(),
			'.python-version'
		)
		env_path = os.path.join(
			os.getcwd(),
			'.python-env'
		)
		if os.path.isfile(ver_path):
			os.remove(ver_path)
		else:
			log.warning(f'Cannot find "{ver_path}".')
		if os.path.isfile(env_path):
			os.remove(env_path)
		else:
			log.warning(f'Cannot find "{env_path}".')
	except:
		log.error(sys.exc_info())
		rc = 1
	return rc

## Display the table, which shows a list about project properties.
#  NOTE: The project property files are located in the project folder
#  with the application executable/script. Change directory to that
#  location before you use a feature, which outputs the project
#  properties.
#
#  @return RC = 0 or other values in case of error.
def listProjectProperties() -> int:
	rc: int = 0
	# noinspection PyBroadException
	try:
		# List project properties in folder tree
		log.verbose(
			'Listing project properties ...'
		)
		up = os.environ['USERPROFILE']
		# Pass 1: Generate list of project properties.
		# 1. Version property
		fnv = '.python-version'
		fpv = scanCwdAndAncestorsForFile(fnv)
		log.debug(f'Version file path: "{fpv}".')
		dtv = ''
		if os.path.isfile(fpv):
			fnv = fpv
			if fnv.startswith(up):
				fnv = '%USERPROFILE%' + fnv[len(up):]
			with open(fpv, 'r') as f:
				dtv = f.read().strip()
				log.debug(f'Version: "{dtv}".')
		else:
			fnv = ''
		prv = f'({dtv})'
		acv = ' '
		if (
			('PROMPT' in os.environ)
			and
			(prv in os.environ['PROMPT'])
		):
			acv = '*'
		# 2. Name property
		fnn = '.python-env'
		fpn = scanCwdAndAncestorsForFile(fnn)
		log.debug(f'Name file path: "{fpn}".')
		dtn = ''
		if os.path.isfile(fpn):
			fnn = fpn
			if fnn.startswith(up):
				fnn = '%USERPROFILE%' + fnn[len(up):]
			with open(fpn, 'r') as f:
				dtn = f.read().strip()
				log.debug(f'Name: "{dtn}".')
		else:
			fnn = ''
		prn = f'({dtn})'
		acn = ' '
		if (
				('PROMPT' in os.environ)
				and
				(prn in os.environ['PROMPT'])
		):
			acn = '*'
		# 3. TreeFolders to exclude property
		fne = '.tree-excludes'
		fpe = scanCwdAndAncestorsForFile(fne)
		log.debug(f'Excludes file path: "{fpe}".')
		dte = ''
		if os.path.isfile(fpe):
			fne = fpe
			if fne.startswith(up):
				fne = '%USERPROFILE%' + fne[len(up):]
			with open(fpe, 'r') as f:
				dte = f.read().strip()
				log.debug(f'Excludes: {dte}.')
			ace = '*'
		else:
			fne = ''
			ace = ' '
		# Generate data
		# noinspection SpellCheckingInspection
		data = [
			[tbl.HEADER, 'A', 'Property Path', 'ID', '"pyenv" Location/Content'],
			[tbl.SEPARATOR]
		]
		dtv_dir =  os.path.join(
			os.environ['PYENV_ROOT'],
			'versions',
			dtv
		)
		if os.path.isdir(dtv_dir):
			data.append([
				tbl.DATA,
				acv,
				fnv,
				f'\x1b[96m{dtv}\x1b[0m',
				dtv_dir
			])
		dtn_dir = os.path.join(
			os.environ['PYENV_ROOT'],
			'versions',
			dtv,
			'envs',
			dtn
		)
		if os.path.isdir(dtn_dir):
			data.append([
				tbl.DATA,
				acn,
				fnn,
				f'\x1b[93m{dtn}\x1b[0m',
				dtn_dir
			])
		if len(dte) > 0:
			data.append([
				tbl.DATA,
				ace,
				fne,
				'\x1b[95m:tuple\x1b[0m',
				dte
			])
		data.append([tbl.SEPARATOR])
		# Pass 2: Output list of project properties.
		table = tbl.SimpleTable(
			data,
			headline='LOCAL PROJECT PROPERTIES (A = active):'
		)
		table.run()
		# Pass 3: Output CWD files and folder tree
		log.verbose(
			'Listing project properties in files and folders tree ...'
		)
		print('\nLOCAL FOLDER TREE:\n')
		tre.tree(
			os.getcwd(),
			exclude=(getTreeFoldersToExclude())
		)
	except:
		log.error(sys.exc_info())
		rc = 1
	return rc

## Get the directory tree folder names to exclude from project property file ".tree-excludes".
#
#  @return Tuple of folder names to exclude or empty tuple in case of not found or error.
def getTreeFoldersToExclude() -> (tuple, tuple[str]):
	result: tuple = ()
	# noinspection PyBroadException
	try:
		file_path = scanCwdAndAncestorsForFile('.tree-excludes')
		if file_path == '':
			return result
		with open(file_path, 'r') as f:
			result_str = f.read().strip()
			# noinspection PyBroadException
			try:
				result: (tuple, tuple[str]) = eval(result_str)
				if not isinstance(result, (tuple, tuple[str])):
					raise TypeError()
			except:
				log.error(f'Content of file "{file_path}", "{result_str}" cannot be interpreted as "empty tuple" or "tuple of str".')
				log.info('Check/repair this file. Content example: "(\'docs\', \'.idea\', \'__pycache__\')".')
	except:
		log.error(sys.exc_info())
	return result


# --- END OF CODE ------------------------------------------------------

