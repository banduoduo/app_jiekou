import mitmproxy.http
from mitmproxy import http


class Events:
    def request(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP request has been read.
        """
        if "https://stock.xueqiu.com/v5/stock/batch/quote.json?_t" \
                in flow.request.url and "x=" in flow.request.url:
            with open("quote.json", encoding="UTF-8") as f:
                flow.response = http.HTTPResponse.make(
                    # 状态码
                    200,
                    # 响应体，传入的数据格式是string
                    f.read(),
                    # 响应头
                )

    def response(self, flow: mitmproxy.http.HTTPFlow):
        """
            The full HTTP response has been read.
        """
        pass


addons = [
    Events()
]

if __name__ == '__main__':
    from mitmproxy.tools.main import mitmdump

    # 使用debug模式启动mitmdump
    mitmdump(['-p', '8888', '-s', __file__])
