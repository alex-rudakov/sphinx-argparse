Markdown
========

As of version 0.2.0, markdown (rather than only reStructuredText) can be included inside directives as nested content. While markdown is much easier to write, please note that it is also less powerful. An example is below::

   .. argparse::
       :filename: ../test/sample.py
       :func: parser
       :prog: sample
       :markdown:

       Header 1
       ========

       [I'm a link to google](http://www.google.com)

       ## Sub-heading

       ```
       This
        is
         a
         fenced
        code
       block
       ```

The above example renders as follows:

.. argparse::
    :filename: ../test/sample.py
    :func: parser
    :prog: sample
    :markdown:

    A random paragraph

    Heading 1
    =========

    [I'm a link to google](http://www.google.com)

    ## Sub heading

    ```
    This
     is
      a
      fenced
     code
    block
    ```

The `CommonMark-py <https://github.com/rtfd/CommonMark-py>`__ is used internally to parse Markdown. Consequently, only Markdown supported by CommonMark-py will be rendered.

You must explicitly use the `:markdown:` flag, otherwise all content inside directives will be parsed as reStructuredText.

A note on headers
-----------------

If the Markdown you nest includes headings, then the first one **MUST** be level 1. Subsequent headings can be at `lower levels <http://daringfireball.net/projects/markdown/syntax#header>`__ and then rendered correctly.

Hard line breaks
----------------

Sphinx strips white-space from the end of lines prior to handing it to this package. Because of that, hard line breaks can not currently be rendered.

Replacing/appending/prepending content
--------------------------------------

When markdown is used as nested content, it's not possible to create dictionary entries like in reStructuredText to `modify program option descriptions <extend.html>`__. This is because CommonMark-py does not support dictionary entries.

MarkDown in program descriptions and option help
------------------------------------------------

In addition to using MarkDown in nested content, one can also use MarkDown directly in program descriptions and option help messages. For example::

    import argparse

    def blah():
        parser = argparse.ArgumentParser(description="""
    ### Example of MarkDown inside programs
    
    [I'm a link](http://www.google.com)
    """)
        parser.add_argument('cmd', help='execute a `command`')
        return parser

To render this as MarkDown rather than reStructuredText, use the `markdownhelp` option::

    .. argparse::
        :filename: ../test/sample2.py
        :func: blah
        :prog: sample
        :markdownhelp:

This will then be rendered as:

.. argparse::
    :filename: ../test/sample2.py
    :func: blah
    :prog: sample
    :markdownhelp:

