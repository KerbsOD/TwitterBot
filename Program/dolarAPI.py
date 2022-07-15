import requests
import json

def update_price(): 
   response = requests.get("https://api.bluelytics.com.ar/v2/latest")
   data = response.json()
   with open('./Program/Resources/Precio.json', 'w') as outfile:
      outfile.write(json.dumps(data,indent=2))
   




