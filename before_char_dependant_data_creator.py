import tools
import random

with open("synth.txt", "r") as f:
    seqs = f.readlines()

chars = sorted(list(set("".join(seqs))))

seqs_concat = "".join(seqs).strip().replace("\n", "").replace("|", "")

char_dicts = {char: {} for char in chars}
char_dicts_totals = {char: 0 for char in chars}

for idx, char in enumerate(seqs_concat):
    if idx > 0:
        prev_char = seqs_concat[idx - 1]
        char_dicts[prev_char][char] = char_dicts[prev_char].get(char, 0) + 1
        char_dicts_totals[prev_char] += 1

# Normalize
for char in char_dicts:
    for next_char in char_dicts[char]:
        char_dicts[char][next_char] /= char_dicts_totals[char]

print(char_dicts)

del char_dicts['|']
del char_dicts['\n']

for seq in seqs:
    random_seq = random.choice([char for char in chars if char not in ['+', '|', '\n']])

    for x in range(len(seq) - 2):
        # Use the char distribution when selecting the next char
        chars = list(char_dicts[random_seq[-1]].keys())
        weights = list(char_dicts[random_seq[-1]].values())

        random_seq += random.choices(chars, weights=weights)[0]
    
    random_seq += "|"

    with open("RPCD_synth.txt", "a") as f:
        f.write(random_seq)
        f.write("\n")