import sys
import codecs
import os
import math
import operator
import json

#multi file reference
def read_files(hyp, ref):
    references = []
    isFile = os.path.isfile(ref)
    if isFile:
        reference_file = codecs.open(ref, 'r', 'utf-8')
        references.append(reference_file.readlines())
    else:
        for root, dirs, files in os.walk(ref):
            for f in files:
                reference_file = codecs.open(os.path.join(root, f), 'r', 'utf-8')
                references.append(reference_file.readlines())
    hypothesis_file = codecs.open(hyp, 'r', 'utf-8')
    hypothesis = hypothesis_file.readlines()
    return hypothesis, references


def count_ngram(hypothesis, references, n):
    clipped_count = 0
    count = 0
    r = 0
    h = 0
    for si in range(len(hypothesis)):
        ref_counts = []
        ref_lengths = []
        # Build dictionary of ngram counts
        for reference in references:
            ref_sentence = reference[si]
            ngram_d = {}
            words = ref_sentence.strip().split()
            ref_lengths.append(len(words))
            limits = len(words) - n + 1
            for i in range(limits):
                ngram = ' '.join(words[i:i+n]).lower()
                if ngram in ngram_d.keys():
                    ngram_d[ngram] += 1
                else:
                    ngram_d[ngram] = 1
            ref_counts.append(ngram_d)

        hyp_sentence = hypothesis[si]
        hyp_dict = {}
        words = hyp_sentence.strip().split()
        limits = len(words) - n + 1
        for i in range(0, limits):
            ngram = ' '.join(words[i:i + n]).lower()
            if ngram in hyp_dict:
                hyp_dict[ngram] += 1
            else:
                hyp_dict[ngram] = 1
        clipped_count += clip_count(hyp_dict, ref_counts)
        count += limits
        best=best_length_match(ref_lengths, len(words))
        r += best
        h += len(words)
    if clipped_count == 0:
        precision = 0
    else:
        precision = float(clipped_count) / count +1e-12 # escape zero division 
        pen = penalty(h, r)
    return precision, pen

def clip_count(hyp_d, ref_ds):
    count = 0
    for m in hyp_d.keys():
        m_w = hyp_d[m]
        m_max = 0
        for ref in ref_ds:
            if m in ref:
                m_max = max(m_max, ref[m])
        m_w = min(m_w, m_max)
        count += m_w
    return count

#select choice best length match for multiple references file
def best_length_match(ref_l, hyp_l):
       least_diff = abs(hyp_l-ref_l[0])
       best = ref_l[0]
       for ref in ref_l:
          if abs(hyp_l-ref) < least_diff:
            least_diff = abs(hyp_l-ref)
            best = ref
       return best
   
def penalty(hyp, ref):
    if hyp > ref:
        pen = 1
    else:
        pen = math.exp(1-(float(ref)/hyp))
    return pen

def geometric_mean(xs):
    epsilon=0.00000000001
    return math.exp(math.fsum(math.log(x+epsilon) for x in xs) / (len(xs) +epsilon))

def calculateBLUE(hypothesis, references,ngram=4):
    precisions = []
    for i in range(ngram):
        precision, penalty = count_ngram(hypothesis, references, i+1)
        precisions.append(precision)
    if(hypothesis!='' and references!=''):
      bleu =   geometric_mean(precisions) * penalty
      return round(100*bleu,2)
    else:
      return 0.0

if __name__ == "__main__":

    hyp_file=sys.argv[1]
    ref_files= sys.argv[2] #directory or file
    hypothesis, references = read_files(hyp_file,  ref_files)
    bleu1 =  calculateBLUE(hypothesis, references,ngram=1)
    bleu2 =  calculateBLUE(hypothesis, references,ngram=2)
    bleu3 =  calculateBLUE(hypothesis, references,ngram=3)
    bleu4 =  calculateBLUE(hypothesis, references)
    print('Bleu1: ',bleu1,' Bleu2: ',bleu2,' Bleu3: ',bleu3,' Bleu4: ',bleu4)