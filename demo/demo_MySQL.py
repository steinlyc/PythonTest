import pymysql


class SelectMysql(object):

    def __init__(self):
        self.get_conn()

    # 获取连接
    def get_conn(self):
        try:
            self.conn = pymysql.connect(
                host='127.0.0.1',
                port=3306,
                user='root',
                password='349618..',
                db='Demo',
                charset='utf8'
            )
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Error:%s' % e)

    # 关闭连接
    def close_conn(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print('Error:%s' % e)

    def get_one(self, age):
        # 执行sql
        sql = "SELECT * FROM `temp` WHERE `age` = '%s' ORDER BY `id`"
        self.cur.execute(sql % age)
        # 提交
        self.conn.commit()
        # 获取结果
        result = self.cur.fetchall()
        print(result)
        print(self.cur.description)
        # 处理结果
        # zip 将对象中对应的元素打包成一个个元组，然后返回由这些元组组成的列表
        msg = dict(zip([key[0] for key in self.cur.description], result))
        # 关闭连接
        self.close_conn()
        return msg

    def get_more(self, age, page, page_size):
        # 执行sql
        offset = int(page - 1) * page_size
        sql = "SELECT * FROM `temp` WHERE `age` = '%s' ORDER BY `id` DESC LIMIT %d,%d;"
        self.cur.execute(sql % (age, offset, page_size))
        # 提交
        self.conn.commit()
        # 获取结果
        result = self.cur.fetchall()
        # 处理结果
        msg = [dict(zip([key[0] for key in self.cur.description], row)) for row in result]
        # 关闭连接
        self.close_conn()
        return msg

    # 如果插入多条数据，想让没问题的插入，有问题的不插入，可以在except里再commit一次，如果其中有一次有错误就都不插入，直接rollbakc回滚
    def inster_data(self):
        try:
            sql = 'INSERT INTO `temp` (`id`,`age`,`name`,`city`) VALUES (%s,%s,%s,%s);'
            self.cur.execute(sql,(7,28,'chenchen','sichuan','1'))
            self.conn.commit()
            self.close_conn()
        except Exception as e:
            print(e)
            self.conn.commit()
            self.conn.rollback()
        self.close_conn()



def main():
    obj = SelectMysql()
    # result = obj.get_one('18')
    # print(result)
    # result = obj.get_more('18', 1,1 )
    # for item in result:
    #     print(item)
    #     print('----------')
    obj.inster_data()


if __name__ == '__main__':
    main()