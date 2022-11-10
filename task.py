import requests 
import json
import time
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

gauth = GoogleAuth
drive = GoogleDrive(gauth)

API_url = ""
req_response = requests.get(API_url)

fname = time.strftime("%Y%m%d-%H%M%S")
dump_file = fname + ".json"
with open(dump_file, "w") as outfile:
    json.dump(req_response, outfile)

google_file = drive.CreateFile({'parents': [{'id': '### folder ID ###'}]})
google_file.SetContentFile(dump_file)
google_file.Upload()
