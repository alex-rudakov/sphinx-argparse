Markdown
========

As of version 0.2.0, markdown (rather than only reStructuredText) can be included inside directives as nested content. While markdown is much easier to write, please note that it is also less powerful. An example is below::

   .. argparse::
       :ref: test.sample.parser
       :prog: sample
       :markdown:

       Header 1
       ========

       [I'm a link to google](http://www.google.com)

       ```
       This
        is
         a
         fenced
        code
       block
       ```

This renders as follows:

.. argparse::
    :ref: test.sample.parser
    :prog: sample
    :markdown:

    A random paragraph

    Heading 1
    =========

    ## Sub heading

    [I'm a link to google](http://www.google.com)

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

If the Markdown you nest includes headings, then the first one **MUST** be level 1. Subsequent headings can be at lower levels and then rendered correctly. As of this writing, only `setext-style headers http://daringfireball.net/projects/markdown/syntax#header`__ are supported by CommonMark-py.

Hard line breaks
----------------

Sphinx strips white-space from the end of lines prior to handing it to this package. Because of that, hard line breaks can not currently be rendered.

Replacing/appending/prepending content
--------------------------------------

When markdown is used as nested content, it's not possible to create dictionary entries like in reStructuredText to `modify program option descriptions <extend.html>`__. This is because CommonMark-py does not support dictionary entries.
