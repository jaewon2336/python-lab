# C:\Users\Administrator\AppData\Local\Programs\Python\Python310\Scripts
# python -m pip install flask

from flask import Flask, request, jsonify
import member_dao as dao

flask = Flask(__name__)  # __main__ 지금 내 파일을 실행하고있구나

# 컨트롤러


@flask.route("/my-member")
def list():
    return jsonify(dao.select_all())


@flask.route("/my-member/<id>")
def detail(id):
    return jsonify(dao.select_one(id=id))  # **data


@flask.route("/my-member/<id>", methods=['DELETE'])
def delete(id):
    return jsonify(dao.delete_one(id=id))


@flask.route("/my-member/<id>", methods=['PUT'])
def update(id):
    # data = request.data # x-www-form-urlencoded 파싱 기법
    data = request.get_json  # application/json 파싱 기법
    # dict 타입이라서!
    return jsonify(dao.update_one(id=id, username=data["username"], password=data["password"]))


@flask.route("/my-member", methods=['POST'])
def save():
    data = request.get_json
    # dict 타입이라서!
    return jsonify(dao.insert_one(username=data["username"], password=data["password"]))


flask.run(
    host="0.0.0.0",  # anywhere
    port=5000,
    debug=True  # 이 부분이 설정되면 파일 저장시 서버 자동 리로드 된다.(개발 시 필요)
)
