import torch

with open("seq_1.txt", "r") as f:
    seq_1 = f.readlines()

with open("seq_2.txt", "r") as f:
    seq_2 = f.readlines()

seqs = ("".join(seq_1) + "".join(seq_2)).strip().replace("\n", "")

chars = sorted(list(set(seqs + "+" + "|")))

def seq_to_tensor(seq):
    tensor = torch.zeros(len(seq), len(chars))
    for i, c in enumerate(seq):
        tensor[i][chars.index(c)] = 1
    return tensor