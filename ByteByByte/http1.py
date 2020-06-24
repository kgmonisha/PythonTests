import requests
import re
requests.get("https://www.google.com/")

req = """GET /index.html HTTP/1.1
Host: localhost
Connection: keep-alive
Cache-Control: max-age=0
Upgrade-Insecure-Requests: 1
User-Agent: Mozilla/5.0 (Windows NT 6.1; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/52.0.2743.116 Safari/537.36
Accept: text/html,application/xhtml+xml,application/xml;q=0.9,image/webp,*/*;q=0.8
Accept-Encoding: gzip, deflate, sdch
Accept-Language: en-US,en;q=0.8"""
lines = req.split('\n')
regex = re.compile(r'([^:]+):\s([\w\W]+)')
dict1 = {}
for line in lines:
    print(line)
    match = regex.search(line)
    if match:
        key = match.group(1)
        value = match.group(2)
        dict1[key] = value
print(dict1)

