Spamcheck-Python
================

A simple Python wrapper for `Postmark’s Spamcheck API`_

Installation
------------

.. code:: bash

    $ pip install spamcheck

Usage
-----

.. code:: python

    import spamcheck

    result = spamcheck.check(your_email_content, report=True)
    score = result['score']
    report = result['report']

License
-------

This software is licensed under `MIT License`_

.. _Postmark’s Spamcheck API: http://spamcheck.postmarkapp.com/doc
.. _MIT License: https://github.com/Tesorio/spamcheck-python/blob/master/LICENSE