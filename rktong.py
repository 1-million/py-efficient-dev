
def filter_url(flow):
    list = ["bj-td-menta-01-callback.advlion.com/v1/batch",
            "quickaplus-he-api-cn-shanghai.aliyuncs.com/unify_logs",
            "cnlogs.umeng.com/unify_logs",
            "bid-adx2.vlion.cn/main?media=7",
            "api-v3.mentamob.com/api/v1/config",
            "utoken.umeng.com/anti/updateZdata"]
    for url in list:
        if flow.request.pretty_url.find(url) > -1:
            flow.response.text = "{}"