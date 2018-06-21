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