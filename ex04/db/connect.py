# import할 때마다 실행되는 모듈
from pymysql import connect, cursors

conn = connect(
    host="localhost",
    user="green",
    password="green1234",
    db="greendb",
    charset="utf8"
)

cursor = conn.cursor(cursors.DictCursor)  # 기본 tuple
