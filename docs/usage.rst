


Basic usage
-----------------

Extension adds "argparse" directive::

    .. argparse::
       :module: my.module
       :func: my_func_that_return_parser
       :prog: fancytool

`module`, `func` and `prog` options are required.

func is function that return parser or just parser instance.

Alternative syntax is to use :ref: like this::

    .. argparse::
       :ref: my.module.my_func_that_return_parser
       :prog: fancytool

in this case :ref: also may point directly to argument pareser instance.

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

\:module\:
    Module name, where the function is located

\:func\:
    Function name

\:prog\:
    It's just name of your tool (or how it's should appear in your documentation). Ex. if you run your script as
    `./boo --some args` then \:prog\: will be "boo"

That's it. Directive will render positional arguments, options and sub-commands.

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