Block Diagrammer (BD)
=====================

**Simple Block Diagram Generator**

.. code-block:: json

   "diagram": {
     "lines": [
       "| A | ---> | D | <-------> | F |",
       "|   | <------------------> |   | <----- | I |",
       "|   | ---> | E | <-------> |   |",
       "           |   | <-------- | G |",
       "| B | <--> |   | <-------> | H | <----> | J |",
       "|   | -------------------> |   |",
       "| C | -------------------> |   | -----> | K |"
     ]
   }

Table of Contents
-----------------

*   `Overview`_
*   `Key Benefits`_
*   `Key Features`_
*   `Known Limitations`_
*   `Installation`_
*   `Usage`_
*   `Documentation`_
*   `Contributing`_

Overview
--------

Creating block diagrams using a drawing tool such as Microsoft Visio can result in complicated diagrams.

Block Diagram Philosopy
-----------------------

#. Only have enough information
#. Make it simple to create
#. Consistent block diagrams
#. Use text as the source

Block Diagrammer trades the flexibility of drawing tools with a set of simple rules.
These rules provide a framework to generate diagrams.

#. Use a grid based system to describe block diagram
#. Nodes are in even columns
#. Arrows are in odd columns
#. Nodes can stack
#. Arrows are only horizontal

Key Benefits
------------

* Simplifies block diagram creation
* Text based input can be source controlled
* Rendered output can be used in documentation

Key Features
------------

* Command line tool
* JSON for input

Installation
------------

You can get the latest released version of Block Diagrammer via **pip**.

.. code-block:: bash

    pip install block-diagrammer

The latest development version can be cloned...

.. code-block:: bash

    git clone https://github.com/jeremiah-c-leary/block_diagrammer.git

...and then installed locally...

.. code-block:: bash

    python setup.py install

Usage
-----

Block Diagrammer can be invoked with:

.. code-block:: bash

   $ bd render svg <config_file>

Here is an example output running against a test file:

.. image:: https://github.com/jeremiah-c-leary/vhdl-style-guide/blob/master/docs/img/fixing_single_file.gif

Documentation
-------------

All documentation for Block Diagrammer is hosted at `read-the-docs <http://block_diagrammer-style-guide.readthedocs.io/en/latest/index.html>`_.

Contributing
------------

I welcome any contributions to this project.
No matter how small or large.

There are several ways to contribute:

* Bug reports
* Code base improvements
* Feature requests
* Pull requests
