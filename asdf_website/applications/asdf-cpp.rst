.. _asdf-cpp:

ASDF for C++
============

`asdf-cxx <https://github.com/eschnett/asdf-cxx>`__ is an open-source prototype implementation of the ASDF Standard in C++ authored by `Erik Schnetter <https://github.com/eschnett>`__. Although not yet feature-complete, the library supports ASDF's core capabilities of storing metadata in YAML and serializing n-dimensional numerical data arrays.


Installation Requirements
-------------------------

- C++ 17-capable C++ compiler (tested with `Clang <https://clang.llvm.org/>`__ and `GCC <https://gcc.gnu.org/>`__)
- `cmake <https://cmake.org/>`__
- `pkg-config <https://www.freedesktop.org/wiki/Software/pkg-config/>`__
- `yaml-cpp <https://github.com/jbeder/yaml-cpp>`__

**Optional libraries for compression and MD5:**

- `OpenSSL <https://www.openssl.org/>`__ (MD5 checksums)
- `bzip2 <http://bzip.org/>`__ (compression)
- `c-blosc <https://www.blosc.org/>`__ (compression)
- `c-blosc2 <https://www.blosc.org/>`__ (compression)
- `lz4 <https://lz4.org/>`__ (compression)
- `zlib <http://zlib.net/>`__ (compression)
- `zstd <https://github.com/facebook/zstd>`__ (compression)


Build Instructions
------------------

.. code-block:: bash
    
    $ git clone https://github.com/eschnett/asdf-cxx
    $ cd asdf-cxx
    $ cmake -B build -S .
    $ cmake --build build
    $ ctest --test-dir build
    $ cmake --install build
