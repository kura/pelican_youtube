===============
Pelican YouTube
===============

Pelican YouTube is a plugin to enabled you to embed YouTube videos in your pages
and articles.

Installation
============

To install pelican-youtube, simply install it from PyPI:

.. code-block:: bash

    $ pip install pelican-youtube

Then enabled it in your pelicanconf.py

.. code-block:: python

    PLUGINS = [
        # ...
        'pelican_youtube',
        # ...
    ]

Usage
=====

In your article or page, you simply need to add a line to embed you video.

.. code-block:: rst

    .. youtube:: VIDEO_ID

Which will result in:

.. code-block:: html

    <div class="youtube" align="left">
    <iframe width="420" height="315" src="https://www.youtube.com/embed/VIDEO_ID" frameborder="0"></iframe>
    </div>

Additional arguments
--------------------

You can also specify a `width`, `height` and `alignment`

.. code-block:: rst

	.. youtube:: 37818131
        :width: 800
        :height: 500
        :align: center

Which will result in:

.. code-block:: html

    <div class="youtube" align="center">
    <iframe width="800" height="500" src="https://www.youtube.com/embed/37818131" frameborder="0"></iframe>
    </div>

License
=======

`MIT`_ license.

.. _MIT: http://opensource.org/licenses/MIT