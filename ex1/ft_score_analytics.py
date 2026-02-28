import sys


def analyze_scores():
    print("=== Player Score Analytics ===")

    if len(sys.argv) == 1:
        print(
            "No scores provided. Usage:" +
            " python3 ft_score_analytics.py <score1> <score2> ..."
        )
    else:
        scores: list = [int(score) for score in sys.argv[1:]]
        print(f"Scores processed: {scores}")
        print(f"Total players: {len(scores)}")
        print(f"Total score: {sum(scores)}")
        print(f"Average socre: {sum(scores) / len(scores)}")
        print(f"High score: {max(scores)}")
        print(f"Low socre: {min(scores)}")
        print(f"Score range: {max(scores) - min(scores)}")


if __name__ == "__main__":
    analyze_scores()
