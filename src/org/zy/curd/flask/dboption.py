from flask import Flask
from flask import request
import pymysql

class SqlOpt:
    def connect(self):
        self.db = pymysql.connect("127.0.0.1","root","123456","test")
        self.cursor = self.db.cursor()

    def insert(self,sql):
        self.cursor.execute(sql)
        self.db.commit()

    def delete(self,sql):
        self.cursor.execute(sql)
        self.db.commit()

    def update(self,sql):
        self.cursor.execute(sql)
        self.db.commit()


    def search(self,sql):
        self.cursor.execute(sql)
        data = self.cursor.fetchall()
        return data

    def close(self):
        self.db.close()

    def test(self):
        self.cursor.execute("select version()")
        data = self.cursor.fetchall()
        print(data)

app = Flask(__name__)


#{"username":"xxx","userid":"xxxx"}
@app.route('/add')
def addUser():
    data = request.args.to_dict()
    id = data.get("userid")
    name = data.get("username")
    opt = SqlOpt()
    opt.connect()
    sql = "insert into flask values (\""+id+"\",\""+name+"\")"
    print("adduser : "+sql)
    opt.insert(sql)
    opt.close()
    return "success"
    pass

# {"userid":"xxx"}
@app.route('/delete')
def deleteUser():
    data = request.args.to_dict()
    id = data.get("userid")
    opt = SqlOpt()
    opt.connect()
    sql = "delete from flask where userid = \""+id+"\""
    opt.delete(sql)
    opt.close()
    return "delete success"
    pass

# {"userid":"xxx","username":"yyy"}
@app.route('/update')
def updateUser():
    data = request.args.to_dict()
    id = data.get("userid")
    name = data.get("username")
    # updatename = data.get("update")
    opt = SqlOpt()
    opt.connect()

    sql = "update flask set username = \""+name+"\" where userid = \""+id+"\""
    opt.update(sql)
    opt.close()
    return "update success"
    pass

# {"userid":"xxx"}
@app.route('/search')
def searchUser():
    data = request.args.to_dict()
    id = data.get("userid")
    opt = SqlOpt()
    opt.connect()
    sql = "select * from flask where userid = \""+id+"\""
    print(sql)
    data= opt.search(sql)
    print(data.__str__())
    opt.close()
    return data.__str__()
    pass


if __name__ == "__main__":
    application = app.run()
