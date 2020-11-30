import kenlm
import os
import sys
from collections import defaultdict

def sort(tup):  
    tup.sort(key = lambda x: x[1],reverse=True)  
    return tup  
def loadLm(lmfile):
   model = kenlm.Model(lmfile)
   return model
def loadTm(filename,lm):
    delim=' ||| '
    dictRes=defaultdict(list)
    infp=open(filename,'r',encoding='utf-8')
    for line in infp:
        text=line.replace('\n','')
        parts=text.split(delim)
        if(len(parts)>2):
              tmScore=float(parts[2])
              lmScore=lm.score(parts[1])
              dictRes[parts[0]].append(tuple((parts[1], tmScore+ 0.1*lmScore) )) 
    return dictRes

def decode(tm,lm,sentence):
    result=""
    parts=sentence.split()
    i=0
    while (i<len(parts)):
       if (i<len(parts)-2 and (parts[i]+" "+parts[i+1]+" "+parts[i+2] in tm)):
           result+=sort(tm[parts[i]+" "+parts[i+1]+" "+parts[i+2]])[0][0]+" "
           i=i+2
       elif (i<len(parts)-1 and (parts[i]+" "+parts[i+1] in tm)):
           result+=sort(tm[parts[i]+" "+parts[i+1]])[0][0]+" "
           i=i+1
       elif (parts[i] in tm):
         result+=sort(tm[parts[i]])[0][0]+" "
       else:
        result+=parts[i]+" "
       i=i+1
    return ' '.join(result[:-1].split())
          
          
if __name__ == '__main__':
     
     testfile=sys.argv[1]
     paraphfile=sys.argv[2]
     tmfile=sys.argv[3]
     lm=loadLm('model/lm')
     tm=loadTm(tmfile,lm)
     infp=open(testfile,'r',encoding='utf-8')
     paraphfp=open(paraphfile,'w',encoding='utf-8')
     paraphfpExtended=open(paraphfile+'.extended','w',encoding='utf-8')
     for sentence in infp:
         text=sentence.replace('\n','')
         paraph=decode(tm,lm,text)
         paraphfp.write(paraph+'\n')
         paraphfpExtended.write(text+' ||| '+paraph+'\n') #sentence ||| paraph
     paraphfp.close()
     paraphfpExtended.close()

         
         
