import boto3
from flask import Flask, request, Response
import pymysql
import config

app = Flask(__name__)
con = config.Config()
s3 = boto3.client('s3',
                  aws_access_key_id=con.AWS_ACCESS_KEY,
                  aws_secret_access_key=con.AWS_SECRET_KEY)

@app.route('/')
def index():
    return 'hello AWS world / .env 테스트 : {}'.format(con.DB_SCHEMA)

@app.route('/health')
def health():
    return Response("Success Health Check", status=200)

@app.route('/upload', methods=['POST'])
def upload_image():
    file = request.files['file']
    if file:
        s3.upload_fileobj(file, con.BUCKET_NAME, file.filename)
        return Response("upload successfully", status=200)
    return Response("No file", status=404)

if __name__ == '__main__':
    db = pymysql.connect(host=con.DB_HOST, user=con.DB_USER, password=con.DB_PASSWORD, db=con.DB_SCHEMA)
    print("connect ok")
    app.run(host='0.0.0.0')
