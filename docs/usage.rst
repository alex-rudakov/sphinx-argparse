


Basic usage
-----------------

Extension adds "argparse" directive::

    .. argparse::
       :module: my.module
       :func: my_func_that_returns_a_parser
       :prog: fancytool

`module`, `func` and `prog` options are required.

func is function that returns an instance of the `argparse.ArgumentParser` class.

Alternative syntax is to use :ref: like this::

    .. argparse::
       :ref: my.module.my_func_that_returns_a_parser
       :prog: fancytool

in this case :ref: also may point directly to argument parser instance.

For this directive to work, you should point it to the function, that will return pre-filled `ArgumentParser`.
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
    We will use this example as a reference for every example in this doc.

To document a file that is not part of a module, use :filename:

    .. argparse::
       :filename: script.py
       :func: my_func_that_returns_a_parser
       :prog: script.py
        

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

Sub-commands are limited to one level. But, you always can output help for subcommands separately::


    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool
       :path: install

This will render same doc for "install" subcommand.

Nesting level is not limited::

    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool
       :path: install subcomand1 subcommand2 subcommand3


Other useful directives
-----------------------------------------

:nodefault: will hide all default values of options.

:nodefaultconst: Like nodefault:, expect it applies only to arguments of types `store_const`, `store_true` and `store_false`.
