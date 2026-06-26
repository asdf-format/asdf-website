.. _asdf_fits:

ASDF for FITS users
===================

ASDF was developed for use in astronomy [GreenField2015]_. For users familiar with FITS it may be
helpful to make some comparisons between the two formats to help understand ASDF.

Data models
-----------

The FITS standard defines:

- a file format: a description of how bytes are encoded and organized on disk
- a data model: requirements and descriptions of how data is organized and interrelated

The :ref`ASDF specification <asdf-standard:asdf-standard>` defines:

- a file format
- a framework and tooling that can be used to define data models

Both describe a file format, however the ASDF specification does not define a singular data model. This
is an intentional decision that allows ASDF to be adapted to different datasets and fields of
study including but not limited to astronomy.

It is important for users to be aware of this distinction when applying FITS experience
to working with ASDF files. For example, the ASDF specification does not describe a ``TELESCOP`` keyword
that can contain the name of the telescope. Instead, ASDF provides a framework that uses
:ref:`tags <asdf-standard:tags>` and :ref:`schemas <asdf-standard:asdf-schemas>` with which a user can
define a data model. Using this framework a user may define a
property that can contain the name of the telescope, include a description of that property
and optionally constrain the possible values or types. For an example, see the
`telescope metadata schema for the Roman mission <https://rad.readthedocs.io/en/0.30.0/generated/schemas/meta/telescope-1.0.0.html#meta-telescope-1-0-0>`__.
Practically, users should consult the documentation
and schemas provided by the data model designers for questions about metadata organization instead
of expecting that the ASDF specification will provide answers. This is similar to
working with FITS files as often handling real data requires understanding the keywords and data
organization specific to a data set or mission (which has defined their own data model that extends FITS).
One key difference is that ASDF provides tooling for data model designers to document and
enforce these decisions.

.. note::

   Previously the ASDF specification was referred to as the ASDF standard. This led to confusion
   when users expected that the specification would contain a singular data model definitiion
   like the FITS standard. There is an (ongoing) effort to use the name specification instead
   of standard to avoid this confusion. There may be some documents that refer the the
   "ASDF standard" and users should be aware that this is the same thing as the "ASDF specification".

File format
-----------

Both ASDF and FITS are file formats that define how bytes are encoded and organized on disk.

FITS files are composed of 1 or more Header and Data Units (HDU) often referred to as "extensions"
with each HDU consisting of:

- a "header" containing a list of of "keyword records" each with a key and optional value.
- optional "data"

This results in a "flat" layout made up of a list of HDUs each with a list of header keyword records (or
keywords for short).

ASDF files are composed of:

- a "tree" containing a flat or nested description of the file contents
- optionally 1 or more binary "blocks"

Data and Metadata
^^^^^^^^^^^^^^^^^

One difference to note is how the two formats handle data and metadata. ASDF files contain a "tree" which
can contain both data and metadata. FITS files contain one data array per HDU and metadata is contained
in keywords. Practically this means that a user wanting to access the metadata for a file will
inspect the ASDF tree. The same is true for the data in the file, it is accessed via the tree.
Distinguising data vs metadata for an ASDF file requires understanding the data model used by
the creator of the file and the tags and schemas should be consulted.

This difference also can lead to some confusion when FITS terminology is applied to ASDF files.
ASDF does not have "keywords" in the FITS sense. Instead the data and metadata are accessed
via the ASDF tree which can be thought of as an object (or mapping of key value pairs). As values
can themselves be objects or sequences (lists) it is often helpful to refer to the "path"
of the value within an ASDF file using either dot-notation ("roman.meta.wcs") or slash-notation
("/roman/meta/wcs") depending on the ASDF implementation.

Another term that can lead to confusion is "extension". For FITS "extension" is often used to refer
to a HDU within a FITS file. As noted above, for ASDF data and metadata are stored within the tree
so there is no equivalent to the term "extension" (in the FITS sense). Confusion often arises
since ASDF uses the term "extension" to refer to how data model designers can use the ASDF
specification framework to define how an ASDF file is organized (the data model). For example, the
`Roman Datamodels <https://roman-datamodels.readthedocs.io/en/latest/>`__ extension (in the
ASDF sense) contains tags, schemas and logic that define the data model for the Roman mission. 
Users should be aware of this difference and know that an ASDF extension (a description of
a data model) refers to something quite different than a FITS extension (the data within a file).

File structure
^^^^^^^^^^^^^^

FITS has a "flat" structure whereas ASDF files can be flat or nested (heirarchically organized).
ASDF files can use this nesting to logically group information and the structures and relationships
can be defined using the data model framework. When working with ASDF files it is often helpful
to think of them as an arbitrary nested collection of objects (a tree) instead of a linear collection
of items all corresponding to one object (the FITS data model). ASDF was designed to allow
multiple data models per file to accomodate multi-detector and/or multi-observation data. These
data models can themselves be nested (a data model for an observation might contain a data model
for a catalog of sources which itself might contain a data model for tabular data). Users and
application developers may find it helpful to ask what level of detail is of interest.
If a data model is of interest (tabular data) for a specific application one should consider:

- How will the tabular data be found? Will the entire file be searched, the user provide a path to
  the tabular data within the ASDF tree, and/or is the some expectation about the tabular data
  location (for instance a table nested within a data model for a mission)? 
- How will files with multiple instances of tabular data be handled?

Much of the interaction with FITS files is guided by the data model described in the FITS
standard and not by the file format. Since ASDF files allow greater flexibility in data model
usage it is often helpful to focus on the data model of interest and less on the file format.

Data types
^^^^^^^^^^

FITS supports scalar values within keyword records and data arrays (and tables) in HDUs. Keyword
records can have 8 ASCII character length names and a value that can be one of the handful of
scalar data types defined in the standard. HDUs can contain either array or tabular data.
Additionally, the standard defines a collection of keywords and HDUs that combined represent
a world coordinate system (WCS). This collection of items and specification for how they are
related can be thought of as a data model for a WCS which is based off the fundemental types
in FITS (keywords and data arrays/tables).

ASDF supports scalar and array values within the tree. Through the ASDF data model framework
these fundemental types can be combined to construct more complex data models. The most common
WCS data model used for ASDF is provided by `gwcs <https://gwcs.readthedocs.io/en/latest/>`__
which uses the `wcs schema <https://www.asdf-format.org/projects/asdf-wcs-schemas/en/latest/generated/gwcs/wcs-1.1.0.html>`__. ASDF files that contain a WCS will have a node (location in the ASDF tree) that
is tagged with the wcs tag:

.. code-block:: yaml
   wcs: !<tag:stsci.edu:gwcs/wcs-1.4.0>
     ...

ASDF imposes no restriction on where this WCS is located and instead allows data model
designers to add a restriction for thier particular data model. A user or application developer
interested in using a WCS within an ASDF file should first consult any defined data model for
the ASDF file (by inspecting tags within the file and consulting the associated data model
documentation and schemas).

Summary
-------

ASDF and FITS are both file formats. However the FITS standard defines a singular data model
that is specific to astronomy. The ASDF specification defines a framework that allows
users to define domain-specifc data models. FITS files are flat with a limited number of standard
data types. ASDF can be flat or nested and extensible allowing users to define custom types
(data models) that can be arbitrarily nested.

References
----------

.. [Greenfield2015] Greenfield, P., Droettboom, M., Bray, E. (2015).
   ASDF: A new data format for astronomy.
   *Astronomy and Computing*, 12: 240-251.
   `doi.org/10.1016/j.ascom.2015.06.004 <https://doi.org/10.1016/j.ascom.2015.06.004>`__
