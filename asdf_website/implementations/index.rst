.. _implementations:

Implementations
===============

The ASDF specification is supported in several programming languages. See the table and links below
for more information about each implementation and what features are supported (``R/W`` = reads and writes).

The "Validation" column refers to support for validation of the YAML metadata against the associated
schemas.

=========================  ========     ===========  =========  ===========  ==========  ==========
Implementation             Metadata     Tags         Blocks     Compression  Validation  Extensions
=========================  ========     ===========  =========  ===========  ==========  ==========
`Python <asdf-python>`     R/W          R/W          R/W        R/W          True        True
`C <asdf-c>`               R/W          R/W          R/W        R/W                      True
`C++ <asdf-cpp>`           R/W          R/W [#cpp]_  R [#cpp]_  R/W [#cpp]_
`Java <asdf-java>`         R            R            R          R
`Julia <asdf-julia>`       R/W          R/W          R/W        R/W
=========================  ========     ===========  =========  ===========  ==========  ==========

.. rubric:: Footnotes

.. [#cpp] The c++ implementation only supports 1.2.0 core schemas and always compresses arrays.

.. toctree::
   :hidden:
   :maxdepth: 1

   Python <asdf-python.rst>
   C <asdf-c.rst>
   C++ <asdf-cpp.rst>
   Java <asdf-java.rst>
   Julia <asdf-julia.rst>
