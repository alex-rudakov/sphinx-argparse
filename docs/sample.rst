==============
Examples
==============

Example structure of pages
=============================

Here is example structure of documentation for complex commands with lots of subcommands.
You are free to use any structure, but this may be a good starting point.

File "index.rst"::

    .. toctree::
       :maxdepth: 2

       cmd

File "cmd.rst"::


    Command line utitlites
    ***********************

    .. toctree::
       :maxdepth: 1

       cmd_main
       cmd_subcommand


File "cmd_main.rst"::


    Fancytool command
    ***********************

    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool

       subcommand
            Here we add reference to subcommand, to simplify navigation.
            See :doc:`cmd_subcommand`


File "cmd_subcommand.rst"::

    Subcommand command
    ***********************

    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool
       :path: subcommand


Source of example file
===========================

This file will be used in all generated examples.

.. literalinclude:: ../test/sample.py


Generated sample 1 - command with subcommands
================================================

Directive
----------------

Source::

    .. argparse::
       :ref: test.sample.parser
       :prog: sample

Output
----------------

.. argparse::
   :ref: test.sample.parser
   :prog: sample


Generated sample 2 - subcommand
==================================

Directive
----------------

Source::

    .. argparse::
       :module: test.sample
       :func: parser
       :prog: sample
       :path: game

Output
----------------

.. argparse::
   :module: test.sample
   :func: parser
   :prog: sample
   :path: game