# Windows PowerShell Script to write the PATH item for 
# 'pyenv-virtualenv' for Windows.
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
# Silently check if this script is running as 'Administrator'
$currentPrincipal = New-Object Security.Principal.WindowsPrincipal([Security.Principal.WindowsIdentity]::GetCurrent())
$as_admin = $currentPrincipal.IsInRole([Security.Principal.WindowsBuiltInRole]::Administrator)

# Silently Get/Check 'PYENV_ROOT' environment variable
try { 
	$pyenv_root = [System.Environment]::GetEnvironmentVariable('PYENV_ROOT').Trim() 
} catch {
	$rc = 1
	Write-Host "$([char]27)[91mERROR    Cannot find 'PYENV_ROOT' environment variable. 'pyenv' is missing (RC = $rc).$([char]27)[0m"
	Write-Host "$([char]27)[37mINFO     Install and configure 'pyenv'. Then try again.$([char]27)[0m"
	exit $rc
}

# Silently scan for 'pyenv' and 'pyenv-virtualenv' in 'Machine' PATH
$machine_paths = [System.Environment]::GetEnvironmentVariable('PATH', "Machine") -Split ";"
$found_machine_bin = ""
$found_machine_shims = ""
$found_machine_plugin_shims = ""
$index_machine_bin = -1
$index_machine_shims = -1
$index_machine_plugin_shims = -1
$i = -1
foreach ($item in $machine_paths) { 
	$i += 1
	$item1 = $item.Trim()
	if ($item1 -ne "") {
		if ($item1 -eq ($pyenv_root + "bin")) {
			$found_machine_bin = $item1
			$index_machine_bin = $i
		}
		if ($item1 -eq ($pyenv_root + "shims")) {
			$found_machine_shims = $item1
			$index_machine_shims = $i
		}
		if ($item1 -eq ($pyenv_root + "plugins\pyenv-virtualenv\shims")) {
			$found_machine_plugin_shims = $item1
			$index_machine_plugin_shims = $i
		}
	}
}

# Silently scan for 'pyenv' and 'pyenv-virtualenv' in 'User' PATH
$user_paths = [System.Environment]::GetEnvironmentVariable('PATH', "User") -Split ";"
$found_user_bin = ""
$found_user_shims = ""
$found_user_plugin_shims = ""
$index_user_bin = -1
$index_user_shims = -1
$index_user_plugin_shims = -1
$i = -1
foreach ($item in $user_paths) { 
	$i += 1
	$item1 = $item.Trim()
	if ($item1 -ne "") {
		if ($item1 -eq ($pyenv_root + "bin")) {
			$found_user_bin = $item1
			$index_user_bin = $i
		}
		if ($item1 -eq ($pyenv_root + "shims")) {
			$found_user_shims = $item1
			$index_user_shims = $i
		}
		if ($item1 -eq ($pyenv_root + "plugins\pyenv-virtualenv\shims")) {
			$found_user_plugin_shims = $item1
			$index_user_plugin_shims = $i
		}
	}
}

# Check if 'pyenv' is installed for 'All Users' or for 'This User Only'
if (($found_machine_bin -ne "") -and ($found_machine_shims -ne "") -and ($found_user_bin -eq "") -and ($found_user_shims -eq "")) {
	# 'pyenv' PATH items found in 'Machine' PATH for 'All Users'
	if ($found_machine_plugin_shims -eq "") {
		if ($as_admin) {
			$new_machine_path = $pyenv_root + "plugins\pyenv-virtualenv\shims"
			foreach ($item in $machine_paths) {
				$new_machine_path += ";" + $item
			}
			try {
				Write-Host "$([char]27)[37mINFO     Writing registry. This could take some seconds ...$([char]27)[0m"
				[System.Environment]::SetEnvironmentVariable('PATH', $new_machine_path, "Machine")
			} catch {
				$rc = 1
				Write-Host "$([char]27)[91mERROR    Cannot write 'Machine' PATH environment variable. (RC = $rc).$([char]27)[0m"
				Write-Host "$([char]27)[95mNOTICE   Read the unit 'Path Conflicts' in the documentation to get help.$([char]27)[0m"
				Write-Host "$([char]27)[37mINFO     Repair the inconsistent 'pyenv' PATH definitions manually. Then try again.$([char]27)[0m"
				exit $rc
			}
			# 'pyenv-virtualenv' PATH item has been correctly written
			Write-Host "$([char]27)[92mSUCCESS  'pyenv-virtualenv' 'Machine' PATH item is now in place. (RC = $rc).$([char]27)[0m"
			Write-Host "$([char]27)[95mNOTICE   Close and reopen the console terminal to let this change take effect.$([char]27)[0m"
		} else {
			$rc = 13
			Write-Host "$([char]27)[91mERROR    Insufficient privileges. (RC = $rc).$([char]27)[0m"
			Write-Host "$([char]27)[37mINFO     Changing the 'Machine PATH' you should call this script in a console terminal with 'Administrator' privileges. Then try again.$([char]27)[0m"
			Write-Host "$([char]27)[95mNOTICE   Alternatively read the unit 'Path Conflicts'. Resolve/repair manually. Then try again.$([char]27)[0m"
			exit $rc
		}
	} else {
		if (($index_machine_plugin_shims -lt $index_machine_bin) -and ($index_machine_plugin_shims -lt $index_machine_shims)) {
			# 'pyenv-virtualenv' PATH item is already set in place
			Write-Host "$([char]27)[92mSUCCESS  'pyenv-virtualenv' 'shims' on 'Machine' PATH is already in place: '$found_machine_plugin_shims' (RC = $rc).$([char]27)[0m"
		} else {
			# 'pyenv-virtualenv' item in 'Machine' PATH
			# has a lower priority than 'pyenv'.
			$rc = 1
			Write-Host "$([char]27)[91mERROR    'pyenv-virtualenv' item in 'Machine' PATH has lower priority than 'pyenv' (RC = $rc).$([char]27)[0m"
			Write-Host "$([char]27)[95mNOTICE   Read the unit 'Path Conflicts' in the documentation to get help.$([char]27)[0m"
			Write-Host "$([char]27)[37mINFO     Repair the inconsistent 'pyenv' PATH definitions manually. Then try again.$([char]27)[0m"
			exit $rc
		}
	}
} elseif (($found_machine_bin -eq "") -and ($found_machine_shims -eq "") -and ($found_user_bin -ne "") -and ($found_user_shims -ne "")) {
	# 'pyenv' PATH items found in 'User' PATH for 'This User Only'
	if ($found_user_plugin_shims -eq "") {
		$new_user_path = $pyenv_root + "plugins\pyenv-virtualenv\shims"
		foreach ($item in $user_paths) {
			$new_user_path += ";" + $item
		}
		try {
			Write-Host "$([char]27)[37mINFO     Writing registry. This could take some seconds ...$([char]27)[0m"
			[System.Environment]::SetEnvironmentVariable('PATH', $new_user_path, "User")
		} catch {
			$rc = 1
			Write-Host "$([char]27)[91mERROR    Cannot write 'User' PATH environment variable. (RC = $rc).$([char]27)[0m"
			Write-Host "$([char]27)[95mNOTICE   Read the unit 'Path Conflicts' in the documentation to get help.$([char]27)[0m"
			Write-Host "$([char]27)[37mINFO     Repair the inconsistent 'pyenv' PATH definitions manually. Then try again.$([char]27)[0m"
			exit $rc
		}
		# 'pyenv-virtualenv' PATH item has been correctly written
		Write-Host "$([char]27)[92mSUCCESS  'pyenv-virtualenv' 'User' PATH item is now in place. (RC = $rc).$([char]27)[0m"
		Write-Host "$([char]27)[95mNOTICE   Close and reopen the console terminal to let this change take effect.$([char]27)[0m"
	} else {
		if (($index_user_plugin_shims -lt $index_user_bin) -and ($index_user_plugin_shims -lt $index_user_shims)) {
			# 'pyenv-virtualenv' PATH item is already set in place
			Write-Host "$([char]27)[92mSUCCESS  'pyenv-virtualenv' 'shims' on 'User' PATH is already in place: '$found_user_plugin_shims' (RC = $rc).$([char]27)[0m"
		} else {
			# 'pyenv-virtualenv' item in 'User' PATH
			# has a lower priority than 'pyenv'.
			$rc = 1
			Write-Host "$([char]27)[91mERROR    'pyenv-virtualenv' item in 'User' PATH has lower priority than 'pyenv' (RC = $rc).$([char]27)[0m"
			Write-Host "$([char]27)[95mNOTICE   Read the unit 'Path Conflicts' in the documentation to get help.$([char]27)[0m"
			Write-Host "$([char]27)[37mINFO     Repair the inconsistent 'pyenv' PATH definitions manually. Then try again.$([char]27)[0m"
			exit $rc
		}
	}
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

# Return error level
exit $rc


# --- END OF CODE ------------------------------------------------------

