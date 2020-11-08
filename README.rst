.. image:: docs/images/logo_swtoolkit.png
   :width: 300

.. image:: https://img.shields.io/pypi/v/swtoolkit.svg
        :target: https://pypi.python.org/pypi/swtoolkit

.. image:: https://img.shields.io/travis/Glutenberg/swtoolkit.svg
        :target: https://travis-ci.com/Glutenberg/swtoolkit

.. image:: https://readthedocs.org/projects/swtoolkit/badge/?version=latest
        :target: https://swtoolkit.readthedocs.io/en/latest/?badge=latest
        :alt: Documentation Status

.. image:: docs/images/intro_code.png
   :width: 600

SW ToolKit is a SolidWorks Toolkit for Python
=============================================
**SW ToolKit** allows you to leverage Python to quickly develop powerful scripts and programs to automate your SolidWorks workflow.

* Free software: MIT license
* Documentation: https://swtoolkit.readthedocs.io.

Use Cases:
----------
* Automate custom property reading and writing to aid in Bill of Material preparation
* Bulk collect model data for design and project analysis.
* Link dimensions and variables to calculated values in scripts and interactive python notebooks

Installation
------------
.. code-block:: bash

        pip install swtoolkit

Usage
-----
.. code-block:: python

        from swtoolkit.api.solidworks import SolidWorks
        
Interacting with SolidWorks
^^^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

        sw = SolidWorks() # Creates Solidworks object
        sw.process_id
        sw.visible = True # Set and get window visibility

        model = sw.get_model() # Returns the active model document
        models = sw.get_documents() # Returns all documents open in the SolidWorks instance

Interacting with Models
^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

        model.title # Returns the model documents title
        features = model.feature_manager.get_features() # Returns a list of features in the model

Interacting with Features
^^^^^^^^^^^^^^^^^^^^^^^^^
.. code-block:: python

        feature = features[0] # Returns the first feature in the model
        feature.name 
        feature.id_

.. Features
.. --------
.. Future
.. ^^^^^^

Credits
-------

This package was created with Cookiecutter_ and the `audreyr/cookiecutter-pypackage`_ project template.

.. _Cookiecutter: https://github.com/audreyr/cookiecutter
.. _`audreyr/cookiecutter-pypackage`: https://github.com/audreyr/cookiecutter-pypackage
