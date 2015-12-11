sphinx-argparse
===============

Sphinx extension that automatically document argparse commands and options

For installation and usage details see docs.

Documentation is here: 
http://sphinx-argparse.readthedocs.org/en/latest/


Changelog & contributors
------------------------------

0.1.15

------------------------------

- Fixed malformed docutils DOM in manpages (Matt Boyer)


0.1.14

-----------------------------

- Support for aliasing arguments #22 (Campbell Barton)
- Support for nested arguments #23 (Campbell Barton)
- Support for subcommand descriptions #24 (Campbell Barton)
- Improved parsing of content of `epilog` and `description` #25 (Louis - https://github.com/paternal)
- Added 'passparser' option (David Hoese)

0.1.13

-----------------------------

- Bugfix: Choices are not always strings (Robert Langlois)
- Polished small mistakes in usage documentation (Dean Malmgren)
- Started to improve man-pages support (Zygmunt Krynicki)

------------------------------
0.1.12

- Improved error reporting (James Anderson)

------------------------------
0.1.11

- Fixed stupid bug, prevented things working on py3 (Alex Rudakov)
- added tox configuration for tests

------------------------------
0.1.10

- Remove the ugly new line in the end of usage string (Vadim Markovtsev)
- Issue #9 Display argument choises (Proposed by Felix-neko, done by Alex Rudakov)
- :ref: syntax for specifying path to parser instance. Issue #7 (Proposed by David Cottrell, Implemented by Alex Rudakov)
- Updated docs to read the docs theme

------------------------------
0.1.9

Fix problem with python version comparison, when python reports it as "2.7.5+" (Alex Rudakov)

------------------------------
0.1.8

Argparse is not required anymore separate module as of python 2.7 (Mike Gleen)

------------------------------
0.1.7

-- Nothing -- Created by axident.

------------------------------
0.1.6

Adding :nodefault: directive that skips default values for options (Stephen Tridgell)

------------------------------
0.1.5

Fix issue: epilog is ignored (James Anderson - https://github.com/jamesra)

------------------------------
0.1.4

Fix issue #3: ==SUPPRESS== in option list with no default value

------------------------------
0.1.2

Fix issue with subcommands (by Tony Narlock - https://github.com/tony)

------------------------------
0.1.1

Initial version

