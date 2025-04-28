import json

from mitmproxy import http
from mitmproxy.tools.main import mitmdump

import cnysTV
import lcz_company
import rktong


def request(flow: http.HTTPFlow):
    # 在此处设置断点
    # flow.request.headers["debug"] = "1"
    pass


def response(flow: http.HTTPFlow):
    #lcz_company.filter_url(flow)
    #rktong.filter_url(flow)
    cnysTV.filter_url(flow)
    print(f"请求:{flow.request.method}->{flow.request.pretty_url}")
    # print(f"响应:{flow.response.status_code}")
    # print(f"内容:{flow.response.text}")


if __name__ == "__main__":
    # 运行 Mitmproxy，并传递命令行参数
    # mitmdump(['-s', __file__, '-p', '8888', '-q'])
    mitmdump(['-s', __file__, '-p','8888','--mode','upstream:http://127.0.0.1:10809', '-q'])

