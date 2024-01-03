print("\033[1;32;40m    ________     __  ___                 __  \033[0m")
print("\033[1;32;40m   /  _/ __ \   /  |/  /___  _________  / /_ \033[0m")
print("\033[1;32;40m   / // /_/ /  / /|_/ / __ \/ ___/ __ \/ __ \\\033[0m")
print("\033[1;32;40m _/ // ____/  / /  / / /_/ / /  / /_/ / / / /\033[0m")
print("\033[1;32;40m/___/_/      /_/  /_/\____/_/  / .___/_/ /_/ \033[0m")
print("\033[1;32;40m                              /_/           \033[0m")
import sys
import time
import subprocess
import warnings
import re
import socket
warnings.filterwarnings("ignore", category=DeprecationWarning)
warnings.filterwarnings("ignore", category=DeprecationWarning, module="protonvpn_cli")

def run_command(command):
    try:
        subprocess.run(command, check=True, shell=True)
    except subprocess.CalledProcessError as e:
        print(f"Error: {e}")
        sys.exit(1)

def lively_print(message):
    symbols = ["🌟", "🚀", "🎉", "💡", "🔧"]
    for symbol in symbols:
        sys.stdout.write(f"\r{symbol} {message} {symbol}")
        sys.stdout.flush()
        time.sleep(0.2)
    print()

def loading_animation():
    animation_states = ["⣾", "⣷", "⣿", "⣶"]
    for _ in range(10):  # Rotate the loading circle 10 times
        for state in animation_states:
            sys.stdout.write(f"\rSetting up Environment... {state}")
            sys.stdout.flush()
            time.sleep(0.1)
    print()

# Print lively ASCII art
lively_print("Welcome to IP MORPH by William Selby")

# Run the commands with lively loading animation
loading_animation()
run_command("sudo apt-get update")
run_command("sudo dpkg -i protonvpn-stable-release_1.0.3_all.deb")

try:
    run_command("sudo apt-get install protonvpn-cli")
except subprocess.CalledProcessError as e:
    lively_print("Failed to install proton-cli tool. Please note that you cannot be in root.")
    sys.exit(1)

# Prompt the user for ProtonVPN username
lively_print("ProtonVPN Setup Complete!")
protonvpn_username = input("👤 Enter your ProtonVPN username: ")

#

# Run protonvpn-cli login command with the provided username
# ... (previous code)
#
# Run protonvpn-cli login command with the provided username
# Run protonvpn-cli status command to check login status
# Run protonvpn-cli whoami command to check login status
# Run protonvpn-cli whoami command to check login status
# Function to check if the provided IP address is reachable
def is_ip_reachable(ip_address):
    try:
        # Create a socket to the provided IP address on a common port (e.g., 80 for HTTP)
        with socket.create_connection((ip_address, 80), timeout=2):
            return True
    except OSError:
        return False

# IP address of a ProtonVPN server to check against
protonvpn_ip_address = "xxx.xxx.xxx.xxx"  # Replace with an actual ProtonVPN server IP

# Check if the ProtonVPN server is reachable (assuming you're already connected)
if is_ip_reachable(protonvpn_ip_address):
    lively_print("User is already connected to ProtonVPN. Proceeding with the script.")
else:
    lively_print("User is not connected to ProtonVPN. Logging in...")

    # Run protonvpn-cli login command with the provided username
    login_command = f"protonvpn-cli login {protonvpn_username}"
    try:
        run_command(login_command)
        lively_print("Login successful. Proceeding with the script.")
    except subprocess.CalledProcessError as e:
        lively_print(f"Error during login. Return code: {e.returncode}")
        sys.exit(1)

# ... (remaining code)

# ... (remaining code)

# Prompt the user for the rotation interval in seconds
rotation_interval = int(input("\n⏰ How often would you like your IP address to rotate? Enter the rotation interval in seconds: "))

# IP rotation loop
try:
    while True:
        subprocess.call("protonvpn-cli d", shell=True)
        subprocess.call("protonvpn-cli c -r", shell=True)

        # Add a print statement after IP rotation
        lively_print("IP successfully changed!")

        # Retrieve and print the current IP address
        current_ip_command = "curl -s ifconfig.me"
        current_ip = subprocess.check_output(current_ip_command, shell=True, text=True).strip()
        lively_print(f"🌐 Current IP address: {current_ip}")

        time.sleep(rotation_interval)

except KeyboardInterrupt:
    # Handle KeyboardInterrupt (Ctrl+C) to gracefully exit the loop
    lively_print("\nIP rotation stopped. Exiting...")
