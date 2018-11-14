Basic usage
===========

This extension adds the "argparse" directive::

    .. argparse::
       :module: my.module
       :func: my_func_that_returns_a_parser
       :prog: fancytool

The `module`, `func` and `prog` options are required.

`func` is a function that returns an instance of the `argparse.ArgumentParser` class.

Alternatively, one can use :ref: like this::

    .. argparse::
       :ref: my.module.my_func_that_returns_a_parser
       :prog: fancytool

In this case :ref: points directly to argument parser instance.

For this directive to work, you should point it to the function that will return a pre-filled `ArgumentParser`.
Something like::

    def my_func_that_return_parser():
        parser = argparse.ArgumentParser()
        parser.add_argument('foo', default=False, help='foo help')
        parser.add_argument('bar', default=False)

        subparsers = parser.add_subparsers()

        subparser = subparsers.add_parser('install', help='install help')
        subparser.add_argument('ref', type=str, help='foo1 help')
        subparser.add_argument('--upgrade', action='store_true', default=False, help='foo2 help')

        return parser

.. note::
    We will use this example as a reference for every example in this document.

To document a file that is not part of a module, use :filename::

    .. argparse::
       :filename: script.py
       :func: my_func_that_returns_a_parser
       :prog: script.py

The 'filename' option could be absolute path or a relative path under current
working dir.

\:module\:
    Module name, where the function is located

\:func\:
    Function name

\:ref\:
    A combination of :module: and :func:

\:filename\:
    A file name, in cases where the file to be documented is not part of a module.

\:prog\:
    The name of your tool (or how it should appear in the documentation). For example, if you run your script as
    `./boo --some args` then \:prog\: will be "boo"

That's it. Directives will render positional arguments, options and sub-commands.

Sub-commands are limited to one level. But, you can always output help for subcommands separately::

    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool
       :path: install

This will render same doc for "install" subcommand.

Nesting level is unlimited::

    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool
       :path: install subcomand1 subcommand2 subcommand3


Other useful directives
-----------------------

:nodefault: Do not show any default values.

:nodefaultconst: Like nodefault:, except it applies only to arguments of types `store_const`, `store_true` and `store_false`.

:nosubcommands: Do not show subcommands.

:noepilog: Do not parse the epilogue, which can be useful if it contains text that could be incorrectly parse as reStructuredText.

:nodescription: Do not parse the description, which can be useful if it contains text that could be incorrectly parse as reStructuredText.

:passparser: This can be used if you don't have a function that returns an argument parser, but rather adds commands to it (`:func:` is then that function).
