# Genome-Assembly-Pipeline
Assignment for computational biology. Based on data from HCMV. Cheng et al. 2017 (https://www.ncbi.nlm.nih.gov/pubmed/29158406

Pipleline 2: Genome assembly

Data from the donors was acquired using wget.

I had reached step 5 when I encountered issues with the query sequence and traced it back to step 2 and was forced to restart. 
I was able to locally create a database of 9 viral genomes under the subfamily Betaherpesviridae but the BLAST would return no results, upon investigation, the query sequence(the longest contig) was a human gene.
