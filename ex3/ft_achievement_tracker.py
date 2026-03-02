#! /usr/bin/env python3


def demo() -> None:
    achvs = {
        "alice": [
            "first_blood",
            "pixel_perfect",
            "speed_runner",
            "first_blood",
            "first_blood",
        ],
        "bob": [
            "level_master",
            "boss_hunter",
            "treasure_seeker",
            "level_master",
            "level_master",
        ],
        "charlie": [
            "treasure_seeker",
            "boss_hunter",
            "combo_king",
            "first_blood",
            "boss_hunter",
            "first_blood",
            "boss_hunter",
            "first_blood",
        ],
        "diana": [
            "first_blood",
            "combo_king",
            "level_master",
            "treasure_seeker",
            "speed_runner",
            "combo_king",
            "combo_king",
            "level_master",
        ],
        "eve": [
            "level_master",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
            "first_blood",
            "treasure_seeker",
        ],
        "frank": [
            "explorer",
            "boss_hunter",
            "first_blood",
            "explorer",
            "first_blood",
            "boss_hunter",
        ],
    }

    player_achvs = {player: set(achvs[player]) for player in achvs}
    distinct_achvs = \
        set.union(*[player_achvs[player] for player in player_achvs])
    common_achvs = \
        set.intersection(*[player_achvs[player] for player in player_achvs])
    alice = player_achvs["alice"]
    bob = player_achvs["bob"]
    all_achivements = [achv for player in achvs for achv in achvs[player]]
    counts = {achv: 0 for achv in distinct_achvs}
    for achv in all_achivements:
        counts[achv] += 1
    rares = {achv for achv in counts if counts[achv] == 1}

    print("=== Achievement Tracker System ===\n")
    for player in achvs:
        print(f"Player {player} acievements: {player_achvs[player]}")

    print("\n=== Achievement Analytics ===")
    print(f"All unique achievements: {distinct_achvs}")
    print(f"Total unique achievements: {len(distinct_achvs)}")

    print("\nCommon to all players: ", end='')
    print(f"({common_achvs if common_achvs != set() else '{}'})")
    print(f"Rare achievements (1 player): {rares}")

    print(f"\nAlice vs Bob common: {alice & bob}")
    print(f"Alice unique: {alice - bob}")
    print(f"Bob unique: {bob - alice}")


if __name__ == "__main__":
    demo()
