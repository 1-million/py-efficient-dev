def filter_url(flow):
    if flow.request.pretty_url.find("cnys.tv/vodplay") > -1:
        flow.response.text = flow.response.text.replace("setInterval(loop, 1);", "console.log('debug');")
    if flow.request.pretty_url.find("addons/dp/player/js/player.js") > -1:
        flow.response.headers.update({"content-type": "application/javascript; charset=utf-8"})
        flow.response.text = flow.response.text.replace(
            """EC.setCookie("time_" + config.url, EC.dp.video.currentTime, 24);""",
            """EC.setCookie("time_" + config.url, EC.dp.video.currentTime, 24);\n       EC.dp.notice("当前播放进度:"+ EC.dp.video.currentTime);""").encode(
            "utf-8")