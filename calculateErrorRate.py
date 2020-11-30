#pip3 install pyter3
import pyter
import codecs
import sys
import os

def read_files(hyp, ref):
    references = []
    reference_file = codecs.open(ref, 'r', 'utf-8')
    references=reference_file.read().splitlines()
    hypothesis_file = codecs.open(hyp, 'r', 'utf-8')
    hypothesis = hypothesis_file.read().splitlines()
    return hypothesis, references

if __name__ == "__main__":

    hyp_file=sys.argv[1]
    ref_file= sys.argv[2]
    outfile= sys.argv[3]
    resultDir='results'
    if (os.path.exists(resultDir)==False):
     os.system('mkdir '+resultDir)

 
    outfp=open(outfile,'w',encoding='utf-8')

    hyps, refs = read_files(hyp_file,  ref_file)
    totalLen=0
    totalErrorLen=0

    accuracyDict={}
    for i in range(len(refs)):
        ref=refs[i].split()
        hyp=hyps[i].split()
        lenRef=len(ref)
        totalLen+=lenRef
        if((lenRef)>0):
           errorRate=pyter.ter(hyp, ref)
           errorLen=errorRate*lenRef
           accuracyDict[i+1]=(1.0-errorRate)
           totalErrorLen+=errorLen

    avgErrorRate=totalErrorLen/totalLen
    correctLen=totalLen-totalErrorLen
    avgErrorRound=round(100*avgErrorRate,2)
    avgAccuracy=round(100 *(1.0-avgErrorRate),2)
    
    print('Word Error Rate: ',avgErrorRound, ' Word Accuracy: ',avgAccuracy)
    sortedDict=sorted(accuracyDict.items(), key=lambda x: x[1])
    #print(sortedDict)
    for elem in  sortedDict:
        outfp.write(str(elem[0])+'.line:\t'+ str(round(100*elem[1],2))+'\n')

    outfp.write( 'Correct: '+ str(int(correctLen)) + '\tTotal: '+ str(int(totalLen)) +'\tWord Error Rate: '+str(avgErrorRound)+ '\tWord Accuracy: '+str(avgAccuracy)+'\n')
    outfp.close()


   
       