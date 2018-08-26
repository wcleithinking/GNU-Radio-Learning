#!/usr/bin/env python

import sys
from gnuradio import gr
from gnuradio import audio
from gnuradio.eng_option import eng_option
from optparse import OptionParser

try:
    from gnuradio import analog
except ImportError:
    sys.stderr.write("Error: Program requires gr-analog.\n")
    sys.exit(1)

class my_top_block(gr.top_block):

    def __init__(self):
        gr.top_block.__init__(self)

        parser = OptionParser(option_class=eng_option)  # option parser
        parser.add_option("-O","--audio-output",type="string",default="",help="pcm output device name. E.g., hw:0,0 or /dev/dsp")   # add option
        parser.add_option("-r","--sample-rate",type="eng_float",default=48000,help="set sample rate to RATE (48000)")   # add option
        (options,args) = parser.parse_args()    # get the options
        if len(args) != 0:
            parser.print_help()
            raise SystemExit,1

        sample_rate = int(options.sample_rate)  # sample rate
        ampl = 0.5  # amplitude

        src0 = analog.sig_source_f(sample_rate,analog.GR_SIN_WAVE,350,ampl) # source 0
        src1 = analog.sig_source_f(sample_rate,analog.GR_SIN_WAVE,440,ampl) # source 1
        dst = audio.sink(sample_rate,options.audio_output)   # sink

        self.connect(src0,(dst,0))
        self.connect(src1,(dst,1))

if __name__ == '__main__':
    try:
        my_top_block().run()
    except KeyboardInterrupt:
        pass
