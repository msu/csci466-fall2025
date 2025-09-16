
import requests

r = requests.get("http://v2.jokeapi.dev/joke/Any?safe-mode")

print(r.status_code)
print(r.headers)
print(r.content)

print(r.text)   

r = requests.get("http://3.143.230.75/file/hello.txt")

print(r.text)
output = open("output.html","w")
output.write(r.text)
output.close()
