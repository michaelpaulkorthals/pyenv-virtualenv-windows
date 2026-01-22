# Windows PowerShell Script to write the 'pyenv.bat' 
# symbolic link to the patched version of that file.
#
# Dependencies:
# (None)
#
# © 2025 Michael Paul Korthals. All rights reserved.
# For legal details see documentation.
#
# 2025-07-31
#
# This script is located in the 'pyenv-virtualenv' plugin root directory.
#
# It will be called by 'install.bat' its parent folder.
#
# The script returns RC = 0 or another value in case of error.

$rc = 0
# Check if this script is running as 'Administrator'
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$as_admin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# Get/Check 'PYENV_ROOT' environment variable
try { 
	$pyenv_root = [System.Environment]::GetEnvironmentVariable('PYENV_ROOT').Trim() 
} catch {
	$rc = 1
	Write-Host "$([char]27)[91mERROR    Cannot find 'PYENV_ROOT' environment variable. 'pyenv' is missing (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Install and configure 'pyenv'. Then try again.$([char]27)[0m"
	exit $rc
}

# Read 'pyenv' version from file
try { 
	$pyenv_version = [IO.File]::ReadAllText("$pyenv_root..\.version").Trim() 
} catch {
	$rc = 1
	Write-Host "$([char]27)[91mERROR    Cannot read 'pyenv' version from file (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Install and configure 'pyenv'. Then try again.$([char]27)[0m"
	exit $rc
}

# Make symbolic link to patched 'pyenv.bat'
if ($as_admin) {
	$link_path = $pyenv_root + "plugins\pyenv-virtualenv\shims\pyenv.bat"
	$link_target = $pyenv_root + "plugins\pyenv-virtualenv\patch\pyenv_ptc_$pyenv_version.bat"
	Write-Host "$([char]27)[37mINFO     Writing symbolic link:$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO       * Path: '$link_path'.$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO       * Target: '$link_target'.$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     This could take some seconds ...$([char]27)[0m"
	try {
		New-Item -ItemType SymbolicLink -Path "$link_path" -Target "$link_target" | Out-Null
	} catch {
		$rc = 1
		Write-Host "$([char]27)[91mERROR    Unexpectedly cannot write symbolic link (RC = $rc).$([char]27)[0m"
		Write-Host "$([char]27)[37mINFO     Analyze/configure/repair the situation, why a script running as 'Administrator' fails. Then try again.$([char]27)[0m"
		exit $rc
	}
	Write-Host "$([char]27)[37mINFO     Done.$([char]27)[0m"
} else {
	$rc = 13
	Write-Host "$([char]27)[91mERROR    Insufficient privileges. (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     To create a symbolic link, you must call this script in a console terminal with 'Administrator' privileges. Then try again.$([char]27)[0m"
	exit $rc
}

# Return error level
exit $rc
 

# --- END OF CODE ------------------------------------------------------

