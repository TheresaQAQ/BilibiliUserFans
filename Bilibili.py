import requests
import json
import time

class Bilibili:
    def __init__(self, uid):
        self._headers = {"user-agent":"Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.96 Safari/537.36 Edg/88.0.705.56"}
        self._uid = uid

    def get_level(self):
        # 获取等级
        url = "https://api.bilibili.com/x/space/acc/info?mid={uid}&jsonp=jsonp".format(uid=self._uid)

        res = json.loads(requests.get(url,headers=self._headers).text)

        return res['data']['level']

    def get_fans(self,page):
        url = "https://api.bilibili.com/x/relation/followers?vmid={uid}&pn={page}&ps=20&order=desc&jsonp=jsonp&callback=".format(uid=self._uid,page=page)

        res = json.loads(requests.get(url, headers=self._headers).text)
        list =[]
        for i in range(20):
            list.append(res['data']['list'][i]['mid'])

        return list



if __name__ == "__main__":
    B = Bilibili('11742550')
    t1 = time.time()
    B.get_fans(1)
    t2 = time.time()
    print(t2-t1)