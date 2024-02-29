import os

def create_bowtie2_index(reference_fasta, index_prefix):
    #create the index
    command = f"bowtie2-build {reference_fasta} {index_prefix}"
    #run command
    os.system(command)

def map_reads_to_hcmv(reads_fastq, hcmv_index_prefix, mapped_reads_fastq):
    # Command to map reads to HCMV index
    command = f"bowtie2 -x {hcmv_index_prefix} -U {reads_fastq} -S {mapped_reads_fastq} --no-unal"
    # Execute the command
    os.system(command)

def count_reads_fastq(fastq_file):
    #count the number of reads
    with open(fastq_file) as f:
        count = sum(1 for line in f) // 4
    return count

def run_spades(input_reads, output_dir):
    # Command to run SPAdes
    command = f"spades.py  -s {input_reads[0]} -s {input_reads[1]} -s {input_reads[2]} -s {input_reads[3]} -o {output_dir} --phred-offset 33"
    # Execute the command
    os.system(command)

###############################################################################

#file path defs
hcmv_genome_fasta = "NC_006273.2.fasta"
hcmv_index_prefix = "hcmv_index"
log_file = "bowtie2_mapping.log"

#create index for hcmv
create_bowtie2_index(hcmv_genome_fasta, hcmv_index_prefix)

#FASTQ input list
fastq_files = ["Donor1_2dpi.fastq", "Donor1_6dpi.fastq", "Donor3_2dpi.fastq", "Donor3_6dpi.fastq"]

#mapping
for fastq_file in fastq_files:
    mapped_reads_fastq = f"mapped_reads_{fastq_file.split('.')[0]}.fastq"
    map_reads_to_hcmv(fastq_file, hcmv_index_prefix, mapped_reads_fastq)

    #count before and afer
    reads_before_mapping = count_reads_fastq(fastq_file)
    reads_after_mapping = count_reads_fastq(mapped_reads_fastq)

    #write to log
    with open(log_file, "a") as f:  # Append to log file
        f.write(f"FASTQ file: {fastq_file}\n")
        f.write(f"Number of reads before mapping: {reads_before_mapping}\n")
        f.write(f"Number of reads after mapping: {reads_after_mapping}\n\n")

###############################################################################
#mapped input
mapped_reads_fastq_files = [
    "mapped_reads_Donor1_2dpi.fastq",
    "mapped_reads_Donor1_6dpi.fastq",
    "mapped_reads_Donor3_2dpi.fastq",
    "mapped_reads_Donor3_6dpi.fastq"
]

#putput
spades_output_dir = "spades_output"

#running spades
run_spades(mapped_reads_fastq_files, spades_output_dir)

#writing the command to the log
spades_command = f"spades.py  -s {mapped_reads_fastq_files[0]} -s {mapped_reads_fastq_files[1]} -s {mapped_reads_fastq_files[2]} -s {mapped_reads_fastq_files[3]} -o {spades_output_dir}"
log_file = "assembly.log"
with open(log_file, "a") as f:
    f.write("SPAdes command:\n")
    f.write(spades_command + "\n")
