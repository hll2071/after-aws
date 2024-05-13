from flask import Flask, Response
import pymysql
import config

app = Flask(__name__)
con = config.Config()

@app.route('/')
def index():
    return 'hello AWS world'

@app.route('/health')
def health():
    return Response("Success Health Check", status=200)


if __name__ == '__main__':
    db = pymysql.connect(host=con.DB_HOST, user=con.DB_USER, password=con.DB_PASSWORD, db=con.DB_SCHEMA)
    print("connect ok")
    app.run(host='0.0.0.0')
