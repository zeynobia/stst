import os
import sys
import re

if __name__ == "__main__":

  hyp_file=sys.argv[1]
  ref_file= sys.argv[2] #directory or file
  resultMeteorFile=sys.argv[3]
  os.system('java -jar meteor-1.5.jar '+hyp_file+' '+ref_file+' -l other'+' > '+resultMeteorFile)
  with open(resultMeteorFile) as file:
     resultsMeteor=  [line.strip() for line in file]
  lenArr=len(resultsMeteor)
  finalScoreStr=resultsMeteor[lenArr-1].replace('Final score:',' ').strip()
  roundScore=round(100*float(finalScoreStr),2)
  f1ScoreStr=resultsMeteor[lenArr-5].replace('f1:',' ').strip()
  roundf1Score=round(100*float(f1ScoreStr),2)

  print('MeteorF1: ',roundf1Score,' MeteorFinal: ',roundScore)
  
  

