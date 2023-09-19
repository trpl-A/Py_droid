
# help https://www.youtube.com/watch?v=F43rgxq4CKw&pp=ygUOcHl0aG9uIGZhc3RhcGk%3D

import requests


url = "http://127.0.0.1:8000"
req = requests.get(url)

# print(req.text)
print(req.json())
