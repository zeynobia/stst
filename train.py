import os
import sys
if __name__ == '__main__':
     
     sourcefile=sys.argv[1]
     targetfile=sys.argv[2]
     mergefile='input/merge.txt'
     ord=3
     os.system('python3 merge.py '+sourcefile+' '+targetfile+' '+mergefile)
     os.system('fast_align/build/fast_align -i '+mergefile+' -d -o -v > model/forward.map')
     os.system('fast_align/build/fast_align -i '+mergefile+' -d -o -v -r > model/reverse.map')
     os.system('fast_align/build/atools -i model/forward.map -j model/reverse.map -c grow-diag-final-and > model/grow.map')
     os.system('python3 mapToProbTable.py '+mergefile+' model/grow.map model/tm')
     os.system('kenlm/build/bin/lmplz -o '+str(ord)+' -S 5% --discount_fallback '+' < '+targetfile+' > '+'model/lm')