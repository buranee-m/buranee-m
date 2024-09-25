from seqbio.calculation.SeqCal import *
from seqbio.pattern.SeqPattern import *
from seqbio.seqMan.dnaconvert import *
# Input
def test():
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

def argparserLocal():
    from argparse import ArgumentParser
    '''Argument parser for the commands'''
    parser = ArgumentParser(prog='myseq', description='Work with sequence')

    subparsers = parser.add_subparsers(
        title='commands', description='Please choose command below:',
        dest='command'
    )
    # subparsers.required = True
#Define commands
    cgc_command = subparsers.add_parser('gcContent', help='Calculate GC content')
    cgc_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")

    count_command = subparsers.add_parser('countBases', help='Count number of each base')
    count_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    count_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    transcrip_command = subparsers.add_parser('transcription', help='Convert DNA to RNA ')
    transcrip_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    transcrip_command.add_argument("-r", "--revcomp", action="store_true", help="Convet DNA to reverse-complementary")

    translation_command = subparsers.add_parser('translation', help='Convert RNA to Protein ')
    translation_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    translation_command.add_argument("-r", "--revcomp", action="store_true", help="Convet RNA to reverse-complementary")

    cgcserch_command = subparsers.add_parser('cpgScan', help='Search for CpG sequence')
    cgcserch_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzTargetsScan_command = subparsers.add_parser('enzTargetsScan', help='Find restriction enzyme')
    enzTargetsScan_command.add_argument("-s", "--seq", type=str, default=None,
                             help="Provide sequence")
    enzTargetsScan_command.add_argument("-e","--enz", type=str, default=None, help="Enzyme Name")
    enzTargetsScan_command.add_argument("-r","--revcomp", action="store_true", help="Convert DNA to reverse-complementary")

    return parser

# def test():
#     # Input
#     parser = argparserLocal()
#     args1 = parser.parse_args(["enzTargetsScan","-seq","ATGGGccGTAGAATTCTTGCaaGCCCGT","-e","EcoRI"])
#     print("Input",args1.seq,f"\n{args1.enz} sites", enzTargetsScan(args1.seq, args1.enz) )
#     args2 = parser.parse_args(["enzTargetsScan", "--seq","ATGGGccGTAGAATTCTTGCaaGCCCGT","-e","EcoRI","-r"])    
#     print("Input",args2.seq,f"\n{args2.enz} sites", enzTargetsScan(reverseComplementSeq(args2.seq, args2.enz) ))

    
# Input
def main():
    parser = argparserLocal()
    args = parser.parse_args()
    if args.seq == None:
        print("------\nError: You do not provide -s or --seq\n------\n")
    else:
        seq = args.seq.upper()
    
    def handle_output(command, seq):
        if command == 'transcription':
            return f"Transcription = {dna2rna(seq)}"
        elif command == 'translation':
            return f"Translation = {dna2protein(seq)}"
        elif command == 'gcContent':
            return f"GC content = {gcContent(seq)}"
        elif command == 'countBases':
            return f"Count Bases = {countBasesDict(seq)}"
        else: command == 'enzTargetsScan' 
        return f"{args.enz} sites = {enzTargetsScan(seq, args.enz)}"
    sequence_to_use = reverseComplementSeq(seq) if args.revcomp else seq
    print(f"Input: {seq}")
    print(handle_output(args.command, sequence_to_use))



if __name__ == "__main__":
    # main()
    main()

