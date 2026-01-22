# Plugin "pyenv-virtualenv" for Windows 

## Version History

This version history is sorted in descending order.

The version number except the patch number are synchronous to the related 'pyenv-virtualenv' package for Posix/Linux, which features has been reverse engineered for Windows.

### 1.2.6 (Open Beta) (2025-08-05)
* Debug 'install.bat' and its sub processes.
* Debug 'pyenv-virtualenv' and its sub processes. 
* Debug creating symbolic links and junctions in Windows with 'Administrator' permissions.
* Debug enabling 'pyenv' and 'pyenv-virtualenv' to have the correct PATH priorities.
* Detect missing 'pip' executable when activating virtual environment on Python 3.3-. 
* Add option '--tree' to commands 'pyenv virtualenvs', 'pyenv virtualenv-props list'.
* Remove obsolete command 'pyenv virtualenv-init' from concept, product and documentation.
* Ensure existence of e.g. 'CHANGELOG.md', 'README.bat', 'install*.*' by modifying 'MANIFEST.in'.
* Optimize the project settings in 'pyproject.toml'.
* Update the documentation (e.g. units 'Installation', 'Path Conflicts', 'Location', 'Publication on PyPI').
* Remove the 'Under Construction' badge and message from GitHub and PyPi.
* This new version deprecates version 1.2.5.

### 1.2.5 (Alpha)
* Test, analyze and debug PiPI packaging.
* This new version deprecates version 1.2.4.

### 1.2.4 (Alpha)
* Analyze the documentation, code, data and behavior of the Linux version of the plugin.
* Configure and use Doxygen web documentation. See 'docs' folder.
* Create data and communication model.
* Reverse engineer Linux version of the plugin for Windows.
* Run Proof of Concept (PoC) tests, successfully resulting in go for development.
* Decide to start development of this plugin. 
* Add launchers to link the plugin into folder 'libexec'.
* Add 'bin/lib/*.py' helper libraries to support the Python code files of this plugin.
  * hlp.py
  * log.py
  * tbl.py
  * tre.py
* Add 'pyenv virtualenv-init' to reinitialize 'pyenv-virtualenv' after upgrading 'pyenv'.  
* Add 'pyenv activate' to activate Python virtual environment.
* Add 'pyenv deactivate' to deactivate Python virtual environment.
* Add 'pyenv virtualenv'  to create a new virtual environment.
* Add 'pyenv virtualenv-props' to manage local project properties.  
* Add 'pyenv virtualenvs' to list all Python versions, virtual environments and local project properties.
* Add 'pyenv virtualenv-prefix' to display real path prefix for virtual environment.
* Add 'pyenv virtualenv-delete' to delete a virtual environment.
* Add aliases for some commands to ease the command handling.
* Construct the workaround to redirect the 'pyenv' command to the its patch.
* Add install script 'install.bat' to install this Windows plugin into 'pyenv' for Windows.
* Perform Alpha Test in laboratory on all features.
* Set up GitHub repository.
* Compile Doxygen documentation, finally for this version. 
* Release this version for Open Beta Test on PyPI.

\-\-\- END OF DOCUMENT ----------------------------------------------------

