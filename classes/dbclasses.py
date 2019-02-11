import MySQLdb
class SQLighter:
    def __init__(self):
        self.conn  = MySQLdb.connect("evaclickwithoutfsm.mysql.pythonanywhere-services.com","evaclickwithoutf","BDclick!2408","evaclickwithoutf$default",charset = "utf8", use_unicode = True)
        self.c = self.conn.cursor()

    def create_table(self, table_name):
        try:
            self.c.execute("DROP TABLE IF EXISTS %s"% (table_name))
            self.c.execute("CREATE TABLE IF NOT EXISTS `%s` (`id` int(11) NOT NULL AUTO_INCREMENT,`ANSW_QUESTION_CODE` varchar(50) NOT NULL,`ANSW_ANSWER_CODE` varchar(50) NOT NULL,PRIMARY KEY (`id`),UNIQUE KEY `ANSW_QUESTION_CODE` (`ANSW_QUESTION_CODE`)) ENGINE=InnoDB  DEFAULT CHARSET=utf8 AUTO_INCREMENT=1 "% (table_name))
        finally:
            self.c.close()
            self.conn.close()

    def getByQuestionCode(self, question_code):

        self.c.execute("SELECT * FROM answer_01 WHERE ANSW_QUESTION_CODE = '" + question_code + "'")
        self.conn.commit()
        return self.c.fetchone()


    def sel_from(self,m):
        try:
            return self.c.execute("SELECT * FROM testtable WHERE id =(%s)"% (m))
        finally:
                     self.c.close()
                     self.conn.close()

    def insert(self,query):
        try:
            self.c.execute(query)
            self.conn.commit()
        finally:
                 self.c.close()
                 self.conn.close()
    def update(self,q,m,z):
        try:
            data = (m,z)
            self.c.execute(q,data)
            self.conn.commit()
            rows =self.c.fetchall()
            return rows
        finally:
            self.c.close()
            self.conn.close()
    def returnany(self,q,m):
        try:
            data = (m,)
            self.c.execute(q,data)
            self.conn.commit()
            rows =self.c.fetchall()
            return rows
        finally:
            self.c.close()
            self.conn.close()
    def update2var(self,q,m,z,x):
        try:
            data = (m,z,x)
            self.c.execute(q,data)
            self.conn.commit()
            rows =self.c.fetchall()
            return rows
        finally:
            self.c.close()
            self.conn.close()


