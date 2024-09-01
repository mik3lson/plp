

#request DNA sequence 
"""
def valid_dna_character(char):
    # to ensure user enters correct nucleotides  
   allowed_letters = {'A','T','G','C'}
   return char in allowed_letters      



def get_valid_dna_string():
   global user_dna_input
   while True:
        user_dna_input = input("Enter DNA sequence: ")
        if all(valid_dna_character(char) for char in user_dna_input):
            print("Input accepted!")
            return user_dna_input
        else:
           print("Invalid input. Please try again.")


get_valid_dna_string()
"""

#request RNA sequEnce
def valid_rna_character(char):
    allowed_letters ={"A","U","G","C"}
    return char in allowed_letters

def get_valid_rna_string():
    global user_rna_input 
    while True:
        user_rna_input = input("Enter RNA sequence")
        if all(valid_rna_character(char) for char in user_rna_input):
            print("Input accepted!")
            return user_rna_input
        else:
            print("invalid input. please try again")
        

get_valid_rna_string()





#convert dna_sequence to rna sequence
#def convert_dna_to_rna(sequence):
#    return sequence.replace("T","U")

#converted_sequence = convert_dna_to_rna(user_dna_input)
#print(converted_sequence)
    



#covert rna sequence to protein sequence
def find_and_group_codons(user_rna_input):
    start_codon = user_rna_input.find("AUG")
    if start_codon== -1:
        print ("sequence don't contain a start codon")
        return None
    else:
       codon_sequence = user_rna_input[start_codon:] #to extract a sequence starting from "AUG"

    #define the stop codons
    stop_codons =["UGA","UAA","UAG"]

    # Group the sequence into codons(triplets) and stop at the first stop codon
    global codons
    codons=[]
    for i in range(0,len(codon_sequence),3):
        codon =codon_sequence[i:3+i]
        if codon in stop_codons:
            break
        codons.append(codon)
    print(codons)


find_and_group_codons(user_rna_input)

# a dictionary mapping each codon to an amino acid    convert the codons to protein sequence
d= {"UUU":"phe","UUC":"phe","UUA":"leu","UUG":"leu","UCU":"ser","UCC":"ser","UCA":"ser","UCG":"ser",
    "CUU":"leu","CUC":"leu","CUA":"leu","CUG":"leu","AUU":"ile","AUC":"ile","AUA":"ile","AUG":"met",
    "GUU":"val","GUC":"val","GUA":"val","GUG":"val","CCU":"pro","CCC":"pro","CCA":"pro","CCG":"pro",
    "ACU":"thr","ACC":"thr","ACA":"thr","ACG":"thr","GCU":"ala","GCC":"ala","GCA":"ala","GCG":"ala",
    "UAU":"tyr","UAC":"tyr","CAU":"his","CAC":"his","CAA":"gln","CAG":"gln","AAU":"asn","AAC":"asn",
    "AAA":"lys","AAG":"lys","GAU":"asp","GAC":"asp","GAA":"glu","GAG":"glu","UGU":"cys","UGC":"cys",
    "UCG":"trp","CGC":"arg","CGC":"arg","CGA":"arg","CGG":"arg","AGU":"ser","AGC":"ser","AGA":"arg",
    "AGG":"arg","GGU":"gly","GGC":"gly","GGA":"gly","GGG":"gly"}

def protein_sequence(codons):
    output_sequence= [d[codon]for codon in codons if codon in d]
    print("-".join(output_sequence))

protein_sequence(codons)