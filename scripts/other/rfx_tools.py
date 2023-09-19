
import sys
import time 
import random 

class tools:
    def r(x):
        pass 

    def f(x):
        pass 

    # ================================

    def writer(message, time1=0.25):
        for char in message:
            sys.stdout.write(char)
            sys.stdout.flush()
            time.sleep(time1)

    def pad(word=str, spacing=2):
        new = (" " * spacing) + word + (" " * spacing) 
        print(new)

    def password_gen(word="Testing"):
        i = word[0] + word[1] + word[-1]
        n = str(random.randint(99, 1001))

        alpha = "abcdefghijklmonpqrstuvwxyz"
        alpha_list = list(alpha)
        a = random.choice(alpha_list)

        symbol = "!@#$%&*_-"
        symbol_list = list(symbol)
        s = random.choice(symbol_list)
        s1 = random.choice(symbol_list)

        password = s + i + n + a + s1
        return password 

# ***********************************************
m="type the message over here"
tools.writer(m, 0.05)