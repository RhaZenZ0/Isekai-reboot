import os
import time
import platform

def restart_life():
    print("Confirm to start a new life.")
    input_val = input("Please enter 'y' to confirm: ")
    
    if input_val.lower() == 'y':
        if platform.system() == "Windows":
            os.system("shutdown /r /t 1")
        elif platform.system() == "Darwin" or platform.system() == "Linux":
            os.system("sudo shutdown now")
        else:
            print("Unsupported operating system.")
    else:
        exit()

def transmigration():
    print("You are transmigrating to another world. Initiating transmigration in 10 seconds...")
    for i in range(10, 0, -1):
        print(f"Transmigration in {i} seconds...", end="\r")
        time.sleep(1)
    print("Transmigrating now!")
    if platform.system() == "Windows":
        os.system("shutdown -t 0 -r -f")
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        os.system("sudo reboot now")
    else:
        print("Unsupported operating system.")

def summoning():
    print("You are too weak for the summoning. Choosing to restart life.")
    restart_life()

if __name__ == "__main__":
    print("Welcome to the Life Restart Program.")
    print("Choose an option:")
    print("1. Restart Life")
    print("2. Transmigration")
    print("3. Summoning")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        restart_life()
    elif choice == '2':
        transmigration()
    elif choice == '3':
        summoning()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
