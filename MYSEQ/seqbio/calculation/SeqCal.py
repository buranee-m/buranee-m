import re
def countBase(seq,base):
    return seq.count(base.upper())

def gcContent(seq):
    gc = len(re.findall('[GC]',seq))
    total_bases = len(seq)
    gc_content = (gc/total_bases)
    return float(gc_content)

def atContent(seq):
    return float((len(re.findall('[AT]',seq)))/len(seq)*100)

def countBasesDict(seq):
    basesM = {}
    for base in seq:
        if base in basesM:
           basesM[base] += 1
        else:
            basesM[base] = 1
    return basesM


