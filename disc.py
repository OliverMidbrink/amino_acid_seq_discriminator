# Start by cutting up the seqs according to a seed
import random
import tools
import model
import torch
from tqdm import tqdm

# Function parameters are as above
def run_discrimination_experiment(comp1, comp2, n_epoch, n_CV, train_frac, seeds, n_chars, max_seq_len, name):
    for seed in seeds:
        random.seed(seed)
        torch.manual_seed(seed)

        with open(comp1, 'r') as f:
            seq_1 = [item.replace("\n", "") for item in f.readlines()]

        with open(comp2, 'r') as f:
            seq_2 = [item.replace("\n", "") for item in f.readlines()]

        random.shuffle(seq_1)
        random.shuffle(seq_2)

        seq_1_train = seq_1[:int(len(seq_1)*train_frac)]
        seq_1_test = seq_1[int(len(seq_1)*train_frac):]

        seq_2_train = seq_2[:int(len(seq_2)*train_frac)]
        seq_2_test = seq_2[int(len(seq_2)*train_frac):]

        # Train the model
        model_ = model.Classifier(n_chars * max_seq_len)
        optimizer = torch.optim.Adam(model_.parameters(), lr=0.001)
        criterion = torch.nn.BCEWithLogitsLoss()

        model_.train()
        for epoch in tqdm(range(n_epoch), desc="Training"):
            for x in range(int((len(seq_1_train) + len(seq_2_train)) / 2)):   
                seq_1 = random.choice(seq_1_train)
                if len(seq_1) > max_seq_len:
                    seq_1 = seq_1[:max_seq_len]
                seq_1 = "+"*(100 - len(seq_1)) + seq_1
                seq_1 = tools.seq_to_tensor(seq_1).flatten()
                lab_1 = torch.tensor([0], dtype=torch.float)

                optimizer.zero_grad()
                out = model_(seq_1)
                loss = criterion(out, lab_1)
                loss.backward()
                optimizer.step()

                seq_2 = random.choice(seq_2_train)
                if len(seq_2) > max_seq_len:
                    seq_2 = seq_2[:max_seq_len]
                seq_2 = "+"*(100 - len(seq_2)) + seq_2
                seq_2 = tools.seq_to_tensor(seq_2).flatten()
                lab_2 = torch.tensor([1], dtype=torch.float)

                optimizer.zero_grad()
                out = model_(seq_2)
                loss = criterion(out, lab_2)
                loss.backward()
                optimizer.step()        

        # Test the model
        model_.eval()
        mean_loss = 0
        for epoch in tqdm(range(n_epoch), desc="Testing"):
            for x in range(int((len(seq_1_test) + len(seq_2_test)) / 2)):   
                seq_1 = random.choice(seq_1_test)
                if len(seq_1) > max_seq_len:
                    seq_1 = seq_1[:max_seq_len]
                seq_1 = "+"*(max_seq_len - len(seq_1)) + seq_1
                seq_1 = tools.seq_to_tensor(seq_1).flatten()
                lab_1 = torch.tensor([0], dtype=torch.float)

                out = model_(seq_1)
                loss = criterion(out, lab_1)
                mean_loss += loss / (len(seq_1_test) + len(seq_2_test)) / n_epoch

                seq_2 = random.choice(seq_2_test)
                if len(seq_2) > max_seq_len:
                    seq_2 = seq_2[:max_seq_len]
                seq_2 = "+"*(max_seq_len - len(seq_2)) + seq_2
                seq_2 = tools.seq_to_tensor(seq_2).flatten()
                lab_2 = torch.tensor([1], dtype=torch.float)

                out = model_(seq_2)
                loss = criterion(out, lab_2)
                mean_loss += loss / (len(seq_1_test) + len(seq_2_test)) / n_epoch

        with open(name, 'a') as f:
            f.write(f"Seed: {seed}, Distance (1/mean_loss): {1/mean_loss}\n")


if __name__ == "__main__":
    n_epoch_ = 2
    n_CV_ = 5
    train_frac_ = 0.8
    #seeds_ = list(range(n_CV_))
    seeds_ = [random.randint(0, 10000000) for _ in range(n_CV_)]


    n_chars_ = len(tools.chars)
    max_seq_len_ = 100

    name_ = "uniform_vs_filtered.txt"
    comp_1 = 'R_synth.txt'
    comp_2 = 'filtered.txt'

    run_discrimination_experiment(comp_1, comp_2, n_epoch_, n_CV_, train_frac_, seeds_, n_chars_, max_seq_len_, name_)
