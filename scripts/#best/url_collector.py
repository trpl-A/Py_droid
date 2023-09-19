# help https://www.youtube.com/watch?v=gCAg8pjYTSs
# adding urls to a list
# use this in for other programs

from googlesearch import search
from colorama import Fore, Back 
import os 

class Urls:
    """
    started:    xx.xx.22
    updated:    19.09.23
    programmer: trpl-A
    """

    def __init__(self, session_name="search"):
        self.results = []
        self.session_name = session_name

  
    def search(self, prompt, num_of_results):
        try:
            for unit in search(prompt, num=5, stop=num_of_results, pause=3):
                print(unit)
                self.results.append(unit + "\n")

        except:
            print("*an error has occurred*")
            print("check your Internet connection")

        # os.remove("google.cookie")


    def save_data(self, prompt):
        save= input("\nSave urls to a textfile? (y/n) ").lower()
        if save == "y":
            try:
                file = open("collection/" + self.session_name + ".txt", "w+")
                file.write(prompt + "\n")
                file.writelines(self.results)
                file.write("<end>")
                print("saving to folder <collection>...")
                print("<data saved>")

            except:
                print("*an error has occurred*")
                print("directory named 'collection' may not exist")
                os.mkdir("collection")
# ******************************************************************

def main():
    os.system("cls")

    # title
    print("URL Collector")
    print("=============")

    # user input 
    name = input(f"\n{Fore.GREEN}Enter a name for this session: {Fore.RESET}")
    search_item = input("\nEnter your prompt: ")
    # num = input("Enter the desired number of results: ")
    num = int(input("Enter the desired number of results: "))

    print()
    obj1 = Urls(name)
    obj1.search(search_item, num)
    obj1.save_data(search_item)
# ==================================

if __name__ == "__main__":
    print(Urls.__doc__)
    # main()
    print("\n<END OF PROGRAM>")
# ==================================