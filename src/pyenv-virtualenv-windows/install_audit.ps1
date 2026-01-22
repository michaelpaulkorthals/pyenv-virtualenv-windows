# Windows PowerShell Script to audit the 'Machine' PATH 
# and the 'User' PATH environment variable for path conflicts,
# which could jeopardize 'pyenv'-related Python calls.
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

if ($as_admin) {
	Write-Host "$([char]27)[92mSUCCESS  This script has been started with 'Administrator' privileges.$([char]27)[0m"
} else {
	Write-Host "$([char]27)[92mSUCCESS  This script has been started with 'User' privileges.$([char]27)[0m"
}

# Get/Check 'PYENV_ROOT' environment variable
try { 
	$pyenv_root = [System.Environment]::GetEnvironmentVariable('PYENV_ROOT').Trim() 
} catch {
	$rc = 1
	Write-Host "$([char]27)[91mERROR    Cannot find 'PYENV_ROOT' environment variable. 'pyenv' is missing (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Install and configure 'pyenv'. Then try again.$([char]27)[0m"
	exit $rc
}
Write-Host "$([char]27)[92mSUCCESS  'pyenv' is installed at: '$pyenv_root'$([char]27)[0m"

# Scan for 'pyenv' in 'Machine' PATH
$machine_paths = [System.Environment]::GetEnvironmentVariable('PATH', "Machine") -Split ";"
$found_machine_bin = ""
$found_machine_shims = ""
foreach ($item in $machine_paths) { 
	$item1 = $item.Trim()
	if ($item1 -ne "") {
		if ($item1 -eq ($pyenv_root + "bin")) {
			$found_machine_bin = $item1
		}
		if ($item1 -eq ($pyenv_root + "shims")) {
			$found_machine_shims = $item1
		}
	}
}
Write-Host "$([char]27)[37mINFO     'pyenv' 'bin' on 'Machine' PATH: '$found_machine_bin'$([char]27)[0m"
Write-Host "$([char]27)[37mINFO     'pyenv' 'shims' on 'Machine' PATH: '$found_machine_shims'$([char]27)[0m"

# Scan for 'pyenv' in 'User' PATH
$user_paths = [System.Environment]::GetEnvironmentVariable('PATH', "User") -Split ";"
$found_user_bin = ""
$found_user_shims = ""
foreach ($item in $user_paths) { 
	$item1 = $item.Trim()
	if ($item1 -ne "") {
		if ($item1 -eq ($pyenv_root + "bin")) {
			$found_user_bin = $item1
		}
		if ($item1 -eq ($pyenv_root + "shims")) {
			$found_user_shims = $item1
		}
	}
}
Write-Host "$([char]27)[37mINFO     'pyenv' 'bin' on 'User' PATH: '$found_user_bin'$([char]27)[0m"
Write-Host "$([char]27)[37mINFO     'pyenv' 'shims' on 'User' PATH: '$found_user_shims'$([char]27)[0m"

# Check if 'pyenv' is installed for 'All Users' or for 'This User Only'
if (($found_machine_bin -ne "") -and ($found_machine_shims -ne "") -and ($found_user_bin -eq "") -and ($found_user_shims -eq "")) {
	Write-Host "$([char]27)[92mSUCCESS  'pyenv' PATH items found in 'Machine' PATH for 'All Users'.$([char]27)[0m"
} elseif (($found_machine_bin -eq "") -and ($found_machine_shims -eq "") -and ($found_user_bin -ne "") -and ($found_user_shims -ne "")) {
	Write-Host "$([char]27)[92mSUCCESS  'pyenv' PATH items found in 'User' PATH for 'This User Only'.$([char]27)[0m"
} elseif (($found_machine_bin -eq "") -and ($found_machine_shims -eq "") -and ($found_user_bin -eq "") -and ($found_user_shims -eq "")) {
	# Not any 'pyenv' PATH item found
	$rc = 1
	Write-Host "$([char]27)[91mERROR    Cannot find 'pyenv' PATH items (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Install and configure 'pyenv'. Then try again.$([char]27)[0m"
	exit $rc
} else {
	# Otherwise, the 'pyenv' PATH definition is inconsistent
	$rc = 1
	Write-Host "$([char]27)[91mERROR    Inconsistent 'pyenv' PATH definition detected (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[95mNOTICE   Read the unit 'Path Conflicts' in the documentation to get help.$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Repair the inconsistent 'pyenv' PATH definitions manually. Then try again.$([char]27)[0m"
	exit $rc
}

# Try to find 'pyenv' Python executable without calling Python
Write-Host "$([char]27)[37mINFO     Trying to find 'pyenv' Python executable by command 'where.exe python':$([char]27)[0m"
where.exe python | Tee-Object -Variable output
$output_lines = $output -Split "\r\n"
$conflicts = @()
$found_python = ""
foreach ($line in $output_lines) {
	$line1 = $line.Trim()
	if ($line.StartsWith($pyenv_root)) {
		# Detect 'pyenv' Python executable
		$found_python = $line1
		break
	} else {
		# Detect a conflict with another global Python executable,
		# which have a higher PATH priority then 'Pyenv'.
		$conflicts += @(, $line1)
	}
}
if ($found_python -eq "") {
	Write-Host "$([char]27)[91mERROR    Unexpectedly cannot find Python executable.$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Install/repair/configure 'pyenv'. Then try again.$([char]27)[0m"
} else {
	if ($conflicts.count -eq 0) {
		Write-Host "$([char]27)[92mSUCCESS  Python executable found at '$found_python' (RC = $rc).$([char]27)[0m"
	} else {
		$rc = 1
		Write-Host "$([char]27)[91mERROR    Found path conflicts (RC = $rc):$([char]27)[0m"
		foreach ($conflict in $conflicts) {
			Write-Host "$([char]27)[91mERROR      * '$conflict'.$([char]27)[0m"
		}
		Write-Host "$([char]27)[95mNOTICE   It is your decision, how to manage your PATH. This program cannot do this for you.$([char]27)[0m"
		Write-Host "$([char]27)[95mNOTICE   To get help, completely read the unit 'Path Conflicts' in the documentation.$([char]27)[0m"
		Write-Host "$([char]27)[37mINFO     Resolve the conflicts adopting the PATH on 'Machine' and 'User' according to your needs. Then try again.$([char]27)[0m"
		exit $rc
	}
}

# Return error level
exit 0


# --- END OF CODE ------------------------------------------------------

