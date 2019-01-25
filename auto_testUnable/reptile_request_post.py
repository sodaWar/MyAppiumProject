import requests
import json
import hashlib

password = "naiwu3425"
password_md5 = hashlib.md5(password)
password_encrypt = password_md5.hexdigest()

values = {"identity": "893026753@qq.com", "type": 0, "password": password_encrypt, "os": 1}
delivery_data = json.dumps(values)
delivery_url = "http://api.test.sokafootball.com:8092/register/email"
delivery_headers = {"Content-Type": "application/json"}
r = requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)
print r.status_code
print r.text
print r.encoding
