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
        print(f"{message}: {translate_message(message)}")

def Reincarnation():
    print("Confirm to start a new life.")
    input_val = input("Please enter 'y' to confirm (yes/いいえ): ")
    
    if input_val.lower() == 'y':
        if platform.system() == "Windows":
            subprocess.run(["shutdown", "/r", "/t", "1"], check=True)
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            subprocess.run(["sudo", "shutdown", "now"], check=True)
        else:
            print("Unsupported operating system.")
    else:
        print("There's no kami in the vicinity, reincarnation aborted!")
        time.sleep(2)  # Wait for 2 seconds
        exit()

def transmigration():
    print("You are transmigrating to another world. Initiating transmigration in 10 seconds (10 秒待ってください)...")
    for i in range(10, 0, -1):
        print(f"Transmigration in {i} seconds (残り {i} 秒)...", end="\r")
        time.sleep(1)
    print("Transmigrating now (転生中)!")
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/r", "/t", "0", "/f"], check=True)
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        subprocess.run(["sudo", "reboot", "now"], check=True)
    else:
        print("Unsupported operating system.")

def summoning():
    print("You are too weak for the summoning and you died, going to restart life (召喚には弱すぎて死んでしまいました、人生を再起動します).")
    time.sleep(2)  # Wait for 2 seconds
    restart_life()

def restart_life():
    print("Welcome to the Life Restart Program (人生リスタートプログラムへようこそ).")
    print("Choose an option:")
    print("1. Reincarnation (転生)")
    print("2. Transmigration (転移)")
    print("3. Summoning (召喚)")
    print("4. Translate All Messages")
    choice()

def choice():
    choice = input("Enter your choice (1/2/3): ")

    if choice == '1':
        Reincarnation()
    elif choice == '2':
        transmigration()
    elif choice == '3':
        summoning()
    elif choice == '4':
        translate_all_messages()
    else:
        print("Invalid choice. Please select 1, 2, 3, or 4 :)")
        choice()# Restart the program if the choice is invalid

if __name__ == "__main__":
    restart_life()
