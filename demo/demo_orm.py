from sqlalchemy import create_engine
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy.orm import sessionmaker
import pymysql
pymysql.install_as_MySQLdb()

# 获取基类
Base = declarative_base()
engine = create_engine('mysql://root:349618..@localhost:3306/Demo2?charset=UTF8MB4')
session = sessionmaker(bind=engine)


class Person(Base):
    __tablename__ = 'person'
    id = Column(Integer, primary_key=True)
    age = Column(Integer, nullable=False)
    name = Column(String(200), nullable=False)
    city = Column(String(200), nullable=False)

# 传入engin 创建数据库
# Person.metadata.create_all(engine)

class OrmTest():
    def __init__(self):
        self.session = session()

    def add_one(self):
        new_data = Person(
            id = 4,
            age = 18,
            name = 'lilei',
            city = '苏州'
        )
        self.session.add(new_data)
        self.session.commit()
        return new_data

    def add_all(self):
        datas = [
            Person(id = 5,age = 18,name = 'aaa',city = '广州'),
            Person(id = 6,age = 18,name = 'bbb',city = '重庆'),
            Person(id = 7,age = 18,name = 'ccc',city = '武汉'),
            Person(id = 8,age = 18,name = 'ddd',city = '湖北'),
        ]
        self.session.add_all(datas)
        self.session.commit()
        return datas

    def get_one(self):
        return self.session.query(Person).get(1)

    def get_more(self):
        return self.session.query(Person).all()

    def update(self,item,val):
        # 更新单条数据
        # data = self.session.query(Person).get(item)
        # if data:
        #     data.age = val
        #     self.session.add(data)
        #     self.session.commit()
        #     return True
        # return False

        # 更新多条数据
        data_list = self.session.query(Person)
        for item in data_list:
            item.age = 20
            self.session.add(item)
        self.session.commit()

    def del_data(self,item):
        data = self.session.query(Person).get(item)
        self.session.delete(data)
        self.session.commit()

def main():
    obj = OrmTest()
    # res = obj.add_all()
    # res = obj.get_more()
    # print(res.count())
    # for item in res:
    #     if item:
    #         print(f'id:{item.id}-----name:{item.name}')
    #     else:
    #         print('数据不存在')
    # res = obj.update(3,50)
    # print(res)
    obj.del_data(3)

if __name__ == "__main__":
    main()