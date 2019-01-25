# -* encoding:utf-8 *-
import requests
import time
import json
import cgi,cgitb
import threading as thd

#match页面中subscribe数据接口请求方法
def match_reptile():
    now = int(round(time.time() * 1000))                #python的时间戳是以秒为单位输出的float,通过把秒转换毫秒的方法获得13位的时间戳
    print now
    now1 = time.time() * 1000

    values = {"uid": "ea99d0954d508888975a18768c6f443f", "startTime": now , "endTime": now , "isback": 0}
    re_url = "http://api.test.sokafootball.com/match/match_list/subscribe"
    r = requests.get(url = re_url,params = values)
    end = r.text                                        #获取接口返回的数据,json格式的数据
    end_json = json.loads(end)      #将json编码的字符串转换回一个python数据结构,该方法是将json数据库解码,而json.dump()是将字符串编码成json数据
    startTime = end_json['data']['startTime']
    endTime = end_json['data']['endTime']
    result = end_json['data']['list']                   #根据匹配字典中的键来查询相应的值
    s1 = len(result)
    print s1                                            #list中的内容长度，该list为数列，即数列中有多少个值，只是每个值又是一个元组
    print startTime,endTime
    # print result
    # a = result[1]                                     #list的索引为1的值，该值为元组
    # b = a['matchId']                                  #该元素的键matchId的值
    # print a
    # print b
    # for i in range(len(result)):
    #     result1 = result[i]
    #     # result_match = result['gameweek']
    #     print result1
        # print result_match
    s3 = s1
    for i in range(100):
        values = {"uid": "ea99d0954d508888975a18768c6f443f", "startTime": startTime, "endTime": endTime, "isback": 0}
        r = requests.get(url=re_url, params=values)
        end = r.text
        end_json = json.loads(end)
        # print end_json
        startTime = end_json['data']['startTime']
        endTime = end_json['data']['endTime']
        result = end_json['data']['list']
        s2 = len(result)
        if s2 == 0:
            print '数据已拉完'
            break
        else:
            s3 = s3 + s2                #注意该方式，要想使得每次循环后的结果都能够相加，那每次循环后的S3的值必须变化，所以s3在定义时需要定义在循环外面
            print s3                    #例如上面的s3=s1，只是初始化s3的值而已，将s3的值初始化成s1的值,然后每次循环后s3的值就能够发生变化，循环相加
    return s3

            # print startTime, endTime

#竞猜页面接口比赛数据返回方法
def match_prediction():
    re_url = "http://api.test.sokafootball.com/prediction/match"
    r = requests.get(url=re_url)
    end = r.text                # 获取接口返回的数据,json格式的数据
    end_json = json.loads(end)  # 将json编码的字符串转换回一个python数据结构,该方法是将json数据库解码，而json.dump()是将字符串编码成json数据
    # print end_json

    a = []
    length = len(end_json['data'])
    for i in range(length):
        matchId1 = end_json['data'][i]
        matchId2 = matchId1['matchDTO']['matchId']
        a.append(matchId2)
    return a

#访问路径页面查询负号数据
def page_count():
    for i in range(118):
        start = "2017-11-19 00:00:00"
        end = "2017-11-20 00:00:00"
        size = 50
        page = i + 1
        print page
        values = {"start" : start ,"end" : end,"page" : page,"size" : size}
        re_url = "http://api.admin.sokafootball.com/admin/metrics/path"
        r = requests.get(url=re_url , params = values)
        end = r.text
        end_json = json.loads(end)
        list = end_json['data']['list']

        for m in range(len(list)):
            path_json = list[m]
            path_data1 = path_json['data']
            a = '[-'
            path_data2 = path_data1.encode("utf-8")                         #将unicode类型的数据转换成str类型的数据，decode()方法是效果相反
            if path_data2.find(a) != -1:
                print '该页面存在负数'
                break
    print '查询结束，暂无结果'

#用户竞猜历史记录接口请求
def prediction_history():
    rs_url = 'http://api.test.sokafootball.com/prediction/history'
    values = {"uid" : 'ea99d0954d508888975a18768c6f443f', "page" : 0, "size" : 10}
    r = requests.get(url = rs_url,params = values)
    end = r.text
    end_json = json.loads(end)
    data1 = end_json['data'][0]
    try:
        data2 = data1['ratio']                                  #未结束竞猜时，接口返回的数据中该竞猜记录没有ratio字段,所以查找该字段时需要捕获异常
        print data2
        return 1
    except KeyError:
        print '暂未找到'
        return 0

#比赛直播接口请求
def match_live():
    re_url = "http://api.test.sokafootball.com/match/live/available"
    r = requests.get(url=re_url)
    end = r.text
    end_json = json.loads(end)

    a = []
    length = len(end_json['data'])
    for i in range(length):
        matchId1 = end_json['data'][i]
        matchId2 = matchId1['matchId']
        a.append(matchId2)
    return a

#文章列表接口请求
def article_list():
    re_url = "http://api.test.sokafootball.com/article/v2/list"
    uid = 'e4593e828dc3f5166eca2c471c56e0d0'
    size = 10
    a = []
    for i in range(10):
        page = i
        values = {"uid": uid, "page": page, "size": size}
        r = requests.get(url=re_url, params=values)
        end = r.text
        end_json = json.loads(end)
        data = end_json['data']
        for i in range(len(data)):
            title = data[i]['title']
            a.append(title)
    return a

#用户兑换商品后再系统后台显示的记录接口请求，即系统后台兑换管理接口
def point_goodRecord(uid):
    re_url = "http://api.test.sokafootball.com/admin/point/good_record"
    p = 1
    size = 10
    values = {'p':p,'size':size}
    r = requests.get(url=re_url,params=values)
    end = r.text
    end_json = json.loads(end)
    list1 = end_json['data']['list']
    list2 = []
    for i in range(len(list1)):
        if list1[i]['userId'] == uid:
            list2.append(list1[i])
    # print list2
    for i in range(len(list2)):
        if list2[i]['name'] == 'ADIDAS Football Boots F10' and list2[i]['point'] == 125700 and  list2[i]['phone'] == '1':
            print '第' + str(i+1) + '条记录正确'
        elif list2[i]['name'] == 'ADIDAS Stockings Adisock' and list2[i]['point'] == 15100 and  list2[i]['phone'] == '1':
            print '第' + str(i+1) + '条记录正确'
        elif list2[i]['name'] == 'PU Flower Shape Training Soccer Ball\n ' and list2[i]['point'] == 24300 and  list2[i]['phone'] == '1':
            print '第' + str(i+1) + '条记录正确'
        elif list2[i]['name'] == 'Redeem Samsung Galaxy J2 Duos - 8GB' and list2[i]['point'] == 145500 and  list2[i]['phone'] == '1':
            print '第' + str(i+1) + '条记录正确'
        elif list2[i]['point'] == 3000 and list2[i]['phone'] == '+254  13575789124':
            print '第' + str(i+1) + '条记录正确'
        elif list2[i]['point'] == 3000 and list2[i]['phone'] == '+234  13575789124':
            print '第' + str(i+1) + '条记录正确'
        else:
            print '第' + str(i+1) + '条记录有误！请核对！'

#系统后台消息管理接口请求
def feedback_list():
    re_url = 'http://api.admin.test.sokafootball.com/admin/feedback/list'
    p = 1
    size = 20
    language = ''
    values = {'p':p,'size':size,'language':language}
    result = requests.get(url=re_url,params=values)
    text = result.text
    end_json = json.loads(text)
    list = end_json['data']['list']
    content = list[0]['content']
    return content


