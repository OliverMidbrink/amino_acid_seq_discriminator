import tools
import random

with open("synth.txt", "r") as f:
    seqs = f.readlines()

chars = sorted(list(set("".join(seqs).strip().replace("\n", "") + "+" + "|")))

char_distribution = {char: 0 for char in chars}
total_chars = 0
for seq in seqs:
    for char in seq:
        if char not in chars:
            continue
        char_distribution[char] += 1
        total_chars += 1

for char in char_distribution:
    char_distribution[char] /= total_chars

for seq in seqs:
    
    random_seq = ""
    for x in range(len(seq) - 1):
        # Use the char distribution when selecting the next char
        random_seq += random.choices([char for char in chars if char not in ['+', '|']], weights=[char_distribution[char] for char in chars  if char not in ['+', '|']])[0]
    
    random_seq += "|"

    with open("RNU_synth.txt", "a") as f:
        f.write(random_seq)
        f.write("\n")