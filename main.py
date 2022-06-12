import json
import string
import requests
import numpy as np
import matplotlib.pyplot as plt
from numerize import numerize
import scipy.stats as stats
import seaborn as sns
import time
import pandas as pd

NUM_DIGITS = 1000000

URL = "https://uploadbeta.com/api/pi/"
SHOW_IMAGES = True


def fetch_digits() -> string:
    digits = ""

    response = requests.get(f"{URL}/?cached&n={NUM_DIGITS}")
    if response.status_code == 200:
        print(f"Successfully hit endpoint {URL}\nRetrieved {NUM_DIGITS} digits of pi.")
        digits = response.json()[1:]  # Endpoints return 0 as first digit
        return digits

    print("Failed to receive digits of pi from URLs.")


def analyze_distribution(digits: string) -> None:
    start = time.time()
    distribution = np.zeros(10)

    for digit in digits:
        distribution[int(digit)] += 1

    probs = distribution / np.linalg.norm(distribution)
    digit_labels = [str(x) for x in range(10)]

    if SHOW_IMAGES:
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        ax.yaxis.grid(True)
        plt.bar(digit_labels, probs, color="lightblue", width=0.8)
        plt.xlabel("Digit")
        plt.ylabel("Frequency (%)")
        plt.title(f"Distribution of {numerize.numerize(NUM_DIGITS)} digits of π")
        plt.show(block=False)

    chi_sq, p_val = stats.chisquare(distribution)
    print(f"\nFrequency Test: \n\tChi squared: {chi_sq}\tp-value: {p_val}")
    print(f"\tAnalysis took {time.time()-start} seconds.")


def analyze_pairs(digits: string) -> None:
    start = time.time()
    freqs = np.zeros((10, 10))
    for i in range(len(digits) - 1):
        freqs[int(digits[i])][int(digits[i + 1])] += 1

    probs = freqs / np.linalg.norm(freqs)

    if SHOW_IMAGES:
        plt.figure()
        sns.heatmap(probs, linewidth=0.5, vmin=0.08, vmax=0.12, cmap="YlGnBu")
        plt.xlabel("Current Digit")
        plt.ylabel("Next Digit")
        plt.title(f"Probability of next digit given current digit")
        plt.show(block=False)

    chi_sq, p_val = stats.chisquare(freqs.flatten())
    print(f"Pair Test: \n\tChi squared: {chi_sq}\tp-value: {p_val}")
    print(f"\tAnalysis took {time.time()-start} seconds.")


def analyze_spaces(digits: string) -> None:
    start = time.time()
    spaces = [[] for _ in range(10)]
    last_seen = [-1 for _ in range(10)]

    for i in range(len(digits)):
        digit = int(digits[i])
        if last_seen[digit] > -1:
            spaces[digit].append(i - last_seen[digit])
        last_seen[digit] = i
    print("Space test:")
    for i in range(10):
        print(f"\t{i}: {sum(spaces[i])/len(spaces[i])}")

    if SHOW_IMAGES:
        fig = plt.figure()
        ax = fig.add_axes([0.1, 0.1, 0.8, 0.8])
        plt.xlabel("Digit")
        plt.ylabel("Distance")
        plt.title(f"Distance between recurrence of the same digit")
        ax.set_xticklabels(np.arange(0, 10))
        bplot = ax.boxplot(
            spaces,
            showfliers=False,
            notch=True,
            vert=True,
            patch_artist=True,
        )
        ax.set_facecolor("lightgrey")
        ax.yaxis.grid(True)
        for patch in bplot["boxes"]:
            patch.set_facecolor("lightblue")
        plt.show()
    print(f"\tAnalysis took {time.time()-start} seconds.")


if __name__ == "__main__":
    start = time.time()
    digits = fetch_digits()
    print(f"\tFetching took {time.time()-start} seconds.")
    if digits:
        analyze_distribution(digits)
        analyze_pairs(digits)
        analyze_spaces(digits)
