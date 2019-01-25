# -* encoding:utf-8 *-
import requests
import json
import hashlib

# password = "naiwu3425"
# password_md5 = hashlib.md5(password)
# password_encrypt = password_md5.hexdigest()
#
# values = {"identity": "893026753@qq.com", "type": 0, "password": password_encrypt, "os": 1}
# delivery_data = json.dumps(values)
# delivery_url = "http://api.test.sokafootball.com:8092/register/email"
# delivery_headers = {"Content-Type": "application/json"}
# r = requests.post(url=delivery_url, data=delivery_data, headers=delivery_headers)
# print r.status_code
# print r.text
# print r.encoding

# 比赛进球的推送接口
def match_push_phrase():
    time = 48
    type = 'goal'
    title = 'Goal'
    matchId = 50762648

    values = {"time" : time,"type" : type,"title" : title,"matchId" : matchId}
    delivery_data = json.dumps(values)
    delivery_url = 'http://api.test.sokafootball.com/match/push_phrase'
    delivery_headers = {"Content-Type" : "application/json"}
    requests.post(url=delivery_url,data=delivery_data,headers=delivery_headers)

#回复用户的接口
def feedback_message_add(uid):
    message = 'test reply user message'
    sourceId = uid
    toId = uid
    values = {"message":message,'sourceId':sourceId,'toId':toId}
    delivery_data = json.dumps(values)
    delivery_url = 'http://api.admin.test.sokafootball.com/admin/feedback/message/add'
    delivery_headers = {"Content-Type" : "application/json"}
    requests.post(url=delivery_url,data=delivery_data,headers=delivery_headers)
