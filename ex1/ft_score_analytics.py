#! /usr/bin/env python3


import sys


def analyze_scores():
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage:" +
            " python3 ft_score_analytics.py <score1> <score2> ...")
    else:
        scores: list = []
        for arg in sys.argv[1:]:
            try:
                scores += [int(arg)]
            except ValueError:
                pass

        try:
            average = sum(scores) / len(scores)
            max_score = max(scores)
            min_score = min(scores)
            range = max_score - min_score
        except (ZeroDivisionError, ValueError):
            average = "No scores"
            max_score = "No scores"
            min_score = "No scores"
            range = "No scores"

        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average socre: {average}")
        print(f"High score: {max_score}")
        print(f"Low socre: {min_score}")
        print(f"Score range: {range}")


if __name__ == "__main__":
    analyze_scores()
