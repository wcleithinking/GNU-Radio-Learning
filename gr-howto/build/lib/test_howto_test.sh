#!/bin/sh
export VOLK_GENERIC=1
export GR_DONT_LOAD_PREFS=1
export srcdir=/home/wenchao/GitHub/gnuradio_files/gr-howto/lib
export PATH=/home/wenchao/GitHub/gnuradio_files/gr-howto/build/lib:$PATH
export LD_LIBRARY_PATH=/home/wenchao/GitHub/gnuradio_files/gr-howto/build/lib:$LD_LIBRARY_PATH
export PYTHONPATH=$PYTHONPATH
test-howto 
