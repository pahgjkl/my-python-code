import requests
import json
respont = requests.get("https://top.baidu.com/api/board?platform=wise&tab=realtime")
data = respont.json()
formatted_data = json.dumps(data, indent=4, ensure_ascii=False)
print(formatted_data)