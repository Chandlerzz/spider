import requests

class IPPool:
    def __init__(self):
        pass

    def get_proxy(self):
        return requests.get("http://127.0.0.1:5010/get/").json()

    def delete_proxy(self,proxy):
        requests.get("http://127.0.0.1:5010/delete/?proxy={}".format(proxy))

    # your spider code

    def getHtml(self,headers,url):
        # ....
        retry_count = 5
        proxy = self.get_proxy().get("proxy")
        while retry_count > 0:
            try:
                html = requests.get(url,headers=headers,proxies={"http": "http://{}".format(proxy)})
                # 使用代理访问
                return html
            except Exception:
                retry_count -= 1
        # 出错5次, 删除代理池中代理
        delete_proxy(proxy)
        return None