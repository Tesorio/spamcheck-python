Spamcheck-Python
================

|PyPI| |GitHub license|

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

.. |PyPI| image:: https://img.shields.io/pypi/v/spamcheck.svg
    :target: https://pypi.python.org/pypi/spamcheck
.. |GitHub license| image:: https://img.shields.io/badge/license-MIT-blue.svg
    :target: https://github.com/Tesorio/spamcheck-python/blob/master/LICENSE
