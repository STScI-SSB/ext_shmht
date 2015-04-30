#!/usr/bin/python
import os
from distutils.core import setup, Extension

#os.putenv("CFLAGS", "-g")

shmht = Extension('ext_shmht/_shmht',
        sources = ['shmht.c', 'hashtable.c']
)

setup(
    name            = 'ext_shmht',
# minimal changing of the version
    version         = '0.1',
# not to claim credit for another's work, nor to unfairly attribute my errors
    author          = '',   
    author_email    = '',
    description     = 'shared memory hash table with locking',
    license         = "BSD",
    keywords        = "shared memory hash table shmem mmap",
    url             = "http://github.com/stsci-sienkiew/pyshmht",
    ext_modules     = [shmht],
    packages        = ["ext_shmht"],
    long_description = """
An extended pyshmht - a simple hash table stored in an mmapped file

The basic access is vaguely dict like with the core capability being:

    h = ext_shmht.HashTable( filename, max_entries )
    h['key'] = 'value'
    v = h['key']

The table only uses strings for keys and values, but there is an
interface that uses an object serializer, such as json or some other
serializer that you provide.

There is a max length of key and value that are specified by defines
in the C code.

extensions include: 

- file locking for multi-threaded or multi-process access 
  n.b. do not use the same object in multiple threads - open the
  file again in each thread.

- a little bit of documentation

- a few test cases that run in Pandokia.  See http://ssb.stsci.edu/testing/pandokia/ or 'pip install pandokia'.


This is extended from pyshmht by felix021@gmail.com.  My intent is
to enhance the original for my needs, in a way that the changes may
someday make a reasonable pull request into the original.  It is a
fork with a new name because I don't have time for the coordination
with someone on the other side of the world right now.  (No kidding!
felix is in Shanghai and I am in Baltimore, separated by 160 degrees
longitude, or 10 to 11 time zones.)
""", 

)
