import sys
import string
import re

def removePunction(content):
    table = str.maketrans(string.punctuation, ' '*len(string.punctuation))
    return content.translate(table)

def toLowercase(text):
    text = re.sub(r"I", "ı", text)
    text = re.sub(r"İ", "i", text)
    text = text.lower()
    return text

def preprocess(content):
    text=removePunction(content)
    return ' '.join(toLowercase(text).split())

if __name__ == '__main__':
     
     infile=sys.argv[1]
     outfile=sys.argv[2]
     infp=open(infile,'r',encoding='utf-8')
     outfp=open(outfile,'w',encoding='utf-8')
     for line in infp:
         text=line.replace('\n','')
         textpre=preprocess(text)
         outfp.write(textpre+'\n')

     outfp.close()
    

     