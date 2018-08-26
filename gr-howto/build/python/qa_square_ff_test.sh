#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/wenchao/GitHub/gnuradio_files/gr-howto/python
export PATH=/home/wenchao/GitHub/gnuradio_files/gr-howto/build/python:$PATH
export LD_LIBRARY_PATH=/home/wenchao/GitHub/gnuradio_files/gr-howto/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=/home/wenchao/GitHub/gnuradio_files/gr-howto/build/swig:$PYTHONPATH
/usr/bin/python2 /home/wenchao/GitHub/gnuradio_files/gr-howto/python/qa_square_ff.py 
