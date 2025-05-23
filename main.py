from db import create_table, add_game, get_all_games, filter_by_status, filter_by_platform


def main():
    create_table()

    while True:
        print("\n🎮 Game Backlog Manager")
        print("1. Add new game")
        print("2. View all games")
        print("3. Exit")
        print("4. Filter by status")
        print("5. Filter by platform")
        choice = input("Choose an option: ")

        if choice == "1":
            title = input("Title: ")
            platform = input("Platform: ")
            genre = input("Genre: ")
            status = input("Status (Backlog, Playing, Completed): ")
            try:
                hours_played = int(input("Hours played: "))
            except ValueError:
                hours_played = 0
            add_game(title, platform, genre, status, hours_played)

        elif choice == "2":
            games = get_all_games()
            if not games:
                print("📭 No games found.")
            else:
                print("\n📋 Your Games:")
                for game in games:
                    print(f"{game[0]}. {game[1]} [{game[2]}] - {game[3]} | {game[4]} ({game[5]} hrs)")

        elif choice == "3":
            print("👋 Exiting...")
            break

        elif choice == "4":
            status = input("Enter status to filter by (Backlog, Playing, Completed): ").title()
            games = filter_by_status(status)
            if not games:
                print("📭 No games found with that status.")
            else:
                print(f"\n🎯 Games with status '{status}':")
                for game in games:
                    print(f"{game[0]}. {game[1]} [{game[2]}] - {game[3]} | {game[4]} ({game[5]} hrs)")

        elif choice == "5":
            platform = input("Enter platform to filter by (e.g., PC, PS5, Switch): ").title()
            games = filter_by_platform(platform)
            if not games:
                print("📭 No games found for that platform.")
            else:
                print(f"\n🎮 Games on platform '{platform}':")
                for game in games:
                    print(f"{game[0]}. {game[1]} [{game[2]}] - {game[3]} | {game[4]} ({game[5]} hrs)")

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
