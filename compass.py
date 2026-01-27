import subprocess
import os
from datetime import datetime

def clear_screen():
    """Clears the terminal screen to maintain a clean learning environment."""
    os.system('cls' if os.name == 'nt' else 'clear')

def save_to_log(goal, command):
    """
    Appends the study session data to a local Markdown file.
    This creates a persistent history of the user's DevOps learning journey.
    """
    filename = "LINUX_STUDY_LOG.md"
    timestamp = datetime.now().strftime("%Y-%m-%d %H:%M")
    
    with open(filename, "a", encoding="utf-8") as f:
        f.write(f"\n## Study Session: {timestamp}\n")
        f.write(f"- Goal: {goal}\n")
        f.write(f"- Command Learned: `{command}`\n")
        f.write("-" * 30 + "\n")

def main():
    clear_screen()
    print("---------------------------------------------")
    print("      THE LINUX COMPASS: YOUR STUDY GUIDE    ")
    print("---------------------------------------------")

    goal = input("\nWhat linux task do you need help with today?\n> ")
    if not goal:
        return

    print(f"\n[1/2] Consulting the Copilot Agent...")
    
    payload = f"suggest -p {goal}"
    cmd = ["gh", "copilot", "-i", payload]

    try:
        subprocess.call(cmd, shell=True)
    except Exception as e:
        print(f"Error: {e}")

  
    print("\n" + "-"*45)
    print("           DOCUMENTATION SYNC                ")
    print("---------------------------------------------")
    print("Step: Input the verified command to generate")
    print("your educational breakdown and study log.")
    print("-"*45)
    
    final_cmd = input("\nPaste verified command: ")

    if final_cmd:
        print("\n[2/2] GENERATING EDUCATIONAL BREAKDOWN...")
        explain_payload = f"explain {final_cmd}"
        subprocess.call(["gh", "copilot", "-i", explain_payload], shell=True)
        
        save_to_log(goal, final_cmd)
        print(f"\nSUCCESS: Notes synchronized to LINUX_STUDY_LOG.md.")

if __name__ == "__main__":
    main()
