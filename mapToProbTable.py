import sys
from collections import defaultdict
import operator
import os
import re
import math
def getNNMap(growMap,  growdelim='-'):
  tokens=growMap.split( )
  tmptarget=''
  tmpsrc=''
  dictsrc=dict()
  for i in range(0,len(tokens)):
    cur=tokens[i].split(growdelim)
    if cur[0] not in dictsrc:
        if i!=len(tokens)-1:
           nex=tokens[i+1].split(growdelim)
           dictsrc[cur[0]]=cur[1]
        else:
           dictsrc[cur[0]]=cur[1]
    else:
        dictsrc[cur[0]]=dictsrc[cur[0]]+' '+cur[1]

  res = defaultdict(list)
  sortedDict=sorted(dictsrc.items())
  for key, val in sortedDict:
    res[val].append(key)
  dictres={}
  for key,val in res.items():
    if (len(val)>1):
        newval=''
        for i in range(len(val)-1):
            newval+=val[i]+' '
        newval+=val[len(val)-1]
        dictres[newval]=key
    else:
        dictres[val[0]]=key
  return dictres

if __name__ == "__main__":

   infile=sys.argv[1]
   growAlignfile=sys.argv[2]
   outfile=sys.argv[3]
   resultDir='results'
   if(os.path.exists(resultDir)==False):
      os.mkdir(resultDir)

   delim='|||'
   delimS=' ||| '
   growdelim='-'
   outfile=outfile
   outtmp=outfile+'.tmp'
   outfp=open(outtmp,'w',encoding='utf-8')
   inline = [line.strip() for line in open(infile,'r',encoding='utf-8')]
   growline=[line.strip() for line in open(growAlignfile,'r',encoding='utf-8')]
   dictlex=defaultdict(list)
   for i in range(len(growline)):
       growMap=growline[i].replace('\n','')
       dictres=getNNMap(growMap)
       text=inline[i].replace('\n','')
       text = re.sub(' +',' ',text)
       textparts=text.split(delim)
       i=i+1
       if(len(textparts)>=2):
         srctext=textparts[0]
         tgttext=textparts[1]
         srcparts=srctext.split()
         tgtparts=tgttext.split()
         for key,value in dictres.items():

           keys=key.split()
           values=value.split()
           if(len(keys)>1):
             tmpkey=''
             for kl in range(len(keys)):
               if( keys[kl].isdigit() and int(keys[kl])<len(srcparts)):
                  tmpkey+=srcparts[int(keys[kl])]+' '
             if(tmpkey!='' and value.isdigit() and int(value)<len(tgtparts)):
                tmpkey=tmpkey[:-1]
                dictlex[tmpkey].append(tgtparts[int(value)])

           elif(len(values)>1):
             tmpvalue=''
             for vl in range(len(values)):
                 if( values[vl].isdigit() and int(values[vl])<len(tgtparts)):
                    tmpvalue+=tgtparts[int(values[vl])]+' '
             if(tmpvalue!='' and key.isdigit() and int(key)<len(srcparts)):
                tmpvalue=tmpvalue[:-1]
                dictlex[srcparts[int(key)]].append(tmpvalue)
           else:
             if(key.isdigit() and value.isdigit() and int(key)<len(srcparts) and  int(value)<len(tgtparts)):  
                dictlex[srcparts[int(key)]].append(tgtparts[int(value)])
 
   epsilon=0.000000001 
   del growline[:]
   for key,value in dictlex.items():
     dictValueCnt = defaultdict(float) 
     for v in value: 
       dictValueCnt[v] += round(1/len(value),6)
     sorted_d = dict(sorted(dictValueCnt.items(), key=operator.itemgetter(1),reverse=True))
     for valueProb,prob in sorted_d.items():
        if(prob==0):
           prob=prob+epsilon      
        outfp.write(str(key)+delimS+str(valueProb)+' '+delimS+str(round(math.log10(prob),9))+'\n')


   outfp.close()
   os.system('sort '+outtmp+' > '+outfile)
   os.system('rm -f '+outtmp)

   

     