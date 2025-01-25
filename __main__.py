import re
import sys
from rttobin import rttobin


if __name__ == '__main__':
    filename = sys.argv[1]

    binaries = rttobin(filename)

    # bintosim(binaries, romfile)
   
   # py . brincanagem.rt