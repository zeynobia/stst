import os
import sys
          
if __name__ == '__main__':
     
     targetfile=sys.argv[1]
     paraphfile=sys.argv[2]
     
     os.system('python3 calculateBleu.py '+paraphfile+' '+targetfile)
     os.system('python3 calculateRouge.py '+paraphfile+' '+targetfile)
     os.system('python3 calculateMeteor.py '+paraphfile+' '+targetfile+' '+'results/meteorResult.txt')
     os.system('python3 calculateErrorRate.py '+paraphfile+' '+targetfile+' '+'results/ErrorRateResult.txt')
