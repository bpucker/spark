### Boas Pucker ###
### bpucker@cebitec.uni-bielefeld.de ###
### v0.1 ###

__usage__ = """
					python SPARK_finder.py
					--in <DATA_FOLDER>
					--out <OUTPUT_FOLDER>
					
					bug reports and feature requests: bpucker@cebitec.uni-bielefeld.de
					"""

import os, glob, re, sys

# --- end of imports --- #


def load_sequences( fasta_file ):
	"""! @brief load candidate gene IDs from file """
	
	sequences = {}
	
	with open( fasta_file ) as f:
		header = f.readline()[1:].strip()
		seq = []
		line = f.readline()
		while line:
			if line[0] == '>':
					sequences.update( { header: "".join( seq ).upper() } )
					header = line.strip()[1:]
					seq = []
			else:
				seq.append( line.strip() )
			line = f.readline()
		sequences.update( { header: "".join( seq ).upper() } )	
	return sequences


def get_matches( seqs, pattern ):
	"""! @brief get all matches """
	
	matches = []
	for key in seqs.keys():
		hits = re.findall( pattern, seqs[ key ] )
		if len( hits ) == 1:
			matches.append( { 'id': key, 'seq': seqs[ key ], 'hit': hits[0] } )
		elif len( hits ) > 1:
			for hit in hits:
				matches.append( { 'id': key, 'seq': seqs[ key ], 'hit': hit } )
			print "WARNING: multiple hits!"
	return matches
	
	


def main( arguments ):
	
	data_dir = arguments[ arguments.index( '--in' )+1 ]
	output_dir = arguments[ arguments.index( '--out' )+1 ]
	
	if not os.path.exists( output_dir ):
		os.makedirs( output_dir )
	
	fasta_files = glob.glob( data_dir + "*.faa" ) + glob.glob( data_dir + "*.fasta" ) + glob.glob( data_dir + "*.fa" )
	
	patterns = [ "C\w{18,27}C\w{26,32}C\w{15,23}C\w{8,15}C\w{22,26}C\w{7,10}C\w{2}C" ]
	#CX(18-27)CX(26-32)CX(15-23)CX(8-15)CX(22-26)CX(7-10)CX(2)C
	
	output_file = output_dir + "results.txt"
	
	total_hit_counter = 0
	with open( output_file, "w" ) as out:
		out.write( "Species\tID\tMatch\tPattern\tSeq\n" )
		for pattern in patterns:
			for idx, fasta in enumerate( fasta_files ):
				print str( idx+1 ) + "/" + str( len( fasta_files ) )
				ID = fasta.split('/')[-1].split('.')[0]
				seqs = load_sequences( fasta )
				matches = get_matches( seqs, pattern )
				for match in matches:
					out.write( "\t".join( [ ID, match['id'], match['hit'], pattern, match['seq'] ] )+'\n' )
				total_hit_counter += len( matches )
	print "total number of hits: " + str( total_hit_counter )


if '--in' in sys.argv and '--out' in sys.argv:
	main( sys.argv )
else:
	sys.exit( __usage__ )
