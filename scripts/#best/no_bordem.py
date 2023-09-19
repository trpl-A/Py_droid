import random 
import time 
import sys 
from colorama import Fore 
# ==========================================

def writer(message=str, pause=0.1):
    for char in message:
        sys.stdout.write(char)
        sys.stdout.flush()
        time.sleep(pause)
        # print(char)
    print()


class Get_busy:
    """
    A small program that randomly 
    selects a task, for the use to do.
    Primarily used if someone is bored.
    """
    
    def __init__(self):
        self.duration_of_task = [5, 10, 15, 20, 30, 60]
        self.activities = [
            "read a novel (10mins+)",
            "programming exercises",
            "math exercises",
            "write code",
            "workout",

            "sleep on floor",
            "go for a walk",
            "recite a religious scripture",
            "religious studies",
            "martial arts training",
            
            "dance routine/ training",
            "meditate",
            "30 push-ups",
            "30 squats",
            "100 second plank",
            
            "3 slow-mo push-ups",
            "3 slow-mo squats",
            "talk for a minute about anything (fluency activity)"
            "play the guitar",
            "talk to someone about something",
            
            "talk in Afrikaans",
            "talk in Spanish",
            "learn Afrikaans",
            "learn Spanish",
            "full body calisthenics workout",
            
            "10-minute-3-set workout",
        ]

    
    def block1(self):
        options= []
        title = "Don't get bored"

        print(f"\n{title}")
        print(len(title) * "=")
        time.sleep(2)

        print("(minimum time: 5 minutes)\n")

        # main loop
        looping = True 
        while looping:
            task = random.choice(self.activities)

            sys.stdout.write("activity: ")
            sys.stdout.flush()                 
            time.sleep(1)

            writer(
                f"{(Fore.LIGHTGREEN_EX + task + Fore.RESET)}"
                )
            options.append(task)
            print(options)
            time.sleep(2)

            rerun = input("\nrerun? (y/n) ").lower()
            if rerun == "y" or rerun == "yes":
                continue 

            else:
                looping = False
                print("<session ended>\n")


# ==========================================

obj1 = Get_busy()
# obj1.block1()


# help
# print(help(obj1))
# print(obj1.__doc__)