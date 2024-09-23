import re
def cpgSearch(seq):
    cpgs = []
    for m in re.finditer(r'CG',seq,re.I):
        cpgs.append((m.group(),m.start(),m.end()))
    return cpgs

def enzTargetsScan(seq,enz):
    resEnzyme = dict(
        EcoRI='GAATTC', 
        BamHI='GGATCC', 
        HindIII='AAGCTT',
        AccB2I='[AG]GCGC[CT]',
        AasI='GAC[ATCG]{6}GTC',
        AceI='GC[AT]GC'
        )
    out = []
    if enz in resEnzyme:
        pattern = resEnzyme[enz]
        for match in re.finditer(pattern,seq):
            out.append((match.group(),match.start(),match.end()))
    return out

    seq = seq.upper()
    print("test cpgSearch:", cpgSearch(seq))
    print("test enzTargetsScan:", enzTargetsScan(seq,'EcoRI'))


