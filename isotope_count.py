"""
This is a program created to estimate the presence of non-standard isotopes in a peptide. It accepts an amino acid sequence as an input and calculates the number of 2H, 13C, 15N, 18O and 34S isotopes.
The program was created for the Python for Biologists course and is not intended for real research applications.
"""

#For clearing the screen, only works for Linux/MacOS
import os

#To pass arguments - this could be done without getops!:
import getopt, sys

#To fetch URLs:
import urllib.request

#Lists for the naturally occurring protein forming amino acids with the number of H, C, N, O, S atoms they contain, respectively
a = Ala = [7, 3, 1, 2, 0]
c = Cys = [7, 3, 1, 2, 1]
d = Asp = [6, 4, 1, 4, 0]
e = Glu = [8, 5, 1, 4, 0]
f = Phe = [11, 9, 1, 2, 0]
g = Gly = [5, 2, 1, 2, 0]
h = His = [9, 6, 3, 2, 0]
i = Ile = [13, 6, 1, 2, 0]
k = Lys = [15, 6, 2, 2, 0]
l = Leu = [13, 6, 1, 2, 0]
m = Met = [11, 5, 1, 2, 1]
n = Asn = [8, 4, 2, 3, 0]
p = Pro = [9, 5, 1, 2, 0]
q = Gln = [10, 5, 2, 3, 0]
r = Arg = [15, 6, 4, 2, 0]
s = Ser = [7, 3, 1, 3, 0]
t = Thr = [9, 4, 1, 3, 0]
v = Val = [11, 5, 1, 2, 0]
w = Trp = [15, 11, 2, 2, 0]
y = Tyr = [11, 9, 1, 3, 0]

#Lists of valid and invalid aa codes
valid = ['a', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'k', 'l', 'm', 'n', 'p', 'q', 'r', 's', 't', 'v', 'w', 'y']
invalid = ['b', 'j', 'o', 'u', 'x', 'z']

#A list of the frequencies of the specified isotopes
freq = [0.01108, 0.00015, 0.00365, 0.00204, 0.0421]



#Define command line arguments - this section is based on https://www.geeksforgeeks.org/command-line-arguments-in-python/
argumentList = sys.argv [1:]
options = "hf:a:s:"
long_options = ["help", "file=", "accession=", "sequence="]



#The function that does the math stuff
def main(sequence):
    
    aa_count = []
    atom_count = [0, 0, 0, 0, 0]
    #Count how many of each amino acid the sequence contains
    for ii in valid:
        aa_count.append(sequence.count(ii))
        
    #Array multiplication: number of each amino acid multiplied by the number of each atom in the amino acids, result is the number of the specified atoms
    for aa in valid:
        for atom in range(len(freq)):
            #eval(aa)[atom] is the count of \atom in the variable named \aa
            #aa_count[valid.index(aa)] shows the element in aa_count corresponding to aa (without the need to make aa_count a dict)
            atom_count[atom] = atom_count[atom] + eval(aa)[atom] * aa_count[valid.index(aa)]

    #Extraction of waters lost during condensation of amino acids, accounting for invalid amino acid letters
    valid_count = 0
    for val in valid:
        valid_count = valid_count + sequence.count(val)
    atom_count[0] = atom_count[0] - (2 * (valid_count - 1))
    atom_count[3] = atom_count[3] - (valid_count - 1)

    #Multiply the number of atoms by the frequency of the isotopes, convert to integers
    isotope_count = [0, 0, 0, 0, 0]
    for it in range(len(freq)):
        isotope_count[it] = atom_count[it] * freq[it]
    isotope_count = [int(x) for x in isotope_count]

    #Print the results
    print ("Processing provided sequence...")
    print("The expected number of isotopes in your sequence:")
    print("2H:", isotope_count[0])
    print("13C:", isotope_count[1])
    print("15N:", isotope_count[2])
    print("18O:", isotope_count[3])
    print("34S:", isotope_count[4])



#Checking for correct sequences - if the sequence comes from a file or a string
def typoDetect(sequence):
    
    #Making sequence lowercase so it matches variables
    sequence = sequence.lower()
    
    if not sequence.isalpha():
        #Sequence does not only contain letters
        print("Error: Invalid characters detected. Please check the input sequence.")
        print("Exiting…")
        
    elif any(x in sequence for x in invalid):
        #Sequence contains letters that are not amino acids
        print("Warning: Invalid amino acid code detected! If you proceed, the invalid characters will be ignored.")
        decision = input("Do you wish to proceed? (y/n)")
        confirmed = ['y', 'Y', 'yes', 'Yes']
        if any(x in decision for x in confirmed):
            main(sequence)
        else:
            print("Exiting…")
    else:
        #Sequence is correct
        main(sequence)



#Fetch sequence by UniProt ID
def fetcher(accession):
    
    #Compile URL
    url = "https://rest.uniprot.org/uniprotkb/{}.fasta".format(accession)
    
    #Download file
    fasta_sequence = urllib.request.urlopen(url)
    
    sequence = ""
    
    #Convert to single string
    for line in fasta_sequence:
        if ">" not in line:
            sequence = sequence + line
            
    #Making sequence lowercase so it matches variables
    sequence = sequence.lower()
    
    #Assuming accessions are correct, so calling main directly
    main(sequence)



#Read sequence from file, handle headers and line breaks
def fileHandler(file_path):
    
    #open file
    fasta_sequence = open (file_path, "r")
    
    sequence = ""
    
    #Convert to single string
    for line in fasta_sequence:
        if ">" not in line:
            sequence = sequence + line.strip()
    
    print(sequence)
    
    
    #Might contain typos, passing it through typoDetect
    typoDetect(sequence)




#No arguments are passed (=no sequence), show help
def helper():
    print ("Placeholder for help message")
    print ("The help message is supposed to state the purpose of the program and list the arguments that can be used")
    print ("It could probably be the same text as the readme file?")



#This is where we start doing stuff
os.system('clear')
print("This program's purpose is to estimate the number of uncommon isotopes (2H, 13C, 15N, 18O and 34S) in a given peptide.")



#Sort out what to do based on the passed arguments
try:
    #Parsing
    arguments, values = getopt.getopt(argumentList, options, long_options)
    
    for currentArgument, currentValue in arguments:
        
        if currentArgument in ("-h", "--help"):
            helper()
        
        elif currentArgument in ("-f", "--file"):
            print ("Reading sequence from file...")
            fileHandler(currentValue)
        
        elif currentArgument in ("-a", "--accession"):
            print ("Fetching sequence from UniProt...")
            fetcher(currentValue)
        
        elif currentArgument in ("-s", "--sequence"):
            typoDetect(currentValue)
        
        else:
            print ("No arguments passed, displaying help screen")
            helper()

#Error handling, not a priority right now
except getopt.error as err:
    print (str(err))


#Add main guard
#Move variables to a config file > 'configparser'
#argparse / sys.argv (this is simpler than argparse)
#Change if-elif-else to switch
#Simplify argument parsing: it can be done without getopt