import time
from datetime import datetime
import requests
req = requests.get("https://github.com")
if req.status_code == 200:
    print("github is ok")

print(datetime.now())
time.sleep(10)
print(datetime.now())