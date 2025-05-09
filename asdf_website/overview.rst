.. _overview:

Overview
========

Introduction
------------

**What is ASDF?**

The Advanced Scientific Data Format (ASDF, pronounced *"Az-diff"*) is a next-generation interchange format for scientific data.

*Key Features*

* Hierarchical, human-readable metadata, made up of basic and rich data types.

* Efficient binary array storage that can optionally be compressed or memory mapped.

* Content validation using schemas.

* Designed for extensibility.

* Files and contents are versioned to maintain backwards compatibility.

* Built on top of industry standards (`YAML <http://www.yaml.org>`__ and `JSON Schema <http://www.json-schema.org>`__)


**What about FITS?**

The Flexible Image Transport System (FITS) has been the de facto standard for storing and exchanging astronomical data for decades, but it is beginning to show its age. Developed in the late 1970s, the FITS authors made a number of implementation choices that, while common at the time, are now seen to limit its utility for the needs of modern science. As astronomy moves into a more varied set of data product types (data models) with richer and more complex metadata, FITS is being pushed to its breaking point. The issues with FITS are outlined in great detail in [Thomas2015]_.

**What makes ASDF unique?**

Newer formats, such as `VOTable
<http://www.ivoa.net/documents/VOTable/>`__ have partially addressed the problem of richer, more structured metadata, by using tree structures rather than flat key/value pairs. However, those text-based formats are unsuitable for storing large amounts of binary data. On the other end of the spectrum, formats such as `HDF5
<http://www.hdfgroup.org/HDF5/>`__ address problems with large data sets and distributed computing, but don't really address the metadata needs of an interchange format. ASDF aims to exist in the same middle ground that made FITS so successful, by being a hybrid text and binary format: containing human editable metadata for interchange, and raw binary data that is fast to load and use. Unlike FITS, the metadata is highly structured and is designed up-front for extensibility.

*Incorporated standards*

The ASDF format is built on top of a number of existing standards:

- `YAML 1.1 <http://yaml.org/spec/1.1/>`__

- JSON Schema Draft 4:

  - `Core <http://tools.ietf.org/html/draft-zyp-json-schema-04>`__

  - `Validation
    <http://tools.ietf.org/html/draft-fge-json-schema-validation-00>`__

  - `Hyper-Schema
    <http://tools.ietf.org/html/draft-luff-json-hyper-schema-00>`__

- `JSON Pointer <http://tools.ietf.org/html/rfc6901>`__

- `Semantic Versioning 2.0.0 <http://semver.org/spec/v2.0.0.html>`__

- `VOUnits (Units in the VO)
  <http://www.ivoa.net/documents/VOUnits/index.html>`__

- `Zlib Deflate compression <http://www.zlib.net/feldspar.html>`__

**Limitations**

ASDF is primarily intended as an interchange format for delivering products from instruments to scientists or between scientists. While it is reasonably efficient to work with and transfer, it may not be optimal for direct use on large data sets in distributed and high performance computing environments. That is explicitly not a goal of the ASDF standard, as those requirements can sometimes be at odds with the needs of an interchange format. ASDF still has a place in those environments as a delivery mechanism, even if it ultimately is not the actual format on which the computing is performed.



ASDF Standard
-------------

The :doc:`ASDF Standard <standard/index>` prescribes implementation standards and requirements for creating, editing and reading files written in the Advanced Scientific Data Format (asdf). This is a good place to start if you want to understand more about the file layout, tree structure, and core schema requirements of ASDF.


Extensions: Optional Schemas
----------------------------

In addition to the core schemas defined by the ASDF Standard, there are several optional schemas that can be used as :doc:`extensions <extensions/index>`.

- :doc:`transform <extensions/asdf-transform-schemas>`
- :doc:`coordinates <extensions/asdf-coordinates-schemas>`
- :doc:`wcs <extensions/asdf-wcs-schemas>`


Applications
------------

The ASDF standard is being developed concurrently with a reference implementation written in Python. There are two prototype implementations for C++ and Julia. Neither is currently feature-complete but provide enough functionality to read and write ASDF files.

- :doc:`python <applications/asdf-python>`
- :doc:`C++ <applications/asdf-cpp>`
- :doc:`Julia <applications/asdf-julia>` 


Tutorials/Workshops
-------------------

- :doc:`tutorials/tutorial1`
- :doc:`tutorials/tutorial2`


Community
---------

- Discussions: https://github.com/asdf-format/asdf/discussions
- Community calls: https://github.com/asdf-format/community-calls/

*Mailing Lists*

- `ASDF Users <https://groups.google.com/forum/#!forum/asdf-users>`__
- `ASDF Developers <https://groups.google.com/forum/#!forum/asdf-developers>`__


References
----------

.. [Thomas2015] Thomas, B., Jenness. T. et al. (2015).
   Learning from FITS: Limitations in use in modern astronomical research.
   *Astronomy and Computing*, 12: 133-145.
   `doi:10.1016/j.ascom.2015.01.009 <https://doi.org/10.1016/j.ascom.2015.01.009>`__
