import sqlite3
from flask import Flask
app = Flask(__name__)

@app.route('/')
def hello_world():
    return "Hello World !!!"

@app.route('/create_table/')
def create_table():
    conn = sqlite3.connect('/share/CA7.db')
    try:
        c = conn.cursor()
        c.execute('''CREATE TABLE  IF NOT EXISTS  JCL_INFO
                (Name text(8) PRIMARY KEY, 
                Frequencty text(1), 
                Type text(1),
                East_run_flag boolean,
                North_run_flag boolean,
                West_run_flag boolean,
                B2B_run_flag boolean)''')
        conn.commit()
        conn.close()
        return "table creation successful"
    except Error as e:
        return e


if __name__ == "__main__":
    app.run(host='0.0.0.0')

