from db import create_table, add_game, get_all_games


def main():
    create_table()

    while True:
        print("\n🎮 Game Backlog Manager")
        print("1. Add new game")
        print("2. View all games")
        print("3. Exit")
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

        else:
            print("❌ Invalid choice.")


if __name__ == "__main__":
    main()
