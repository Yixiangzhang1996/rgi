import os
import sys
import filepaths
import argparse

script_path = filepaths.determine_path()
working_directory = os.getcwd()
path = script_path+"/"

#remove temporary file
def main():
	
	if os.path.isfile(path+"contigToPro.fasta"):
		os.remove(path+"contigToPro.fasta")
	if os.path.isfile(path+"read.fsa"):
		os.remove(path+"read.fsa")
	if os.path.isfile(path+"contig.fsa"):
		os.remove(path+"contig.fsa")
	if os.path.isfile(path+"contigToORF.fsa"):
		os.remove(path+"contigToORF.fsa")
	if os.path.isfile(path+"blastRes.xml"):
		os.remove(path+"blastRes.xml")
	if os.path.isfile(path+"blastpjson"):
		os.remove(path+"blastpjson")
	if os.path.isfile(path+"proteindb.fsa"):
		os.remove(path+"proteindb.fsa")
	if os.path.isfile(path+"dnadb.fsa"):
		os.remove(path+"dnadb.fsa")
	if os.path.isfile(path+"protein.db.phr"):
		os.remove(path+"protein.db.phr")
		os.remove(path+"protein.db.pin")
		os.remove(path+"protein.db.psq")
	if os.path.isfile(path+"temp.fsa"):
		os.remove(path+"temp.fsa")
	if os.path.isfile(path+"dna.db.nhr"):
		os.remove(path+"dna.db.nhr")
		os.remove(path+"dna.db.nin")
		os.remove(path+"dna.db.nsq")
	if os.path.isfile(path+"Report.json"):
		os.remove(path+"Report.json")
	if os.path.isfile(path+"draft"):
		os.remove(path+"draft")
	if os.path.isfile(path+"dataSummary.txt"):
		os.remove(path+"dataSummary.txt")


	print>>sys.stderr, "Cleaned directory: "+path

if __name__ == '__main__':
	parser = argparse.ArgumentParser(description='Removes BLAST databases created using card.json')
	args = parser.parse_args()
	main()