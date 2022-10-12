# GBG_Python_course: isotope_counter.py
Project work for the "Python for biologists" course.
This is a program created to estimate the presence of non-standard isotopes in a peptide. It accepts an amino acid sequence as an input and calculates the number of 2H, 13C, 15N, 18O and 34S isotopes.


The script can be called with the following arguments:

	-h, --help: Print a help message and exit
	-f, --file: Read the amino acid sequence from a file (fasta headers are ignored). Needs to be followed by an absolute file path.
	-a, --accession: Fetch the sequence from the UniProt database. Needs to be followed by a UniProt accession number.
	-s, --sequence: process the sequence passed in the command line. Needs to be followed by the sequence.


Examples:

	A file:
		Q8LPD9.fasta (included in the repo)
		Chlamydomonas reinhardtii phototropin
		Values: 64/0/3/2/0

	An accession:
		Q8WZ42
		Human titin (the largest protein in the database).
		Values: 3008/25/166/106/38

	A string:
		MHSWERLAVLVLLGAAACAAPPRGRILGGREAEAHARPYMASVQLNGAHLCGGVLVAEQWVLSAAHCLEDAADGKVQVLLGAHSLSQPEPSKRLYDVLRAVPHPDSQPDTIDHDLLLLQLSEKATLGPAVRPLPWQRVDRDVAPGTLCDVAGWGIVNHAGRRPDSLQHVLLPVLDRATCNRRTHHDGAITERLMCAESNRRDSCKGDSGGPLVCGGVLEGVVTSGSRVCGNRKKPGIYTRVASYAAWIDSVLA
		Human complement factor D
		Values: 21/0/1/0/0
