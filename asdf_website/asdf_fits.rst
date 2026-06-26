.. _asdf_fits:

ASDF for FITS users
===================

ASDF was developed for use in astronomy [Greenfield2015]_. For users familiar with the Flexible Image Transport System (FITS), 
this page offers a comparison between the two formats.

Data models
-----------

The FITS standard defines:

- a file format: a description of how bytes are encoded and organized
- a data model: requirements and descriptions of how data is organized and interrelated

The :ref:`ASDF specification <asdf-standard:asdf-standard>` defines:

- a file format
- a framework and tooling that can be used to define data models

Both describe a file format, however the ASDF specification does not define a singular data model. This
is an intentional decision that allows ASDF to be adapted to different datasets and fields of
study including but not limited to astronomy.

It is important for users to be aware of this distinction when applying FITS experience
to working with ASDF files. The ASDF specification alone does not define how data is organized
within an ASDF file.

For example, the FITS standard describes the optional ``TELESCOP`` keyword that, if present, contains the name of the telescope used to acquire the data. 
The ASDF specification does not define an equivalent of ``TELESCOP``.
Instead, ASDF provides a framework using :ref:`tags <asdf-standard:tags>` and
:ref:`schemas <asdf-standard:asdf-schemas>` that a data model designer can use to define how
data will be organized. An equivalent of ``TELESCOP`` could be defined using this framework similar
to how for Roman data there is a `telescope metadata schema <https://rad.readthedocs.io/en/0.30.0/generated/schemas/meta/telescope-1.0.0.html#meta-telescope-1-0-0>`__
which describes and constrains the "telescope" value that is referenced in other
`Roman Datamodels <https://roman-datamodels.readthedocs.io/en/latest/>`__.

Practically, users should consult the documentation
and schemas provided by the data model designers for questions about metadata organization instead
of expecting the ASDF specification to provide answers. This is similar to
working with FITS files, as often handling real data requires understanding the keyword and data
organization specific to a data set or mission (which has defined their own data model that extends FITS).
One key difference is that ASDF provides tooling for data model designers to document and
enforce these decisions.

.. note::

   Previously, documents referred to the ASDF specification as the "ASDF standard".
   This led to confusion when users expected that the specification would contain a singular data model definition similar to the FITS standard.
   There is an (ongoing) effort to replace usage of the word "standard" with "specification" in new documentation, in order to reduce this confusion.

File format
-----------

Both ASDF and FITS are file formats, defining how bytes are encoded and organized in a file on disk.

FITS files are comprised of 1 or more Header and Data Units (HDUs), often referred to as "extensions". Each HDU consists of:

- a "header" containing a list of "keywords" (called "keyword records" in the FITS standard) with names and optional values
- optional "data"

This results in a "flat" layout made up of a list of HDUs each with a list of header keyword records (or
keywords for short).

ASDF files are composed of:

- a :ref:`tree-structured representation of data and metadata (an "ASDF tree") <asdf-standard:tree>` 
- optionally, one or more :ref`binary blocks <asdf-standard:block>` of data

Data and metadata
^^^^^^^^^^^^^^^^^

One difference to note is how the two formats handle data and metadata. ASDF files contain a
:ref:`tree <asdf-standard:tree>` which can contain both data and metadata at arbitrary depth of nodes (locations in the ASDF tree). FITS files contain
one data array per HDU and metadata in keywords records. Practically, a user wanting to access
the metadata in an ASDF file will inspect the ASDF tree. The same is true for the data in the ASDF file which is also
 accessed via the tree. Distinguishing data vs metadata for an ASDF file requires understanding the
data model (including the tags and schemas) used by the creator of the file.

This difference can lead to some confusion when FITS terminology is applied to ASDF files.
ASDF does not have "keywords" in the FITS sense. Instead, the data and metadata are accessed
via the ASDF tree which can be thought of as an object (or mapping of key value pairs). As values
can themselves be objects, sequences (lists) or scalar values it is often helpful to refer to the "path"
of the value within an ASDF file using either dot-notation ("roman.meta.wcs") or slash-notation
("/roman/meta/wcs") depending on the ASDF implementation.

Another term that can lead to confusion is "extension". For FITS, "extension" is often used to refer
to a HDU within a FITS file. As noted above, ASDF data and metadata are stored within the tree
so there is no equivalent to the term "extension" (in the FITS sense). Confusion often arises
since ASDF uses the term "extension" to refer to how data model designers can use the ASDF
specification framework to define how an ASDF file is organized (the data model). For example, the
`Roman Datamodels <https://roman-datamodels.readthedocs.io/en/latest/>`__ ASDF extension contains tags, schemas and logic that define the data model for the Roman Telescope mission. 
Users should be aware of this difference and know that an ASDF extension (a description of
a data model) refers to something quite different than a FITS extension (the data within a file, an HDU).

File structure
^^^^^^^^^^^^^^

FITS has a "flat" structure, whereas ASDF files can be flat or nested (hierarchically organized).
ASDF files can use this nesting to logically group information.
When working with ASDF files it is often helpful 
to think of them as an arbitrary nested collection of objects (a tree) instead of a linear collection
of items all corresponding to one object (the FITS data model). 
This flexibility may be constrained for a particular data model, which may enforce a particular structure and contents.
ASDF was designed to allow
multiple data models per file to accomodate multi-detector and/or multi-observation data. These
data models can themselves be nested (a data model for an observation might contain a data model
for a catalog of sources, which itself might contain a data model for tabular data). Users and
application developers may find it helpful to ask what level of detail is of interest.
If a data model is of interest (for example tabular data) for a specific application consider:

- How will the tabular data be found? Will the entire file be searched, or will the user provide a path to the tabular data within the ASDF tree?
- Is there some expectation about the location of the data? For instance, is the data nested within a data model for a particular mission? 
- How will files with multiple instances of tabular data be handled?

Much of the interaction with FITS files is guided by the data model described in the FITS
standard and not by the file format. Since ASDF files allow greater flexibility in data models, 
it is often helpful to focus on the data model of interest and less on the file format.

Data types
^^^^^^^^^^

FITS supports scalar values within keyword records and data arrays (and tables) in HDUs. Keyword
records can have 8 ASCII character length names, and a value is limited to one of the handful of
scalar data types defined by the FITS standard. HDUs can contain either array or tabular data.
Additionally, the standard defines a collection of keywords and HDUs that combined represent
a world coordinate system (WCS). This collection of items and specification for how they are
related can be thought of as a data model for a WCS, built out of the fundamental types
defined in the FITS standard.

ASDF supports scalar and array values within the tree. Through the ASDF data model framework
these fundemental types can be combined to construct more complex data models. For example, the most common
WCS data model used for ASDF is provided by `gwcs <https://gwcs.readthedocs.io/en/latest/>`__
which uses the `wcs schema <https://www.asdf-format.org/projects/asdf-wcs-schemas/en/latest/generated/gwcs/wcs-1.1.0.html>`__. A WCS in an ASDF file has the following tag:

.. code-block:: yaml
   wcs: !<tag:stsci.edu:gwcs/wcs-1.4.0>
     ...

ASDF imposes no restriction on where this WCS is located and instead allows data model
designers to add restrictions for their particular data model. A user or application developer
interested in using a WCS from an ASDF file should first consult any defined data model used
in the ASDF file (by inspecting tags within the file and consulting the associated data model
documentation and schemas).

Versioning
----------

The FITS data model has no provision for versioning. ASDF uses versioning extensively:

- the version number of the file format is encoded in every file
- versions of tags and schemas used to describe data models are encoded in ASDF files
- ASDF files contain a record of versions of extensions used to produce the file

See the ASDF specification for more information about :ref:`versioning <asdf-standard:versioning-conventions>`.
Users should consider the versions of software and extensions that they have installed when
working with ASDF files. These versions allow ASDF and the data models defined using the extension
framework to adapt and improve over time. Application developers and data model designers should consider
versioning early in the development process to plan for version changes to the above items and
how those changes might be presented to the user.

Summary
-------

ASDF and FITS are both file formats. However the FITS standard defines a singular unversioned data model
that is specific to astronomy. The ASDF specification defines a framework that allows
users to define domain-specifc versioned data models. FITS files are flat with a limited number of standard
data types. ASDF can be flat or nested and contain both basic types and custom data models
defined using tags and schemas (in extensions).

References
----------

.. [Greenfield2015] Greenfield, P., Droettboom, M., Bray, E. (2015).
   ASDF: A new data format for astronomy.
   *Astronomy and Computing*, 12: 240-251.
   `doi.org/10.1016/j.ascom.2015.06.004 <https://doi.org/10.1016/j.ascom.2015.06.004>`__
