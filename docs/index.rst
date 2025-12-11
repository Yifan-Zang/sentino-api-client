Sentino API Client Documentation
=================================

A Python client for the Sentino Personality API. Analyze Big Five personality traits from text.

.. toctree::
   :maxdepth: 2
   :caption: Contents:

   installation
   quickstart
   api

Installation
============

.. code-block:: bash

   pip install sentino-api

Get your API token from info@sentino.org

Quick Start
===========

.. code-block:: python

   from sentino_api import SentinoClient

   # Initialize client
   client = SentinoClient("your_api_token")

   # Analyze text
   text = "I love meeting new people and going to parties."
   result = client.score_text(text, inventories=["big5"])

   # Convert to DataFrame
   df = client.results_to_dataframe(result)
   print(df)

API Reference
=============

.. automodule:: sentino_api.client
   :members:
   :undoc-members:
   :show-inheritance:

Indices and tables
==================

* :ref:`genindex`
* :ref:`modindex`
* :ref:`search`

