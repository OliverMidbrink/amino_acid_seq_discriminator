
def check_dist(dataset_name):
    with open(dataset_name, "r") as f:
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

    return char_distribution


if __name__ == "__main__":
    dataset_name = "filtered.txt"
    dist_filtered = check_dist(dataset_name)

    dataset_name = "random_non_uniform.txt"
    dist_rand_non_uniform = check_dist(dataset_name)

    dataset_name = "random.txt"
    dist_rand_uniform = check_dist(dataset_name)

    # Plot the distributions
    import matplotlib.pyplot as plt
    plt.bar(dist_filtered.keys(), dist_filtered.values(), color='b', alpha=0.5, label='Filtered')
    plt.bar(dist_rand_non_uniform.keys(), dist_rand_non_uniform.values(), color='r', alpha=0.5, label='Random non-uniform')
    plt.bar(dist_rand_uniform.keys(), dist_rand_uniform.values(), color='g', alpha=0.5, label='Random uniform')
    plt.legend()

    plt.show()
