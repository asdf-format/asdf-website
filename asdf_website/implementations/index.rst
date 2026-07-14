.. _implementations:

Implementations
===============

The ASDF specification is supported in several programming languages. See the table and links below
for more information about each implementation and what features are supported (``R/W`` = reads and writes).

==============  ========     ===========  =========  ===========  ==========  ==========
Implementation  Metadata     Tags         Blocks     Compression  Validation  Extensions
==============  ========     ===========  =========  ===========  ==========  ==========
python          R/W          R/W          R/W        R/W          True        True
c++             R/W          R/W [#cpp]_  R [#cpp]_  R/W [#cpp]_
java            R            R            R          R
julia           R/W          R/W          R/W        R/W
==============  ========     ===========  =========  ===========  ==========  ==========

.. toctree::
   :maxdepth: 1

   python <asdf-python.rst>
   c++ <asdf-cpp.rst>
   java <asdf-java.rst>
   julia <asdf-julia.rst>

.. rubric:: Footnotes

.. [#cpp] The c++ implementation only supports 1.2.0 core schemas and always compresses arrays.
