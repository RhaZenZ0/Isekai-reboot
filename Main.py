import subprocess
import time
import platform

def Reincarnation():
    print("Confirm to start a new life.")
    input_val = input("Please enter 'y' to confirm: ")
    
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
    print("You are transmigrating to another world. Initiating transmigration in 10 seconds...")
    for i in range(10, 0, -1):
        print(f"Transmigration in {i} seconds...", end="\r")
        time.sleep(1)
    print("Transmigrating now!")
    if platform.system() == "Windows":
        subprocess.run(["shutdown", "/r", "/t", "0", "/f"], check=True)
    elif platform.system() == "Darwin" or platform.system() == "Linux":
        subprocess.run(["sudo", "reboot", "now"], check=True)
    else:
        print("Unsupported operating system.")

def summoning():
    print("You are too weak for the summoning and you died, going tho restart life.")
    time.sleep(2)  # Wait for 2 seconds
    restart_life()

if __name__ == "__main__":
    print("Welcome to the Life Restart Program.")
    print("Choose an option:")
    print("1. Reincarnation")
    print("2. Transmigration")
    print("3. Summoning")
    
    choice = input("Enter your choice (1/2/3): ")
    
    if choice == '1':
        Reincarnation()
    elif choice == '2':
        transmigration()
    elif choice == '3':
        summoning()
    else:
        print("Invalid choice. Please select 1, 2, or 3.")
        
