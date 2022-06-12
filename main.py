import json
import string
import requests
import numpy as np
import matplotlib.pyplot as plt
from numerize import numerize
import scipy.stats as stats
import seaborn as sns

NUM_DIGITS = 1000000
URLS = ["https://uploadbeta.com/api/pi/"]


def fetch_digits() -> string:
    digits = ""

    for url in URLS:
        response = requests.get(f"{url}/?cached&n={NUM_DIGITS}")
        if response.status_code == 200:
            print(
                f"Successfully hit endpoint {url}\nRetrieved {NUM_DIGITS} digits of pi."
            )
            digits = response.json()[1:]  # Endpoints return 0 as first digit
            return digits
    print("Failed to receive digits of pi from URLs.")


def analyze_distribution(digits: string) -> None:
    distribution = np.zeros(10)

    for digit in digits:
        distribution[int(digit)] += 1

    probs = distribution / np.linalg.norm(distribution)
    digit_labels = [str(x) for x in range(10)]

    plt.figure()
    plt.bar(digit_labels, probs, color="lightblue", width=0.8)
    plt.xlabel("Digit")
    plt.ylabel("Frequency (%)")
    plt.title(f"Distribution of {numerize.numerize(NUM_DIGITS)} digits of π")
    plt.show(block=False)

    chi_sq, p_val = stats.chisquare(distribution)
    print(f"Chi squared: {chi_sq}\tp-value: {p_val}")


def analyze_pairs(digits: string) -> None:
    freqs = np.zeros((10, 10))
    for i in range(len(digits) - 1):
        freqs[int(digits[i])][int(digits[i + 1])] += 1

    probs = freqs / np.linalg.norm(freqs)

    plt.figure()
    sns.heatmap(probs, linewidth=0.5, vmin=0.08, vmax=0.12, cmap="YlGnBu")
    plt.show()

    chi_sq, p_val = stats.chisquare(freqs.flatten())
    print(f"Chi squared: {chi_sq}\tp-value: {p_val}")


def analyze_runs(digits: string) -> None:
    going_up = digits[1] > digits[0]
    total_runs = 0
    for i in range(1, len(digits) - 1):
        running_up = int(digits[i + 1]) > int(digits[i])
        if running_up != going_up:
            going_up = running_up
            total_runs += 1

    expected_mean = (2 * len(digits) - 1) / 3
    print(expected_mean)
    print(total_runs)
    expected_sd = np.sqrt((16 * len(digits) - 29) / 90)
    print(expected_sd)
    t_test = (total_runs - expected_mean) / expected_sd
    p_val = stats.t.sf(np.abs(t_test), len(digits) - 1) * 2
    print(f"T-statistic: {t_test}\tp-value: {p_val}")


if __name__ == "__main__":

    digits = fetch_digits()

    if digits:
        analyze_distribution(digits)
        analyze_pairs(digits)
        analyze_runs(digits)
