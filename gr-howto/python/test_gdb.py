""" Testing GDB, yay """

import os
from gnuradio import gr
#import howto

class SquareThat(gr.top_block):
    def __init__(self):
        gr.top_block.__init__(self, name="square that")
        self.src = gr.vector_source_f((1,2,3,4,)*5)
        self.sqr = howto.square2_ff()
        self.sink = gr.vector_sink_f()
        self.connect(self.src,self.sqr,self.sink)

def main():
    """ go, go, go """
    top_block = SquareThat()
    top_block.run()

if __name__ == "__main__":
    print("Blocked waiting for GDB attach (pid = %d)" % (os.getpid(),))
    raw_input("Press Enter to continue: ")
    main()