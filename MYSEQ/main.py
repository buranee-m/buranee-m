from seqbio.calculation.SeqCal import gcContent, countBase, atContent,countBasesDict
from seqbio.pattern.SeqPattern import cpgSearch, enzTargetsScan
from seqbio.seqMan.dnaconvert import reverseSeq,complementSeq,reverseComplementSeq, dna2rna, dna2protein

# Input
seq = 'ATGGGccGTAGAATTCTTGCaaGCCCGT'
seq = seq.upper()
print("Transcription: ", dna2rna(seq))
print("Transcription-revcomp: ", dna2rna(reverseComplementSeq(seq)))
print("Translation: ", dna2protein(seq))
print("Translation-revcomp: ", dna2protein(reverseComplementSeq(seq)))
print("GC Content:", gcContent(seq))
print("Count Bases: ", countBasesDict(seq))
print("Count Bases-revcomp: ", countBasesDict(reverseComplementSeq(seq)))
print("Search EcoRI: ", enzTargetsScan(seq, 'EcoRI'))
print("Search EcoRI-revcomp: ", enzTargetsScan(reverseComplementSeq(seq), 'EcoRI'))
