from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine
from datetime import datetime

engine = create_engine( # 改成 mysql 的連線方式
    'mysql+pymysql://root:root@127.0.0.1:3306/DevDb', echo=False)
Base = declarative_base()


class AppInfo(Base):
    __tablename__ = 'app_info'
    id = Column('id', Integer, primary_key=True)
    name = Column(String)
    version = Column(String)
    author = Column(String)
    date = Column(Integer)
    remark = Column(String)

    def __init__(self, name, version, author, date, remark):
        self.name = name
        self.version = version
        self.author = author
        self.date = date
        self.remark = remark

    def __str__(self):
        return """
        app_id => {},
        app_name => {},
        app_version => {},
        app_author => {},
        app_date => {},
        app_remark => {}
        """.format(self.id, self.name, self.version, self.author, self.date, self.remark)


Session = sessionmaker(bind=engine)
session = Session()

appDesc = """
Please input action code :

1 - Insert Data
2 - Update Data
3 - Delect Date
--- --- ---
0 - exit

"""
isRun = True

while(isRun):
    result = session.query(AppInfo).all()
    for row in result:
        print(row)

    ctrl = input(appDesc)
    if ctrl == "0":
        isRun = False
    elif ctrl == "1":
        print(datetime(2021, 11, 8, 12, 30, 10))
        print(type(datetime(2021, 11, 8, 12, 30)))
        appInfo = AppInfo('App', '1.0.1', 'DevAuth', # 宣告 AppInfo 物件
                          datetime(2021, 11, 8, 12, 30, 10), 'App-v1.0.1')
        session.add(appInfo) # add() 方法，參數帶入目標物件
        session.commit() # 新增的操作必須要加上提交的方法
    elif ctrl == "2":
        row_id = input("id = ? ")
        appInfo = session.query(AppInfo).filter_by(id=row_id).first() # 先查詢出目標物件
        appInfo.name = "AppNew" # 直接修改物件的參數
        appInfo.version = "1.0.2"
        appInfo.remark = "App-v1.0.2"
        session.commit() # 更新的操作必須要加上提交的方法
    elif ctrl == "3":
        row_id = input("id = ? ")
        appInfo = session.query(AppInfo).filter_by(id=row_id).first() # 先查詢出目標物件
        session.delete(appInfo) # delete 方法，參數帶入目標物件
        session.commit() # 刪除的操作必須要加上提交的方法