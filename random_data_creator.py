import tools
import random

with open("synth.txt", "r") as f:
    seqs = f.readlines()

for seq in seqs:
    
    random_seq = ""
    for x in range(len(seq) - 1):
        random_seq += random.choice([char for char in tools.chars if char not in ['+', '|']])
    
    random_seq += "|"

    with open("R_synth.txt", "a") as f:
        f.write(random_seq)
        f.write("\n")