tasks = []

# ─── FUNCTION 1: Task Add Karna ───────────────────────────
# "add_task" naam ka function define kiya
def add_task():
    # User se naya task lo
    task = input("Naya task likho: ")
    # tasks list mein add karo
    tasks.append(task)
    # Confirm karo ke task add ho gaya
    print(f"✅ '{task}' add ho gaya!")

# ─── FUNCTION 2: Tasks Dekhna ─────────────────────────────
# "view_tasks" naam ka function define kiya
def view_tasks():
    # Check kiya ke list mein koi task hai ya nahi
    if len(tasks) == 0:
        # Agar list khali hai toh yeh message dikhao
        print("Koi task nahi hai abhi.")
    else:
        # Agar tasks hain toh heading print karo
        print("\n--- Tumhari To-Do List ---")
        # enumerate() — har task ke saath uska number bhi deta hai (1 se shuru)
        # i = number (1,2,3...), task = task ka naam
        for i, task in enumerate(tasks, 1):
            # Har task ko uske number ke saath print karo
            print(f"{i}. {task}")

# ─── FUNCTION 3: Task Delete Karna ────────────────────────
# "delete_task" naam ka function define kiya
def delete_task():
    # Pehle saari tasks dikhao taaki user decide kar sake
    view_tasks()
    # Agar list khali hai toh function yahan se band ho jaye
    if len(tasks) == 0:
        return                        # function se bahar nikal jao
    # User se poochho ke konsa number wala task delete karna hai
    # int() isliye kyunke input() string deta hai, hume number chahiye
    num = int(input("Konsa task delete karna hai? (number likho): "))
    # Check karo ke diya hua number valid hai ya nahi
    # 1 se kam ya list ki size se zyada nahi hona chahiye
    if 1 <= num <= len(tasks):
        # pop(num-1) — us position se task nikal ke "removed" mein save karo
        # num-1 isliye kyunke list 0 se start hoti hai, user 1 se sochta hai
        removed = tasks.pop(num - 1)
        # Batao ke konsa task delete hua
        print(f"🗑️ '{removed}' delete ho gaya!")
    else:
        # Agar number range se bahar tha
        print("Galat number!")

# ─── MAIN LOOP ────────────────────────────────────────────
# while True — yeh loop tab tak chalta rahega jab tak "break" na mile
while True:
    # Har baar menu print karo
    print("\n===== To-Do List =====")
    print("1. Task add karo")
    print("2. Tasks dekho")
    print("3. Task delete karo")
    print("4. Exit")
    # User se choice lo
    choice = input("Choice karo (1-4): ")

    # Agar '1' choose kiya toh add_task function chalao
    if choice == '1':
        add_task()
    # Agar '2' choose kiya toh view_tasks function chalao
    elif choice == '2':
        view_tasks()
    # Agar '3' choose kiya toh delete_task function chalao
    elif choice == '3':
        delete_task()
    # Agar '4' choose kiya toh program band karo
    elif choice == '4':
        print("Bye! 👋")
        break        # while loop yahan tod diya — program khatam
    # Agar koi aur key daali jo 1-4 mein nahi
    else:
        print("Galat choice, dobara try karo!")
