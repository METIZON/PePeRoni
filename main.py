# beginning 
import requests

p = requests.get('link')
out = open("img.jpg", "wb")
out.write(p.content)
out.close()
