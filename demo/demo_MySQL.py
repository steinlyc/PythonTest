import pymysql


class SelectMysql(object):
    def __init__(self):
        self.get_conn()

    # 获取连接方法
    def get_conn(self):
        try:
            self.conn = pymysql.connect(host='127.0.0.1',
                                        port=3306,
                                        user='root',
                                        password='349618..',
                                        db='Demo',
                                        charset='utf8')
            # 得到一个可以执行SQL语句的游标对象
            self.cur = self.conn.cursor()
        except Exception as e:
            print('Error:%s' % e)

    # 关闭连接方法
    def close_conn(self):
        try:
            self.cur.close()
            self.conn.close()
        except Exception as e:
            print('Error:%s' % e)

    def get_one(self, age):
        # 定义SQL语句
        sql = "SELECT * FROM `temp` WHERE `age` = %s ORDER BY `id`"
        # 如果一个变量，直接逗号分隔，如果多个，用列表和字典都可以
        self.cur.execute(sql, age)
        # 提交才会显示在数据库，不提交只是暂存
        self.conn.commit()
        # 获取结果，返回的是一个元祖
        result = self.cur.fetchone()
        # 处理结果
        # description是描述，获取的是游标当中列名以及描述信息，是元祖的集合如：('id', 3, None, 11, 11, 0, False)
        # 获取 description 中每一个元祖的第一项，即列名，用列表推导式组成一个列表
        # zip 传入的2个列表每一位一一对应组合，然后返回由这些元组组成的新列表，有dict函数来映射成字典
        msg = dict(zip([key[0] for key in self.cur.description], result))
        # 关闭连接
        self.close_conn()
        return msg

    def get_more(self, age, page, page_size):
        # page 和 page_size 做分页查询处理
        offset = int(page - 1) * page_size
        sql = "SELECT * FROM `temp` WHERE `age` = %s ORDER BY `id` DESC LIMIT %s,%s;"
        self.cur.execute(sql, [age, offset, page_size])
        # 使用conn提交
        self.conn.commit()
        # 获取结果，返回的是一个元祖集合
        result = self.cur.fetchall()
        # 处理结果，因为这里是多条数据，即每一条数据都要映射成一个字典，使用列表推导式进行forin循环
        msg = [dict(zip([key[0] for key in self.cur.description], row))for row in result]
        # 关闭连接
        self.close_conn()
        return msg

    # 如果插入多条数据，想让没问题的插入，有问题的不插入，可以在except里再commit一次，想要如果其中有一次有错误就都不插入，直接rollbakc回滚
    def inster_data(self):
        try:
            # 可以插入多条数据，VALUES 后面逗号分隔
            sql = 'INSERT INTO `temp` (`id`,`age`,`name`,`city`) VALUES (%s,%s,%s,%s);'
            self.cur.execute(sql, (7, 28, 'chenchen', 'sichuan', '1'))
            self.conn.commit()
            self.close_conn()
        except Exception as e:
            print(e)
            # self.conn.commit()
            self.conn.rollback()
        self.close_conn()


def main():
    # 实例化连接对象
    obj = SelectMysql()
    # 查询一条
    # result = obj.get_one('18')
    # print(result)
    # 查询多条
    result = obj.get_more('18', 1, 2)
    for item in result:
        print(item)
        print('----------')
    # 插入数据
    # obj.inster_data()


if __name__ == '__main__':
    main()