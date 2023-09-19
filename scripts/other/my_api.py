
from fastapi import FastAPI
from googlesearch import search
from GoogleNews import GoogleNews
# help https://www.youtube.com/watch?v=F43rgxq4CKw&pp=ygUOcHl0aG9uIGZhc3RhcGk%3D

# =====================================================

app = FastAPI()

def greeting(name):
    print("Hello", name)


@app.get("/")
async def root():
    return {
        "root_dir": "this is the root directory",
        "text": "this is text",
        "number": 126,
        "list": [],
        "is_new_api": True,
        "new_dict": {"data": "more data"},
        "url": "https://www.google.com",
        "function": greeting("Jacob"),
        }
# =====================================================



@app.get("/page0/{word}")
async def to_ascii(word: str):
        chars = []
        for char in word:
            char = ord(char) 
            chars.append(char)

        return {"ascii_values": chars}
# =====================================================


@app.get("/page1/{num}")
async def num_systems(num: int):
    bin_form = bin(num)
    oct_form = oct(num)
    hex_form = hex(num)
    
    return {
        num: {"bin": bin_form, 
            "oct": oct_form, 
            "hex": hex_form
            }
        } 
# =====================================================


@app.get("/page2/q={query}")
async def search_google(query: str, num_results=5):
    results_urls = []
    results_dict = {}

    count = 0
    for i in search(query, num=5, stop=num_results, pause=1):
        # results_urls.append(i)
        results_dict[count] = i
        count +=1

    # return {"results": [result_urls]}
    return results_dict
# =====================================================


@app.get("/news_all/q={query}")
async def news_all(query):
    g = GoogleNews()
    # "intitle:'cput' after:2022"

    # g.get_news(query)
    g.search(query)

    # list of news dicts
    n = g.result() 

    return n
# =====================================================
