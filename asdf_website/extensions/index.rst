.. _extensions:

Extensions
==========

In addition to the core schemas defined in the ASDF Standard, there are several additional schemas available as extensions. These schemas are based upon the schemas in :ref:`ASDF Standard <asdf-standard:asdf-standard>` and are packaged for use by the :ref:`asdf <asdf:asdf>` library.

.. toctree::
   :maxdepth: 1
   :hidden:
   
   asdf-transform-schemas
   asdf-coordinates-schemas
   asdf-wcs-schemas


Transforms
----------

The :doc:`ASDF Transform Schemas <asdf-transform-schemas>` define a set of schemas for serializing the models defined by :ref:`astropy.modeling <astropy:astropy-modeling>` for the ASDF file format. 

Coordinates
-----------

The :doc:`ASDF Coordinates Schemas <asdf-coordinates-schemas>` define a set of schemas for serializing the astronomical coordinate systems defined by :ref:`astropy.coordinates <astropy:astropy-coordinates>` for the ASDF file format.


WCS
---

The :doc:`ASDF WCS Schemas <asdf-wcs-schemas>` define a set of schemas for serializing WCS objects for the `GWCS <https://gwcs.readthedocs.io/en/latest/index.html#gwcs>`__ package.
