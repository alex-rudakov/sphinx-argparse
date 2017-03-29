Examples
========

Example documentation structure
-------------------------------

Here is an example structure for the documentation of a complex command with many subcommands. 
You are free to use any structure, but this may be a good starting point.

File "index.rst"::

    .. toctree::
       :maxdepth: 2

       cmd

File "cmd.rst"::


    Command line utilities
    **********************

    .. toctree::
       :maxdepth: 1

       cmd_main
       cmd_subcommand


File "cmd_main.rst"::


    Fancytool command
    ***********************

    .. argparse::
       :module: my.module
       :func: my_func_that_returns_a_parser
       :prog: fancytool

       subcommand
            Here we add a reference to subcommand, to simplify navigation.
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
----------------------

This file will be used in all generated examples.

.. literalinclude:: ../test/sample.py


Generated sample 1 - command with subcommands
---------------------------------------------

Directive
~~~~~~~~~

Source::

    .. argparse::
       :filename: ../test/sample.py
       :func: parser
       :prog: sample

Output
~~~~~~

.. argparse::
    :filename: ../test/sample.py
    :func: parser
    :prog: sample


Generated sample 2 - subcommand
-------------------------------

Directive
~~~~~~~~~

Source::

    .. argparse::
       :filename../test/sample.py
       :func: parser
       :prog: sample
       :path: game

Output
~~~~~~

.. argparse::
   :filename: ../test/sample.py
   :func: parser
   :prog: sample
   :path: game
