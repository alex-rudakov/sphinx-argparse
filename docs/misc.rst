Miscellaneous
=============

Text wrapping in argument tables
--------------------------------

A common issue with the default html output is that the table within which options are displayed is designed such that the option descriptions are each held on one line. Any even remotely lengthy description then causes the viewer to need to scroll left/right to view the entire text. This is typically undesirable and the fix is described fully `here <http://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html>`_.

The short synopsis is below:

 1. Create a new CSS file (likely under `_static`) and point to it in `html_static_path` and `html_context` (or a template in the `templates_path`) in `conf.py`.
 2. In that CSS file, add the following code:

    .. code:: CSS

        .wy-table-responsive table td {
            white-space: normal !important;
        }
        .wy-table-responsive {
            overflow: visible !important;
        }

Alternatively, you can create a `docutil.conf` file with the following contents::

    [writers]
    option-limit=1


Linking to action groups
------------------------

As of version 0.2.0, action groups (e.g., "Optional arguments", "Required arguments", and subcommands) can be included in tables of contents and external links. The anchor name is the same as the title name (e.g., "Optional arguments"). In cases where titles are duplicated, as is often the case when subcommands are used, `_repeatX`, where `X` is a number, is prepended to duplicate anchor names to ensure that they can all be uniquely linked.
