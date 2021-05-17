import json

import mitmproxy.http


class Events:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        pass

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" in flow.request.url and "x=" in flow.request.url:
            # 把str数据类型转换为json格式
            data = json.loads(flow.response.text)
            # 修改雪球股票名称数据
            # data["data"]["items"][0]["quote"]["name"] = "多多"
            # data["data"]["items"][1]["quote"]["name"] = "倾心"
            # data["data"]["items"][2]["quote"]["name"] = "hogwarts3"
            # 修改雪球涨跌幅数据
            data["data"]["items"][0]["quote"]["percent"] = "-0.01"
            data["data"]["items"][1]["quote"]["percent"] = "0.01"
            data["data"]["items"][2]["quote"]["percent"] = "0"


            
            # 修改相应数据
            flow.response.text = json.dumps(data)


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8888', '-s', __file__])
