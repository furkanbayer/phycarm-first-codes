import datetime
import os

while True:
    print("\n" + "=" * 40)
    print("📘 DIGITAL DIARY v1.0")
    print("=" * 40)
    print("1. ✍️  Write New Entry")
    print("2. 📖 Read Past Entries")
    print("3. ❌ Exit")

    choice = input("Enter your choice (1-3): ")

    if choice == '1':
        timestamp = datetime.datetime.now().strftime("%d.%m.%Y - %H:%M")

        print(f"\n🕒 Date: {timestamp}")
        entry = input("Dear Diary: ")

        with open("my_diary.txt", "a", encoding="utf-8") as file:
            file.write(f"\n--- {timestamp} ---\n")
            file.write(f"{entry}\n")
            file.write("-" * 30)

        print("✅ Saved successfully!")

    elif choice == '2':
        if os.path.exists("my_diary.txt"):
            print("\n" + "~" * 20)
            print("📖 YOUR PAST ENTRIES:")

            with open("my_diary.txt", "r", encoding="utf-8") as file:
                print(file.read())

            print("~" * 20)
        else:
            print("\n⚠️ You haven't written anything yet!")

    elif choice == '3':
        print("Goodbye! Your secrets are safe with me. 🔒")
        break

    else:
        print("Invalid input, please try again.")
