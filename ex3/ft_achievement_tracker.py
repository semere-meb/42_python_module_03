#! /usr/bin/env python3


def demo() -> None:
    print("=== Achievement Tracker System ===")

    achievements = {
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

    for player in achievements:
        print(f"Player {player} acievements: {achievements[player]}")

    uniqs_per_player = [set(achievements[p]) for p in achievements]
    uniqs_all = set.union(*uniqs_per_player)
    common_all = set.intersection(*uniqs_per_player)
    alice_bob = \
        set.difference(set(achievements["alice"]), set(achievements["bob"]))

    table = {}
    for player in achievements:
        for achievement in achievements[player]:
            if achievement not in table:
                table[achievement] = 1
            else:
                table[achievement] = 0
    rares = [achievement for achievement in table if table[achievement] == 1]

    print("\n=== Achievement Analytics ===")
    print(f"\nAll unique achievements: {uniqs_all}")
    print(f"Total unique achievements: {len(uniqs_all)}")

    print(f"\nCommon to all players:({list(common_all)})")
    print(f"Rare achievements (1 player): {rares}")

    print(f"\nAlice vs Bob common: {alice_bob}")
    print(f"Alice unique: {set(achievements['alice'])}")
    print(f"Bob unique: {set(achievements['bob'])}")


if __name__ == "__main__":
    demo()
