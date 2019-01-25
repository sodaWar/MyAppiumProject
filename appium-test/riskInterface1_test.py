# coding=utf-8
import requests
import json
from sdgo_request_post_test import unicode2str,signHeaders


def limitQuery(url,userId, schooling, marriage,professional,workExperience,company,method):
    # 返回：{"code": 1000000,"msg": "成功","phone": null}
    userId, schooling, marriage, professional, workExperience, company = map(unicode2str, [userId, schooling, marriage,professional,workExperience,company])
    payload = ''
    response = ''
    if method == 'phone':
        payload = json.dumps(
            dict(userId = userId, schooling=schooling, marriage=marriage,professional=professional,workExperience=workExperience,company=company), ensure_ascii=False)
    elif method == 'Form':
        payload = dict(userId = userId, schooling=schooling, marriage=marriage,professional=professional,workExperience=workExperience,company=company)
    headers = signHeaders(payload,method)
    if method == 'Data':
        response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    elif method == 'Form':
        response = requests.post(url=url, data=payload, timeout=5)
    # assert response.status_code == 200                                                          # 断言assert的作用是判断接下来的语句是否正确，如果断言成功即判断的布尔值返回为true,那么不执行任何操作,如果断言不成功,会触发AssertionError返回报错信息
    print(response.status_code)
    print(response.text)
    return response
    # text = response.text.split('phone')
    # print(text[1])

def limitQuery2(url,userId, type,data,method):
    # 返回：{"code": 1000000,"msg": "成功","phone": null}
    userId,type,data = map(unicode2str, [userId, type,data])
    payload = ''
    response = ''
    if method == 'phone':
        payload = json.dumps(
            dict(userId=userId, type = type,data=data), ensure_ascii=False)
    elif method == 'Form':
        payload = dict(userId=userId, type = type,data = data)
    headers = signHeaders(payload,method)
    if method == 'Data':
        response = requests.post(url = url,  data=payload,headers=headers, timeout=5)
    elif method == 'Form':                                                                       # Form传递的数据,不能加headers,否则会错误！！至于为什么之后查看原因！
        response = requests.post(url=url, data=payload, timeout=5)
    # assert response.status_code == 200                                                          # 断言assert的作用是判断接下来的语句是否正确，如果断言成功即判断的布尔值返回为true,那么不执行任何操作,如果断言不成功,会触发AssertionError返回报错信息
    print(response.status_code)
    print(response.text)
    return response
    # text = response.text.split('phone')
    # print(text[1])


if __name__ == "__main__":

    # url1 = "http://116.62.67.80:9050/baseVerify/faceErrorCorrect"                                   # 身份证纠错  （参数错误时报系统异常）
    # url1 = "http://116.62.67.80:9050/tjVerify/apiVerify"                                            # 天机api认证
    # url1 = "http://116.62.67.80:9050/baseVerify/userAmount"                                         # 用户额度查询 (form提交)
    # url1 = "http://116.62.67.80:9050/riskVerify/zhiMaAuth"                                          # 芝麻分认证 （form提交）
    # url1 = "http://116.62.67.80:9050/baseVerify/addContacts"                                        # 手机通讯录
    url1 = "http://116.62.67.80:9050/baseVerify/addSelfContacts"                                    # 手机通话和短信记录(form提交,这里注意data的值为以下该形式！)
    # url1 = "http://116.62.67.80:9050/baseVerify/channelSelect"                                      # 实名渠道选择 （form提交,channelrealName为ocr）
    # url1 = "http://116.62.67.80:9050/baseVerify/faceAuthentication"                                 # 实名认证
    # url1 = "http://116.62.67.80:9050/baseVerify/stLivingCheck"                                      # 活体认证  (系统异常)
    # url1 = "http://116.62.67.80:9050/baseVerify/addUserInfo"                                        # 用户信息认证
    # url1 = "http://116.62.67.80:9050/tjVerify/operatorVerify"                                       # 运营商认证   (form提交)
    # url1 = "http://116.62.67.80:9050/baseVerify/risk"                                               # 订单过风控
    # url1 = "http://192.168.1.133:9050/tjVerify/operatorVerify"

    userId = 'f000212cb3434a0db94fe1f8dbcb749d'
    # schooling = '初中'
    # marriage = '未婚'
    # professional = '教师'
    # workExperience = '五年'
    # company = '北京小学'
    # channel = 'faceid'
    # cardrealNameFont = '00110101001111010101'
    # cardrealNameBack = '10000111010010101111'
    # realName = '洪乃武'
    # phone = '17348518942'
    # idCard = '360281199312211010'
    types = '1'
    data = "[{'name': 'laozhang', 'formatted_number': '17348518942', 'location': 'jiangxi', 'duration': '5', 'type': '1', 'matched_number': '18897983780'}]"

    limitQuery2(url1, userId,types,data,'Form')
    # limitQuery(url1, userId,schooling,marriage,professional,workExperience,company,'Data')



