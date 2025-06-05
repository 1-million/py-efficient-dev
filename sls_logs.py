from flask import Flask, request, jsonify

app = Flask(__name__)


@app.route('/fspjConfig/open/saveLogs.do', methods=['GET', 'POST'])
def print_params():
    # 获取所有参数（兼容 GET 和 POST）
    if request.method == 'GET':
        params = request.args.to_dict()  # GET 参数（URL 查询字符串）
    else:
        if request.is_json:
            params = request.get_json()  # JSON 数据
        else:
            params = request.form.to_dict()  # Form 表单数据

    print("Received parameters:", params)
    return jsonify({"status": "success", "data": params})


if __name__ == '__main__':
    app.run(host='0.0.0.0', port=7777, debug=True)
