# 开发时间：2023/3/30 21:20

import pymysql

from common.yaml_conffig import GetConf


class MysqlOperate:
    def __init__(self):
        mysql_conf = GetConf().get_mysql_config()
        self.host = mysql_conf["host"]
        self.db = mysql_conf["db"]
        self.port = mysql_conf["port"]
        self.user = mysql_conf["user"]
        self.password = mysql_conf["password"]
        self.conn = None
        self.cur = None

    def __conn_db(self):
        try:
            self.conn = pymysql.connect(
                host=self.host,
                user=self.user,
                password=self.password,
                db=self.db,
                port=self.port,
                charset="utf8"
            )
        except Exception as e:
            print(e)
            return False
        self.cur = self.conn.cursor()
        return True

    # 关闭数据库连接
    def __close_conn(self):
        self.cur.close()
        self.conn.close()
        return True

    def __commit(self):
        self.conn.commit()
        return True

    def query(self,sql):
        '''执行查询语句'''
        # 连接数据库
        self.__conn_db()
        # 执行sql
        self.cur.execute(sql)
        # 通过fetchall获取到查询的数据
        query_data = self.cur.fetchall()
        if query_data==():
            query_data = None
            print("没有获取到数据表为空")
        else:
            pass
        # 关闭连接
        self.__close_conn()
        return query_data

    def insert_update_table(self,sql):
        '''执行插入或修改sql语句'''
        # 连接数据库
        self.__conn_db()
        # 执行sql
        self.cur.execute(sql)
        self.__commit()
        # 关闭连接
        self.__close_conn()