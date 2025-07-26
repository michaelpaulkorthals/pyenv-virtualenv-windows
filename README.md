![pyenv-virtualenv_activate](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/under_construction_256.png "Under Construction")

> IMPORTANT NOTICE: This repository is currently under construction. Please wait until this message disappears before using this information.

[![license](https://img.shields.io/badge/License-GPL%203.0-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/LICENSE)
[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/CODE_OF_CONDUCT.md)
[![docs](https://img.shields.io/badge/Download-Doxygen%20Docs-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/doxygen_pyenv-virtualenv-windows.zip)

[![status](https://img.shields.io/badge/Status-Open%20Beta%20Test-60A020)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows)
[![pypi](https://img.shields.io/badge/PyPI-Pyenv%20Virtualenv%20Windows%20|%201.24-2040A0)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows)
[![github](https://img.shields.io/badge/GitHub-Pyenv%20Virtualenv%20Windows%20|%201.24-2040A0)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows)
[![python](https://img.shields.io/badge/Python-3.6%20|%203.7%20|%203.8%20|%203.9%20|%203.10%20|%203.11%20|%203.12%20|%203.13-C0C040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows)
[![change_log](https://img.shields.io/badge/Info-Change%20Log-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/src/pyenv-virtualenv-windows/CHANGELOG.md)

# Table of Contents <a name="table_of_contents"></a>
1. [Introduction](#introduction)</br>
    1.1. [Architecture](#architecture)</br>
    1.2. [Quick Reference](#quick_reference)</br>
	1.3. [Description](#description)
2. [Check Dependencies](#check_dependencies)</br>
3. [Installation](#installation)</br>
4. [Location](#location)</br>
5. [Usage](#usage)</br>
    5.1. [Concepts](#concepts)</br>
    &nbsp;&nbsp;&nbsp;&nbsp;5.1.1. [Audits](#audits)</br>
    &nbsp;&nbsp;&nbsp;&nbsp;5.1.2. [Commands](#commands)</br>
    &nbsp;&nbsp;&nbsp;&nbsp;5.1.3. [Project Properties](#project_properties)</br>
    &nbsp;&nbsp;&nbsp;&nbsp;5.1.4. [Help](#help)</br>
    &nbsp;&nbsp;&nbsp;&nbsp;5.1.5. [Logging](#logging)</br>
	5.2. [Create Virtual Environment](#create_virtual_environment)</br>
	&nbsp;&nbsp;&nbsp;&nbsp;5.2.1. [Create with Version and Name](#create_with_version_and_name)</br>
	&nbsp;&nbsp;&nbsp;&nbsp;5.2.2. [Create With Name Only](#create_with_name_only)</br>
	5.3. [List Installed Virtual Environments](#list_installed_virtual_environments)</br>
	5.4. [Activate Virtual Environment](#activate_virtual_environment)</br>
	5.5. [Delete Installed Virtual Environment](#delete_virtual_environment)</br>
	5.6. [Manage Project Properties](#manage_project_properties)</br>
	5.7. [Virtual Environment Prefix](#virtual_environment_prefix)</br>
	5.8. [Reconfigure After 'pyenv' Upgrade](#reconfigure_after_pyenv_upgrade)</br>
6. [Python Venv](#python_venv)</br>
7. [Patch for 'pyenv' for Windows](#patch_for_pyenv)</br>
    7.1 [Patch Details](#patch_for_pyenv_details)</br>
8. [How to contribute](#how_to_contribute)</br>

## Introduction <a name="introduction"></a>

### Architecture <a name="architecture"></a>

"pyenv-virtualenv" for Windows is a “pyenv” plugin to manage Python virtual environments, depending on different Python versions, for various Python projects.

It extends the command set of 'pyenv' for Windows by commands, which empowers  you to clear, quickly and efficiently manage a lot of python virtual environments for each of your Python projects. 

Let's have a look on the software architecture and its dependencies of 'pyenv-virtualenv' for Windows.

![pyenv-virtualenv_architecture](./images/pyenv-virtualenv_architecture.png "'pyenv-virtualenv' for Windows - Architecture'")

Opposite to 'pyenv', which depends on the Windows scripting languages only, the 'pyenv-virtualenv' for Windows depends on the Windows CMD/BAT scripting language (~1/3) and on the global Python version (~2/3) that is installed and configured via 'pyenv' for Windows.    

To fulfill the requirements for 'pyenv-virtualenv' for Windows, the global Python version must be 3.6+. Lower Python version are not supported. In addition, the Python package 'virtualenv' must be installed by pip into the global Python version.

Managed by 'pyenv-virtualenv' for Windows, for each project a single or multiple Python virtual environments can be installed and configured.

Within the path tree branch of the project, the local configured project properties define Python version and virtual environment name for the specific use case inside a project. 

These properties are inherited along the path tree branch. Using the 'activate' command without parameters, the specific virtual environment is automatically selected by 'pyenv-virtualenv' for Windows. 

The magic of 'pyenv-virtualenv' for Windows is located in the 'pyenv-win' command redirection feature. It activates the related utility scripts, which executable folders are prioritized within the PATH environment variable. Or, it automatically starts the python.exe or pip.exe in the related Python virtual environment 'Scripts' folder.

The result of this magic is an efficient and easy management of multiple projects on your development workstation, on test systems, productive servers or on the user client system in production.

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Quick Reference <a name="quick_reference"></a>

> NOTE: This unit serves as a reminder for experienced users to recapitulate how to use this tool. Newcomers should start with the [Description](#description).

For first, use the instructions on the <a href="https://github.com/pyenv-win/pyenv-win/" rel="noopener noreferrer" target="_blank">'pyenv' for Windows home page on GitHub</a> to completely install and configure 'pyenv'.

Completely perform these steps to fulfill the dependencies to 'pyenv' for Windows: 
1. Install Python version 3.6+. E.g. 'pyenv install 3.12.10'.
2. Make that Python version 'global'. E.g. 'pyenv global 3.12.10'.
3. Install package 'virtualenv'. E.g. 'pip install --upgrade virtualenv'.

Afterward, install 'pyenv-virtualenv' for Windows in a console terminal with 'Administrator' privileges:
~~~{.cmd}
pip install pyenv-virtualenv-windows
~~~

Finally, use these commands to manage virtual environments in your projects: 

| Command          | Description                                                                                        |
|:-----------------|:---------------------------------------------------------------------------------------------------|
| pyenv venv-new   | [Create a new virtual environment.](#create_virtual_environment)                                   |
| pyenv venv-list  | [List Python versions, environments and project properties.](#list_installed_virtual_environments) |
| pyenv venv-del   | [Delete a virtual environment.](#delete_installed_virtual_environment)                             |
| pyenv venv-props | [Manage project properties.](#manage_project_properties)                                           |
| pyenv venv-init  | [Reconfigure after 'pyenv' version upgrade.](#reconfigure_after_pyenv_upgrade)                     |
| activate         | [Activate virtual environment.](#activate_virtual_environment)                                     |
| deactivate       | [Deactivate virtual environment.](#activate_virtual_environment)                                   |

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Description <a name="description"></a> 

This unit is starting your tutorial to master your first steps in 'pyenv_virtualenv'.

In addition, download the Doxygen v1.13+ industry standard documentation for 'pyenv-virtualenv' for Windows from GitHub. 

The Doxygen HTML documentation is much easier to handle. It will be displayed in healthy dark mode.

[![docs](https://img.shields.io/badge/Download-Doxygen%20Docs-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/doxygen_pyenv-virtualenv-windows.zip)

![doxygen](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/doxygen_docu.png "Doxygen Industry Standard Documentation")

The Doxygen documentation includes:
  * Project description
  * User Manual
  * Operations Manual
  * Development Manual
  * Packages (Code documentation)
  * Classes (Code documentation)
  * Files (Code documentation)

Unzip the Doxygen ZIP file, find the 'index.html' file inside and simply open it with your web browser. Finally add a link to the documentation. 

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## Check Dependencies <a name="check_dependencies"></a>

> WARNING: Do not ignore this unit and read it carefully. There is no room for incompleteness. Otherwise, the dependencies are not completely fulfilled and you could fail.

Use the instructions on the <a href="https://github.com/pyenv-win/pyenv-win/" rel="noopener noreferrer" target="_blank">'pyenv' for Windows home page on GitHub</a> to completely install and configure 'pyenv'.   

Afterward, perform this manual test, to completely check the truth:
~~~{.cmd}
REM 1. Check if the 2 'pyenv' executable paths are at the beginning of the PATH.
path
REM 2. Check if the 'pyenv' Python executable is found on top of calling priority.
where python
REM 3. Check if the 'pyenv' global Python version is correctly set.
python -c "import sys; print(sys.executable); quit()"
REM 4. Ensure the actual versions of 'pip' and 'virtualenv' are installed.
python -m pip install --upgrade pip virtualenv
~~~

Output (e.g.):
~~~
C:\Users\Paul>path
PATH=C:\Users\Paul\.pyenv\pyenv-win\bin;C:\Users\Paul\.pyenv\pyenv-win\shims;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files\FireDaemon OpenSSL 3\bin;C:\cygwin64\bin;C:\Apache24\bin;C:\PHP7;C:\Program Files\MariaDB 10.5\bin; ...

C:\Users\Paul>where python
C:\Users\Paul\.pyenv\pyenv-win\shims\python
C:\Users\Paul\.pyenv\pyenv-win\shims\python.bat
C:\cygwin64\bin\python
C:\Program Files\KiCad\8.0\bin\python.exe
C:\Program Files\Inkscape\bin\python.exe
C:\Users\Paul\AppData\Local\Microsoft\WindowsApps\python.exe

C:\Users\Paul>python -c "import sys; print(sys.executable); quit()"
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\python.exe

C:\Users\Paul\eclipse-workspace\pyenv-virtualenv-windows>python -m pip install --upgrade pip virtualenv
Requirement already satisfied: pip in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (25.1.1)
Requirement already satisfied: virtualenv in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (20.31.2)
Requirement already satisfied: distlib<1,>=0.3.7 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (0.3.9)
Requirement already satisfied: filelock<4,>=3.12.2 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (3.18.0)
Requirement already satisfied: platformdirs<5,>=3.9.1 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (4.3.8)
~~~

> WARNING: If there is only the slightest deviation, it is essential you reconfigure 'pyenv'. Otherwise, the plugin 'pyenv-virtualenv' installer or the plugin itself will cancel after running into error messages.

Let's have a detailed view on the resulting output and possible remediation tasks.

1. Position of the 'pyenv' executable paths in PATH system environment variable:
~~~
PATH=C:\Users\Paul\.pyenv\pyenv-win\bin;C:\Users\Paul\.pyenv\pyenv-win\shims;C:\Program Files\Common Files\Oracle\Java\javapath;C:\Program Files\FireDaemon OpenSSL 3\bin;C:\cygwin64\bin;C:\Apache24\bin;C:\PHP7;C:\Program Files\MariaDB 10.5\bin; ...
~~~
* In case of success: 
  * The 'pyenv'-related paths are located at the beginning of PATH.
  * Both paths are beginning with '%USERPROFILE%\\.pyenv\\pyenv-win'.
  * The first path ends with '\\bin'.
  * The second path ends with '\\shims'.
* In case of failure/deviation:
  * NOTE: You need 'Administrator' privileges on your system.  
  * Goto Windows 'Settings' and search for 'path' and select 'Edit System Environment Variables'.
    * In the 'System Properties' dialog press the button "Environment Variables".
    * In the 'Environment Variables' dialog:
      * Cut both paths from user PATH. 
      * Prepending to the beginning, paste both paths to system PATH.
      * Close all dialogs with OK.
  * Repeat test 1.

2. Position of the 'python' command in the call priority list called by 'where python':
~~~
C:\Users\Paul>where python
C:\Users\Paul\.pyenv\pyenv-win\shims\python
C:\Users\Paul\.pyenv\pyenv-win\shims\python.bat
C:\cygwin64\bin\python
C:\Program Files\KiCad\8.0\bin\python.exe
C:\Program Files\Inkscape\bin\python.exe
C:\Users\Paul\AppData\Local\Microsoft\WindowsApps\python.exe
~~~
* In case of success:
  * Python is found in directory '%USERPROFILE%\\.pyenv\\pyenv-win\\shims'
  * The entries for that directory are shown on top of the list (highest priority)
* In case of failure/deviation:
  * Jump back to the detailed remediation instructions in test 1.
  * Repeat test 1 and 2.

3. Global 'pyenv' global version configuration for Python:
~~~
C:\Users\Paul\.pyenv\pyenv-win\versions\3.12.10\python.exe
~~~
* In case of success:
  * Python found its interpreter executable as '%USERPROFILE%\\.pyenv\\pyenv-win\\versions\\{global version number}\\python.exe'.
* In case of failure/deviation:
  * Call 'pyenv install {global version number}'.
  * Call 'pyenv global {global version number}'.
  * Call 'pyenv versions' to check, which version is '*' global.
  * Repeat test 3. 

4. Python packages 'pip' and 'virtualenv' are up-to-date:
~~~
Requirement already satisfied: pip in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (25.1.1)
Requirement already satisfied: virtualenv in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (20.31.2)
Requirement already satisfied: distlib<1,>=0.3.7 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (0.3.9)
Requirement already satisfied: filelock<4,>=3.12.2 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (3.18.0)
Requirement already satisfied: platformdirs<5,>=3.9.1 in c:\users\paul\.pyenv\pyenv-win\versions\3.12.10\lib\site-packages (from virtualenv) (4.3.8)
~~~
* In case of success:
  * The requirements for 'pip' and 'virtualenv' and its dependencies are completely satisfied.
* In case of failure/deviation:
  * Ensure that the global Python version in 'pyenv' is 3.6 or higher.
  * Repeat the whole test sequence beginning with test 1.

If everything is crystal-clear fine, then step forward to the next unit.

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## Installation <a name="installation"></a>

Hardware and system software requirements are the same as for 'pyenv' for Windows.

This plugin depends on 'pyenv' with globally installed Python version '3.6' or higher.

This plugin will be installed with Python 'pip' via the PyPI Cloud Application:

> IMPORTANT NOTE: Because the system PATH environment variable must be adopted, the package installer must be run with 'Administrator' privileges. Otherwise, the plugin-internal "install.bat" will show an error message and cancel.

~~~{.cmd}
pip install pyenv-virtualenv-windows
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## Location <a name="location"></a>

To find all 'pyenv' locations, execute the following command:
~~~{.cmd}
REM If Cygwin is not installed and configured:
set 
echo Search for "PYENV" manually.
REM Having Cygwin on board:
set | grep "pyenv"
~~~
Output (e.g.):
~~~
path=C:\Users\Paul\.pyenv\pyenv-win\bin;C:\Users\Paul\.pyenv\pyenv-win\shims; ...
PYENV=C:\Users\Paul\.pyenv\pyenv-win\
PYENV_HOME=C:\Users\Paul\.pyenv\pyenv-win\
PYENV_ROOT=C:\Users\Paul\.pyenv\pyenv-win\
~~~

This tree chart gives an overview about the most important sub-folders in this plugin:
~~~
%USERPROFILE%\.pyenv\pyenv-win\plugins\pyenv-virtualenv
├───bin
├───docs
│   └───images
├───libexec
└───shims
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## Usage <a name="usage"></a>

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Concepts <a name="concepts"></a>

For better understanding, how 'pyenv-virtualenv' for windows is working, read this unit carefully, before you start to use 'pyenv-virtualenv'. 

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Audits <a name="audits"></a>

Each utility in 'pyenv-virtualenv' for Windows is auditing your system environment to avoid functional problems or lack of completeness in installing/configuring 'pyenv' and 'pyenv-virtualenv' for Windows. 

In case of deviation, the utility logs a red-colored error message and a remediation instruction to the console. Afterward, the program will be canceled to avoid further problems.

It is essential that you remediate all deviations to finally get 'pyenv-virtualenv' for Windows working well.

If everything is fine, nothing will be logged about the audits.

If you want to see the audit activities and its results on detail on the console terminal, execute these commands:
~~~{.cmd}
REM Set log level to "verbose"
set LOG_LEVEL=15
REM Execute a passive utility, which shows information only
pyenv virtualenvs
REM Reset log level to default ("info")
set LOG_LEVEL=20
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Commands <a name="commands"></a>

The management of Python versions and virtual environments for Posix/Linux and Windows is implemented as a series of commands, which are executed in the CLI terminal. 

In both platform ecosystems the syntax and behavior of the utilities are nearly identical. 'pyenv-virtualenv' for Windows includes some new enhancements. Use the '-h' or '--help' argument to display the details for each utility command.

Using Python virtual environment, the short form 'venv' has been established within the publications of the developer community. Also, 'venv' is quicker and easier to type in opposite to 'virtualenv'.

In addition, in Windows the words 'new' and 'list' are more familiar to create and to list somthing on command line. 

"rm" in Cygwin, Posix/Linux operating systems and "del" on Windows are the common synonyms to delete/remove something in both ecosystems. 

To round this up, 'activate' and 'deactivate' are the known commands to enable/disable the Python virtual environment.   

To take these mods into account, these short and alternative command names are implemented:

| Original                | Short             | Alternative     |
|:------------------------|:------------------|:----------------|
| pyenv virtualenv        | -                 | pyenv venv-new  |
| pyenv virtualenvs       | -                 | pyenv venv-list |
| pyenv virtualenv-delete | pyenv venv-del    | venv-rm         |
| pyenv virtualenv-prefix | pyenv venv-prefix | -               |
| pyenv virtualenv-props  | pyenv venv-props  | -               |
| pyenv virtualenv-init   | pyenv venv-init   | -               |
| pyenv activate          | -                 | activate        |
| pyenv deactivate        | -                 | deactivate      |

Now the best of the two worlds can coexist. Use this as you like.

My favorite and more coherent command list for 'pyenv-virtualenv' for Windows is:

| Command          | Description                                                |
|:-----------------|:-----------------------------------------------------------|
| pyenv venv-new   | Create a new virtual environment.                          |
| pyenv venv-list  | List Python versions, environments and project properties. |
| pyenv venv-del   | Delete a virtual environment.                              |
| pyenv venv-props | Manage project properties.                                 |
| pyenv venv-init  | Reconfigure after 'pyenv' version upgrade.                 |
| activate         | Activate virtual environment.                              |
| deactivate       | Deactivate virtual environment.                            |

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Project Properties <a name="project_properties"></a>

To control, which Python version and virtual environment are in use for a specific local project, some hidden information files can be manged:

| File Name       | Content                                                                                                       |
|:----------------|:--------------------------------------------------------------------------------------------------------------|
| .python-version | 3-Digit Python version number (e.g. 3.12.10)                                                                  |
| .python-env     | Virtual environment short name (e.g. cinema_5)                                                                |
| .tree-excludes  | Tuple of folder names to exclude from local project tree view.<br/>E.g.: ('docs', '\_\_pycache\_\_', '.idea') |

These files automatically inherit the version, virtual environment and exclude settings along the Windows directory paths.

These settings allow you to use different Python versions and virtual environments within the same project.

The content of '.tree-excludes' file allows to exclude 'spam' folders from the tree view. E.g. 'docs', caches and IDE project configuration folders. The excludes prevents you from scrolling through non-relevant information. 

In this example project, the setup routine and the application are using the same Python version, but different virtual environments:
~~~
C:\Users\Paul\eclipse\cinema_5
│   .python-version  <-- Configured Python version  
│   docs.doxyfile  
├───back-end
│   .python-env      <-- Configured virtual environment
│   .tree-excludes   <-- Configured directory tree excludes
│   back-end.bat     <-- Launcher to automate app call
│   back-end.py      <-- Application script
├───docs
│   └───images
└───setup
    .python-env      <-- Configured another virtual environment
    setup.bat        <-- Launcher to automate the setup call
    setup.py         <-- Setup script
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Help <a name="help"></a>

Each of the tool scripts includes Python argument parser 'argparse'. If you add the '-h' or '--help' option:  
~~~{.cmd}
pyenv virtualenv --help 
~~~

See output of this call for details:
~~~
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
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Logging <a name="logging"></a>

Each of the 'pyenv' scripts has a colored comprehensive logging implemented. 

> NOTE: No log files are implemented. The log output is written to console only:

The logging is divided into to the following log levels:

| Level    | Value | Color   | Description                                              |
|:---------|------:|:--------|:---------------------------------------------------------|
| critical |    50 | red+    | Critical error, which let the program exit immediately.  |
| error    |    40 | red     | Normal error message, which finishes the program.        |
| success  |    35 | green   | Success message.                                         |
| warning  |    30 | yellow  | Warning message.                                         |
| notice   |    25 | magenta | Notice message.                                          |
| info     |    20 | white   | Information message (Default level).                     |
| verbose  |    15 | blue    | Verbose message for overview in diagnosis.               |
| debug    |    10 | green   | Debug message to trace states in running the program.    |
| spam     |     5 | gray    | Mass messages for loop observations and deep diagnosis.  |

The lower the log level is, much more colored log will appear on console terminal. 

The log level can be set using the OS environment variable "LOG_LEVEL":
~~~{.cmd}
REM Set log level to "debug"
set LOG_LEVEL=10
REM Override virtual environment
pyenv virtualenv 3.12 cinema_5 --props
REM Reset loglevel to default
set LOG_LEVEL=20
~~~

Output:

![pyenv_virtualenv_debug_logging](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/pyenv_virtualenv_debug_logging.png "Colored Comprehensive Logging")

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Create Virtual Environment <a name="create_virtual_environment"></a>

To generate a virtual environment for the Python version installed in 'pyenv', call
'pyenv virtualenv', specifying the installed Python version you want and the name
of the virtualenv directory (e.g. the short name of your project folder). 

In addition, this script configures the version and the virtual environment for your project.

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Create with Version and Name <a name="create_with_version_and_name"></a>

> NOTE: Be aware that this command copies 2 hidden files into your project folder. These files are your 'pyenv virtualenv' project properties, which contain the Python version number and the virtual environment name. If required, other scripts in this workflow read these files to know which Python version and virtual environment is set.

This example creates a virtual environment named 'cinema_5', which depends on version 'Python 3.12.10':
~~~{.sh}
REM Change directory to your Python project folder
cd "%USERPROFILE%\eclipse-workspace\cinema_5"
REM Generate the virtual environment and set project properties in CWD
pyenv virtualenv 3.12.10 cinema_5 --props
REM Show project property files
dir .python*.*
type .python-version
type .python-env
~~~

Output:
~~~
INFO     Creating Python virtual environment in "pyenv":
INFO       * Version: 3.12.10
INFO       * Name:    cinema_5
INFO       * Set project properties: True
INFO     This will take some seconds ...
SUCCESS  Virtual environment "cinema_5" is installed in "pyenv", depending on "Python 3.12.10".

 Datenträger in Laufwerk C: ist SYSTEM
 Volumeseriennummer: 38E4-3A30

 Verzeichnis von C:\Users\Paul\eclipse-workspace\cinema_5

Fr, 04. 07. 2025  07:46                 8 .python-env
Fr, 04. 07. 2025  07:46                 7 .python-version
               2 Datei(en),             15 Bytes
               0 Verzeichnis(se), 117.726.687.232 Bytes frei
3.12.10
cinema_5
~~~

'pyenv virtualenv' forwards 2 positional arguments and 1 option to the underlying command that actually creates the virtual environment using 'python -m venv':

This will create a virtual environment based on 'Python 3.12.10' under '%PYENV_ROOT%/versions' in a folder junction called 'cinema_5-3.12.10'.

That folder junction is linked to folder:
~~~
%PYENV_ROOT%/versions/3.12.10/envs/cinema_5-3.12.10
~~~
Finally, the 'pyenv virtualenv' project property files has been written.

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Create With Name Only <a name="create_with_name_only"></a>

If there is only one positional argument given to 'pyenv virtualenv', the virtualenv will be created with the given name based on the current pyenv Python version.

~~~{.cmd}
REM Check global Python version 
pyenv version
3.12.10 (set by ...)
REM Change directory to your Python project folder
cd "%USERPROFILE%\eclipse-workspace\cinema_5"
REM Generate the virtual environment and set project properties
pyenv virtualenv 3.12.10 cinema_5 --props
~~~

Output:
~~~
3.12.10 (set by ...)

INFO     Creating Python virtual environment in "pyenv":
INFO       * Version: 3.12.10 (global)
INFO       * Name:    cinema_5
INFO       * Set project properties: True
INFO     This will take some seconds ...
SUCCESS  Virtual environment "cinema_5" is installed in "pyenv", depending on "Python 3.12.10".
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### List Installed Virtual Environments <a name="list_installed_virtual_environments"></a>

The utility 'pyenv virtualenvs' displays 3 tables and a tree view:
1. Installed Python Versions
2. Available Virtual Environments
3. Local Project Properties
4. CWD tree view

Output:

![pyenv_virtualenvs_tables](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/pyenv_virtualenvs_tables.png "") ![pyenv_virtualenvs_tree](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/pyenv_virtualenvs_tree.png "Data Listing")

If you know about Python Virtual Environment it is easy for you to interpret the data. Some stati are depending on the PWD path, the Python version numbers and the installed and globalized versions and virtual environments.

There are two entries for each virtualenv, and the shorter one is just a symlink.

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Activate Virtual Environment <a name="activate_virtual_environment"></a>

> NOTE: The behavior of the 'activate' command depends on the project property settings on CWD. See unit 'Concepts' / 'Project Properties'.

Use these commands to activate and use the configured virtual environment:
~~~{.cmd}
REM Activate Python virtual environment
activate
... use and manage the virtual environment ...
REM Deactivate Python virtual environment
deactivate
~~~

![pyenv-virtualenv_activate](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/pyenv-virtualenv_activate.png "Activated Virtual Environment")

Please notice the details in the screenshot above:
* The 'activate' command adds information in colors to the terminal prompt:
  - Virtual environment name (yellow) 
  - Python version number (cyan)
  - Path string (blue)
* The successful activation is proved by checking the output 'sys.executable' in Python.
* The 'deactivate' command removes virtual environment name and version from terminal prompt.
* After finally executed the 'deactivate' command closes the subshell and returns to your main shell. The color of the path in the terminal prompt turns to white again.

To ensure interoperability the equivalent Posix/Linux commands are available in Windows. Here the complete command listing with all synonyms and argument scenarios: 
~~~{.cmd}
pyenv activate
pyenv activate <name>
pyenv activate <version> <name>
pyenv deactivate
activate
activate <name>
activate <version> <name>
deactivate
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Delete Installed Virtual Environment <a name="delete_installed_virtual_environment"></a>

Manually removing the related junction (symbolic links) in the 'versions' directory and the related virtual environment in the 'envs' subfolder of that version will delete a virtual directory.

See in these folders:
~~~
%PYENV_ROOT%versions
%PYENV_ROOT%versions\{version}\envs
~~~

To automate this, use the 'pyenv-virtualenv' plugin to uninstall virtual environments:
~~~{.cmd}
pyenv virtualenv-delete {version} {name}
pyenv virtualemv-delete 3.12.10 cinema_5a
~~~

> NOTE: This will only delete the virtual environment, so called 'cinema_5a'. The version '3.12.10' remains untouched. 

Use 'pyenv' as usual to manage the Python versions and to uninstall these:
~~~{.cmd}
REM Unsinstall
pyenv uninstall {version}
pyenv uninstall 3.9.6
REM Set version 'global'
pyenv global {version}
pyenv global 3.13.3
~~~

Finally, to check your results in a single view, call:
~~~{.cmd}
pyenv virtualenvs
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Manage Project Properties <a name="manage_project_properties"></a>

This utility manages two virtual environment-related project properties:
1. .python-version (e.g. 3.12.10)  
2. .python-env (cinema_5)

It has 3 features:

| Command                       | Description                       | Feature Aliases            |
|:------------------------------|:----------------------------------|:---------------------------|
| pyenv virtualenv-props set    | Set project properties in CWD.    | s                          |
| pyenv virtualenv-props unlink | Unlink project properties in CWD. | u,d,del,delete,r,rm,remove |
| pyenv virtualenv-props list   | List project properties in CWD.   | l,ls                       |

![pyenv-virtualenv_activate](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/pyenv_virtualenv-props.png "Project Properties List")

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

#### Exclude 'Spam' Folders 

In 'pyenv-virtualenv' for Windows an additional project property '.tree-excludes' is implemented. This property will also be automatically inherited to its subfolders. 

It is used to exclude 'spam' folders files and folders tree-view, which is displayed by the 'pyenv virtualenvs' and 'pyenv virtualenv-props list' commands.  

It can be manually managed in CWD as follows:
~~~{.cmd}
REM Set the '.tree-exclude' property in CWD, e.g.:
echo ('docs', '__pycache__', '.idea') > .tree-excludes
REM Edit the '.tree-exclude' property in CWD, e.g.:
notepad++ .tree-exclude 
REM Unlink the '.tree-exclude' property from CWD, e.g.:
del .tree-excludes
REM List the project properties, e.g.:
pyenv virtualenv-props list
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Virtual Environment Prefix <a name="virtual_environment_prefix"></a>

Use these commands to get the path prefix for virtual environment:
~~~{.cmd}
REM Get prefix for the CWD
pyenv virtualenv-prefix
REM Get prefix for installed virtual environment
pyenv virtualenv-prefix {name}
pyenv virtualenv-prefix cinema_5a 
~~~

Output: 

![pyenv-virtualenv-prefix](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/images/pyenv-virtualenv-prefix.png "Virtual Environment Prefix")

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Reconfigure After 'pyenv' Upgrade <a name="reconfigure_after_pyenv_upgrade"></a>

After upgrading "pyenv" some path settings and the patch must be reconfigured. This ensures that the 'pyenv-virtualenv' plugin continues working without errors.

> IMPORTANT NOTE: This command should be run in a console terminal, which has been opened as 'Administrator'. Otherwise, it would be not capable to alter the system PATH environment variable when managing the path priorities for 'pyenv-virtualenv' for Windows. If that is necessary, and it would run with user privileges only, it would display an error message and cancel.

You should not waste your efforts on this task to do it manually. 

Instead, use this command or its alias to run this job automatically within seconds:
~~~{.cmd}
pyenv virtualenv-init
pyenv venv-init 
~~~

> NOTE: This command 'pyenv virtualenv-init' has in Posix/Linux a different meaning, help and description. Here in Windows, please refer to how it is documented for Windows.

In addition, this command scans the PATH environment variable and displays the dead links to non-existing folders.

If you have those deviations, it is your responsibility to remove the dead links from PATH.    

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## Python Venv <a name="python_venv"></a>

There is a [venv](http://docs.python.org/3/library/venv.html) module available
for 'Python 3.3+'.

It provides an executable module 'venv', which is the successor of 'virtualenv'
and distributed by default.

'pyenv-virtualenv' uses 'python -m venv' if it is available and the 'virtualenv'
command is not available.

Each utility in 'pyenv-virtualenv' tries to import the 'virtualenv' near the beginning of the program. This let the utility programs exit immediately by error and so should avoid problems with globalized outdated Python versions. 

[[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## Patch for 'pyenv' for Windows <a name="patch_for_pyenv"></a>

To operate this plugin, a patch for 'pyenv' for Windows is needed. This patch touches the file '%PYENV_ROOT%\\shims\\pyenv.bat'.

That patch significantly improves the 'pyenv' plugin interface by these advantages:
* It simplifies and stabilizes the plugin interface to dock 'pyenv-virtualenv' for Windows.
* Installing a plugin, the following code folders and its content politely remain untouched:
  * %PYENV_ROOT%\\libexec
  * %PYENV_ROOT%\\bin
  * %PYENV_ROOT%\\shims
* It allows to implement multiple plugins from different sources basing on a unified syntax.
* It ensures Posix/Linux to Windows interoperability implementing the same command names e.g. like in 'pyenv-virtualenv' for Linux or macOS.  

The current version 1.2.4 of 'pyenv-virtualenv' for Windows is including that patch. This patch redirects the 'pyenv' command to its patched counterpart in its own 'shims' folder. 

This temporary workaround allows 'pyenv-virtualenv' for Windows to operate without problems for the upcoming Beta test.

A pull request on GitHub for 'pyenv' for Windows is set. After the supervisor of 'pyenv' for Windows with curtesy answers this pull request with a new version, an upgrade for 'pyenv-virtualenv' for Windows is planned. That future upgrade will not include a workaround anymore.    

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

### Patch Details <a name="patch_for_pyenv_details"></a>

The actual workaround redirection uses the PATH environment variable to redirect the 'pyenv' command to the 'pyenv-virtualenv' for Windows 'shims' folder, file 'pyenv.bat' (patched version).  

You are recommended to compare the original and patched files e.g. using Notepad++ with 'Compare' plugin to make all changes visible.

The first change (near the beginning of the script), is only part of the current workaround to make 'pyenv-virtualenv' for Windows operable.

It avoids problems if something could be wrong with 'pyenv' for Windows.

In addition, it makes the script independent of its location within the '%PYENV_ROOT%' directory tree:
~~~{.cmd}
@echo off
setlocal
chcp 65001 >nul 2>&1

REM --------------------------------------------------------------------
REM --- PATCH 1 FOR PYENV-VIRTUALENV 2025-07-14 ---
REM --------------------------------------------------------------------

REM Determine log level
if not defined LOG_LEVEL goto log_level1
  set /a LOG_LEVEL=%LOG_LEVEL% 
  goto log_level2
:log_level1
  set /a LOG_LEVEL=20
:log_level2

REM Determine pyenv root folder
if not defined PYENV_ROOT goto undefined0
if not exist "%PYENV_ROOT%" goto nonexist0
goto continue0
undefined0:
  echo [101mCRITICAL Cannot find "PYENV_ROOT" environment variable.[0m
  echo [37mINFO     Check/install/configure "pyenv". Then try again.[0m
  exit /b 1
:nonexist0
  echo [101mCRITICAL Cannot find environment "pyenv root" directory "%PYENV_ROOT%".[0m
  echo [37mINFO     Check/repair/configure "pyenv". Then try again.[0m
  exit /b 1
:continue0

REM NOTE: In addition all substrings "%~dp0..\" has been replaced
REM by "%PYENV_ROOT%" to make this script independent from its location
REM on the system hard disk.
REM --------------------------------------------------------------------
...
~~~

The second change enhances the plugin interface. See the new code in the 'plugin' function:
~~~{.cmd}
...
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
:plugin
set "exe=%PYENV_ROOT%libexec\pyenv-%1"
rem TODO needed?
call :normalizepath %exe% exe

if exist "%exe%.bat" (
  set "exe=call "%exe%.bat""

) else if exist "%exe%.cmd" (
  set "exe=call "%exe%.cmd""

) else if exist "%exe%.vbs" (
  set "exe=cscript //nologo "%exe%.vbs""

) else if exist "%exe%.lnk" (
  set "exe=start '' "%exe%.bat""
) else (
  REM --------------------------------------------------------------------
  REM --- PATCH 2 FOR PYENV-VIRTUALENV 2025-07-14 ---
  REM --------------------------------------------------------------------
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Cannot find executable "%exe%.*".[0m
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Redirecting command "pyenv %1" to related plugin ...[0m
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Working around entropy caused by deviations from 'pyenv-virtualenv' common command design ...[0m
  REM Determine the plugin name
  REM NOTE: The "virtualenv" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="virtualenv" goto redirect_to_virtualenv
  REM NOTE: The "virtualenvs" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="virtualenvs" goto redirect_to_virtualenv
  REM NOTE: The "activate" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="activate" goto redirect_to_virtualenv
  REM NOTE: The "deactivate" command will be redirected to 'pyenv-virtualenv'.
  if "%1"=="deactivate" goto redirect_to_virtualenv
  goto endworkaround1
  :redirect_to_virtualenv
    set "PLUGIN_NAME=virtualenv"
    goto continue1
  :endworkaround1
    if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Detecting plugin name in command name "%1" ...[0m
    for /f "tokens=1 delims=-" %%a in ("%1") do set "PLUGIN_NAME=%%a"
	REM NOTE: All commands starting with "venv-" will be redirected to "pyenv-virtualenv".
	if "%PLUGIN_NAME%"=="venv" goto redirect_to_virtualenv
	REM NOTE: All other commands will be forwarded to other installed plugins if available.
	goto continue1
  :continue1
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Plugin name: "%PLUGIN_NAME%".[0m
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Plugin command: "%1".[0m
  REM Forward the command to the detected plugin
  set "exe=%PYENV_ROOT%plugins\pyenv-%PLUGIN_NAME%\libexec\pyenv-%1"
  call :normalizepath %exe% exe
  if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Plugin call: "%exe%".[0m
  REM Calculate path to existing executable only
  if exist "%exe%.bat" (
    set "exe=call "%exe%.bat""
  ) else if exist "%exe%.cmd" (
    set "exe=call "%exe%.cmd""
  ) else if exist "%exe%.vbs" (
    set "exe=cscript //nologo "%exe%.vbs""
  ) else if exist "%exe%.lnk" (
    set "exe=start '' "%exe%.bat""
  ) else (
	REM Not existing
    if %LOG_LEVEL% leq 15 echo [94mVERBOSE  Cannot find executable "%exe%.*".[0m
    echo pyenv: no such command '%1'
	REM Cancel with error level 1
    exit /b 1
  )
  REM The following 2 lines are obsolete now and has been commented:
  REM echo pyenv: no such command '%1'
  REM exit /b 1
  
  REM ------------------------------------------------------------------
)

:: replace first arg with %exe%
set cmdline=%*
set cmdline=%cmdline:^=^^%
set cmdline=%cmdline:!=^!%
set "arg1=%1"
set "len=1"
:loop_len
set /a len=%len%+1
set "arg1=%arg1:~1%"
if not [%arg1%]==[] goto :loop_len

setlocal enabledelayedexpansion
set cmdline=!exe! !cmdline:~%len%!
:: run command (no need to update PATH for plugins)
:: endlocal needed to ensure exit will not automatically close setlocal
:: otherwise PYTHON_VERSION will be lost
endlocal && endlocal && %cmdline% || goto :error
exit /b
::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::::
...
~~~

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)

## How to Contribute <a name="how_to_contribute"></a> 

Hi, I am Paul.

As supervisor of 'pyenv-virtualenv' for Windows I welcome you to this project.

Currently, this Python software project is in the state of 'Open Beta Test'.

[![pypi](https://img.shields.io/badge/Status-Open%20Beta%20Test-60A020)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows) 

From my point of view it is stable, but what do you think about it?

In case you want to discuss an 'issue', or, have a brilliant idea for a 'pull request', I ask you to read the related units in the README.md. In addition, download and study the Doxygen documentation. 

[![docs](https://img.shields.io/badge/Download-Doxygen%20Docs-20A040)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/doxygen_pyenv-virtualenv-windows.zip) 

In most cases, this should avoid unnecessary effort and communication. 

To ensure a clear, calm and joyful working atmosphere in this project, I recommend you to be informed and to agree to our rules of engagement before you publish your contribution. 

[![Contributor Covenant](https://img.shields.io/badge/Contributor%20Covenant-2.1-4baaaa.svg)](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/blob/main/CODE_OF_CONDUCT.md)

Our Code of Conduct is version 2.1 of the Contributor Covenant, published with the courtesy of the organization of the same name [https://www.contributor-covenant.org/](https://www.contributor-covenant.org/). 

Possible violations/incidents regarding the code of conduct in this project can be reported to me via a ['code of conduct'-labeled 'pull-request' contribution to this project](https://github.com/michaelpaulkorthals/pyenv-virtualenv-windows/pulls).

Let's do it this way!

[![quick_reference](https://img.shields.io/badge/&#8594;-Quick%20Reference-20A040)](#quick_reference)
[![contents](https://img.shields.io/badge/&#8594;-Contents-4060E0)](#table_of_contents)


\-\-\- END OF DOCUMENT ----------------------------------------------------

