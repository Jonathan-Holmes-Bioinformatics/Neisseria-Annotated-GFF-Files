# Neisseria-Annotated-GFF-Files
Neisseria-annotated-GFF-Files

Use:

This is a simple custom script aiming to increase the readability of gff files in programmes such as artemis by combining 
annotation derived terms and the database specific NEIS terms used in PubMLST. 

Tutorial:

This  pipeline requires two files and was designed with the following programme versions. I cannot guarantee correct 
functionality with alternative versions, but older version may work.

Python 3.7.4
Prokka 1.14.0

Input files:
  - Protein xmfa file, download for the isolate and genes of interest from PubMLST: https://pubmlst.org/
  - Genome sequence (or contigs) for the Isolate of interest, from sources such as NCBI
  
Pipeline:
- Run Prokka against the Genome file with no additional arguements e.g:
  
  Prokka Genome.fasta
  
- Run xmfa_to_fasta.py on the downloaded protein xmfa file from pubMLST as follows:
  
  Python3 input.xmfa output.fasta
 
- Run Prokka against the original Genome file using the newly generated Fasta as a protein library:

  Prokka --proteins output.fasta Genome.fasta
  
- Finally run Custom_Annotation.py on the generated files to combine the annotations for the two files:

  Python3 Custom_Annotation.py PROKKA-Only-Genome.gff With-NEIS-Genome.gff Combined-Genome.gff
  
  
  The Combined-Genome.gff can now be read into Artemis with each gene/CDS named with the PROKKA functional annotation 
  with the appropriate NEIS number annotated within the notes section of each gene/CDS where possible.
  
  
  Method.
  
  The annotation of the genome into a gff file generates open reading frames with their: Location and name.
  If the locaitonal coordinates are conserved between the default Prokka and NEIS annotated Prokka file then the
  two CDS are assumed to reference the same gene. This information is then combined into a new annotation line. 
  
  
  
  
  




