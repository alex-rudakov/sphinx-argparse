Miscellaneous
=============

Text wrapping in argument tables
--------------------------------

A common issue with the default html output is that the table within which options are displayed is designed such that the option descriptions are each held on one line. Any even remotely lengthy description then causes the viewer to need to scroll left/right to view the entire text. This is typically undesirable and the fix is described fully `here <http://rackerlabs.github.io/docs-rackspace/tools/rtd-tables.html>`_.

The short synopsis is below:

 1. Create a new CSS file (likely under `_static`) and point to it in `html_static_path` and `html_context` (or a template in the `templates_path`) in `conf.py`.
 2. In that CSS file, add the following code::

.. code:: CSS

    .wy-table-responsive table td {
        white-space: normal !important;
    }
    .wy-table-responsive {
        overflow: visible !important;
    }
