#python3 merge.py input/source.txt.pre input/target.txt.pre
import sys
import string
import re

def mergeTwoFile(infile1,infile2,outfile,delimiter):
 
    lines1 = [ line.strip() for line in open(infile1,'r',encoding='utf-8') ]
    lines2 = [ line.strip() for line in open(infile2,'r',encoding='utf-8') ]
    outfp=open(outfile,"w",encoding='utf-8')

    for i in range(0,len(lines1)):
        #if(lines1[i].strip()!='' and lines2[i].strip()!=''):        
           srctext = re.sub(' +',' ',lines1[i])
           tgttext = re.sub(' +',' ',lines2[i])
           outfp.write( srctext +delimiter+tgttext+"\n")
    outfp.close()

if __name__ == '__main__':
     
     infile1=sys.argv[1]
     infile2=sys.argv[2]
     outfile=sys.argv[3]
     delimiter=' ||| '
     mergeTwoFile(infile1,infile2,outfile,delimiter)