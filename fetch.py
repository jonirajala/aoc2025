import requests
import sys
import os
from vars import cookies, headers

day = sys.argv[1]

response = requests.get(f'https://adventofcode.com/2025/day/{day}/input', cookies=cookies, headers=headers)

os.makedirs(f"day{day}", exist_ok=True)
open(os.path.join(f"day{day}", "solve.py"), 'a').close()
with open(os.path.join(f"day{day}", "data.txt"), "w") as f: f.write(response.text)