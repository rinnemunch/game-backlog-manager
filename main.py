from db import create_table, add_game


def main():
    create_table()

    print("🎮 Add a new game to your backlog")
    title = input("Title: ")
    platform = input("Platform: ")
    genre = input("Genre: ")
    status = input("Status (e.g. Backlog, Playing, Completed): ")
    try:
        hours_played = int(input("Hours played: "))
    except ValueError:
        hours_played = 0

    add_game(title, platform, genre, status, hours_played)


if __name__ == "__main__":
    main()
