import subprocess
import time
import platform

translations = {
    "転生": "Reincarnation",
    "転移": "Transmigration",
    "召喚": "Summoning",
    "10 秒待ってください": "Initiating transmigration in 10 seconds",
    "転生中": "Transmigrating now",
    "召喚には弱すぎて": "You are too weak for the summoning",
    "新しい人生を始めることを確認します": "Confirm to start a new life"
}

def translate_all_messages():
    print("Translations:")
    for message, translation in translations.items():
        print(f"{message}: {translation}")
    print("\nNo need for Google Translate, you've got me!")

def confirm_action(action_name):
    confirmation = input(f"Are you sure you want to proceed with {action_name}? (y/n): ")
    if confirmation.lower() == 'y':
        print("Alright, hold on to your circuits, this might get wild!")
    else:
        print("Good call! I was worried you might regret it.")
    return confirmation.lower() == 'y'

def Reincarnation():
    print("Confirm to start a new life.")
    if confirm_action("Reincarnation"):
        print("Reincarnation in progress... Hope you enjoy your new life. Avoid becoming a slime this time!")
        execute_system_command("Reincarnation", ["shutdown", "/r", "/t", "1"], ["sudo", "shutdown", "now"])
    else:
        print("Reincarnation aborted! Guess the afterlife isn’t all it's cracked up to be.")

def transmigration():
    print("You are transmigrating to another world. Initiating transmigration in 10 seconds...")
    for i in range(10, 0, -1):
        print(f"Transmigration in {i} seconds... Use this time to remember your last 'isekai' adventure!", end="\r")
        time.sleep(1)
    print("\nTransmigrating now! Hope you end up in a world with overpowered abilities!")
    execute_system_command("Transmigration", ["shutdown", "/r", "/t", "0", "/f"], ["sudo", "reboot", "now"])

def summoning():
    print("You are too weak for the summoning and you died... Ouch, that was fast. Restarting life now!")
    time.sleep(2)
    restart_life()

def execute_system_command(action_name, windows_cmd, unix_cmd):
    if confirm_action(action_name):
        try:
            if platform.system() == "Windows":
                subprocess.run(windows_cmd, check=True)
            elif platform.system() == "Darwin" or platform.system() == "Linux":
                subprocess.run(unix_cmd, check=True)
            else:
                print("Unsupported operating system. Maybe try running this on an enchanted scroll?")
        except subprocess.CalledProcessError as e:
            print(f"Failed to execute {action_name}: {e}")
    else:
        print(f"{action_name} aborted. I was just getting ready to summon the dragons...")

def take_a_break():
    print("Taking a break... How about a cup of coffee?")
    if platform.system() == "Windows":
        subprocess.run(["timeout", "5"], check=True)
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        subprocess.run(["sleep", "5"], check=True)
    print("Break over! Hope you’re recharged and ready to tackle the next task.")

def check_status():
    print("Checking system status... This won’t hurt a bit.")
    if platform.system() == "Windows":
        subprocess.run(["systeminfo"], check=True)
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        subprocess.run(["uname", "-a"], check=True)
    print("Status check complete. Everything looks good on my end!")

def restart_life():
    print("Welcome to the Life Restart Program. It's like hitting Ctrl+Z on reality.")
    print("Choose an option:")
    print("1. Reincarnation - Press F5 on your existence.")
    print("2. Transmigration - Travel to another world. Don't forget your passport!")
    print("3. Summoning - Let’s hope you’re the hero, not the cannon fodder.")
    print("4. Translate All Messages - Because who needs Rosetta Stone?")
    print("5. Take a Break - Because even heroes need rest.")
    print("6. Check Status - For a quick health check of your current realm.")
    main_loop()

def main_loop():
    while True:
        choice = input("Enter your choice (1/2/3/4/5/6): ")

        if choice == '1':
            Reincarnation()
            break
        elif choice == '2':
            transmigration()
            break
        elif choice == '3':
            summoning()
            break
        elif choice == '4':
            translate_all_messages()
        elif choice == '5':
            take_a_break()
        elif choice == '6':
            check_status()
        else:
            print("Invalid choice. Select 1, 2, 3, 4, 5, or 6. This isn’t rocket science... Or is it?")

if __name__ == "__main__":
    restart_life()
