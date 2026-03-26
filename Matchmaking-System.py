import os
import random
import time

# ---------------- DATA ----------------
players = []

# ---------------- CLEAR SCREEN ----------------
def clear():
    os.system("cls" if os.name == "nt" else "clear")

# ---------------- RANK SYSTEM ----------------
def get_rank_color(rank):
    if rank < 1000:
        return "\033[91m"   # Bronze (Red)
    elif rank < 1500:
        return "\033[97m"   # Silver (White)
    elif rank < 2000:
        return "\033[93m"   # Gold (Yellow)
    else:
        return "\033[96m"   # Diamond (Cyan)

def get_rank_name(rank):
    if rank < 1000:
        return "Bronze"
    elif rank < 1500:
        return "Silver"
    elif rank < 2000:
        return "Gold"
    else:
        return "Diamond"

# ---------------- GENERATE UNIQUE ID ----------------
def generate_id():
    while True:
        new_id = random.randint(1000, 9999)
        if all(p["id"] != new_id for p in players):
            return new_id

# ---------------- INIT RANDOM PLAYERS ----------------
def init_players():
    names = ["Ace", "Blaze", "Cobra", "Drift", "Echo", "Frost", "Ghost", "Hawk"]
    
    for _ in range(6):
        players.append({
            "id": generate_id(),
            "name": random.choice(names) + str(random.randint(1,99)),
            "rank": random.randint(800, 2500)
        })

# ---------------- ADD PLAYER ----------------
def add_player():
    clear()
    print("➕ ADD PLAYER")
    id = generate_id()
    name = input("Name: ")
    rank = int(input("Rank: "))
    
    players.append({"id": id, "name": name, "rank": rank})
    
    print(f"✅ Added! ID = {id}")
    input("Press Enter...")

# ---------------- SHOW PLAYERS ----------------
def show_players():
    clear()
    
    if not players:
        print("❌ No players in queue")
        input("Press Enter...")
        return

    sorted_players = sorted(players, key=lambda x: x["rank"], reverse=True)

    print("\033[95m")
    print("╔════════════════════════════════════════════╗")
    print("║            🎮 TOP PLAYERS 🎮              ║")
    print("╠════════════════════════════════════════════╣")
    print("║ Pos | Name           | Rank               ║")
    print("╠════════════════════════════════════════════╣")

    for i, p in enumerate(sorted_players, start=1):
        color = get_rank_color(p["rank"])
        reset = "\033[0m"
        rank_name = get_rank_name(p["rank"])
        crown = "👑" if i == 1 else " "
        badge = "🔥" if p["rank"] >= 2000 else ""
        print(f"{color}║ {i:<3} | {p['name']:<14} | {p['rank']} {rank_name} {crown}{badge:<3} ║{reset}")

    print("╚════════════════════════════════════════════╝")
    print("\033[0m")
    input("\nPress Enter...")

# ---------------- MATCHMAKING (เลือกชื่อ) ----------------
def match_players():
    clear()

    if len(players) < 2:
        print("❌ Not enough players")
        input("Press Enter...")
        return

    # ---------------- SHOW LEADERBOARD ----------------
    sorted_players = sorted(players, key=lambda x: x["rank"], reverse=True)
    print("\033[95m")
    print("╔════════════════════════════════════════════╗")
    print("║            🎮 TOP PLAYERS 🎮              ║")
    print("╠════════════════════════════════════════════╣")
    print("║ Pos | Name           | Rank               ║")
    print("╠════════════════════════════════════════════╣")
    for i, p in enumerate(sorted_players, start=1):
        color = get_rank_color(p["rank"])
        reset = "\033[0m"
        rank_name = get_rank_name(p["rank"])
        crown = "👑" if i == 1 else " "
        badge = "🔥" if p["rank"] >= 2000 else ""
        print(f"{color}║ {i:<3} | {p['name']:<14} | {p['rank']} {rank_name} {crown}{badge:<3} ║{reset}")
    print("╚════════════════════════════════════════════╝")
    print("\033[0m")

    # ---------------- CHOOSE MATCH METHOD ----------------
    print("\nChoose matchmaking method:")
    print("1️⃣ Enter your Name")
    print("2️⃣ Random match from queue")
    choice = input("Select: ").strip()

    if choice == "1":
        user_name = input("\nEnter your Name to find a match: ").strip()

        # หา player
        p1 = None
        for p in players:
            if p["name"].lower() == user_name.lower():
                p1 = p
                break

        if not p1:
            print("❌ Name not found")
            input("Press Enter...")
            return

        # หา rank ใกล้ที่สุด
        closest_diff = float('inf')
        p2 = None
        for p in players:
            if p["name"].lower() == p1["name"].lower():
                continue
            diff = abs(p1["rank"] - p["rank"])
            if diff < closest_diff:
                closest_diff = diff
                p2 = p

    elif choice == "2":
        # --- Random match ---
        p1, p2 = random.sample(players, 2)
    else:
        print("❌ Invalid choice")
        input("Press Enter...")
        return

    # ---------------- SHOW MATCH RESULT ----------------
    print("\n🎮 MATCH FOUND!\n")
    print(f"🔥 {p1['name']} ({p1['rank']})  VS  {p2['name']} ({p2['rank']})\n")

    # ลบทั้งสองจาก queue
    players.remove(p1)
    players.remove(p2)

    input("Press Enter...")

# ---------------- RANDOM PLAYERS ----------------
def random_players():
    names = ["Ace", "Blaze", "Cobra", "Drift", "Echo", "Frost", "Ghost", "Hawk"]

    for _ in range(5):
        players.append({
            "id": generate_id(),
            "name": random.choice(names) + str(random.randint(1,99)),
            "rank": random.randint(800, 2500)
        })

    print("🎲 Random players added!")
    input("Press Enter...")

# ---------------- DELETE PLAYER ----------------
def delete_player():
    clear()
    name = input("Enter Name to delete: ").strip()
    
    for p in players:
        if p["name"].lower() == name.lower():
            players.remove(p)
            print(f"✅ {name} deleted!")
            input("Press Enter...")
            return

    print("❌ Name not found")
    input("Press Enter...")

# ---------------- MENU ----------------
def menu():
    while True:
        clear()
        print("\033[95m")
        print("╔════════════════════════════╗")
        print("║   🎮 MATCHMAKING SYSTEM   ║")
        print("╠════════════════════════════╣")
        print("║ 1. ➕ Add Player          ║")
        print("║ 2. 📋 Show Players        ║")
        print("║ 3. 🔥 Match Players       ║")
        print("║ 4. 🎲 Random Players      ║")
        print("║ 5. 🗑 Delete Player       ║")
        print("║ 6. ❌ Exit                ║")
        print("╚════════════════════════════╝")
        print("\033[0m")

        choice = input("Select: ")

        if choice == "1":
            add_player()
        elif choice == "2":
            show_players()
        elif choice == "3":
            match_players()
        elif choice == "4":
            random_players()
        elif choice == "5":
            delete_player()
        elif choice == "6":
            break

# ---------------- RUN PROGRAM ----------------
init_players()
menu()