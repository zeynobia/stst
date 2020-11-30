#pip3 install rouge
from rouge import FilesRouge
import sys
if __name__ == "__main__":

  hyp_file=sys.argv[1]
  ref_file= sys.argv[2] #directory or file
  files_rouge = FilesRouge()
  scores = files_rouge.get_scores(hyp_file, ref_file, avg=True, ignore_empty=True)
  print('Rouge1 F1Score: ', round(100*scores['rouge-1']['f'],2) ,'Rouge2 F1Score: ', round(100*scores['rouge-2']['f'],2)    )