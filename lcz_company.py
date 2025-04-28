import http
import json


def filter_url(flow):
    # 网盛数新办公平台系统
    # 拦截 任务管理2.0查询返回结果 url:https://lcz.lczyun.com/creater/kapi/list/!fileKey
    if flow.request.pretty_url.find("creater/kapi/list/!fileKey") > -1:
        # 解析 将任务记录解析成指定格式并打印
        if flow.response.status_code == 200:
            pass
            rows = parse_rows(flow.response.text)
            print(rows)
            f_rows = format_rows(rows)
            print(f_rows)
            print_rows(f_rows)


def parse_rows(text):
    data = json.loads(text)
    rows = []
    # 解析记录
    for task in data["rowDataList"]:
        task_id = task["r"]["task_id"]["v"]
        task_title = task["r"]["task_title"]["v"]
        priority = task["r"]["priority"]["v"]
        dead_line = task["r"]["dead_line"]["v"]
        row = (task_id, task_title, priority, dead_line)
        rows.append(row)
    return rows


def format_rows(rows: ()):
    strs = []
    for row in rows:
        s = f"【系统缺陷】- {row[0]} - {row[1]} : {row[2]} - {row[3]}"
        print(s)
        strs.append(s)
    return strs


def print_rows(rows):
    print(f"---------------任务清单--START---------------")
    for row in rows:
        print(row)
    print(f"---------------任务清单--END-----------------")
