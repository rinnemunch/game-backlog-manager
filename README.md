# 🎮 Game Backlog Manager

A simple command-line app to track your video game backlog using Python and SQLite.

---

## 🚀 Features

✅ Add new games with title, platform, genre, status, and hours  
✅ View all games in your backlog  
✅ Filter games by platform or status  
✅ Update game info by ID  
✅ Delete games from the backlog  
✅ Fully stored in a local SQLite database

---

## 🖼️ Preview

Coming soon — CLI screenshots or demo GIF

---

## 💻 How to Run

1. **Clone the repo**
```bash
git clone https://github.com/rinnemunch/game-backlog-manager.git
cd game-backlog-manager
``` 

Create and activate a virtual environment 
````bash
python -m venv venv
source venv/bin/activate  # Windows: venv\Scripts\activate
````

Install dependencies 
````bash
pip install -r requirements.txt
```` 

Run the app 
````bash
python main.py
````  

📁 Structure 
db.py       # All database functions (CRUD) 
games.db    # SQLite database (auto-generated)
main.py     # CLI menu + logic 

🧪 Sample Menu 
````bash
🎮 Game Backlog Manager
1. Add new game
2. View all games
3. Exit
4. Filter by status
5. Filter by platform
6. Delete a game
7. Edit a game
````  
🔓 License
MIT — Free to use and modify