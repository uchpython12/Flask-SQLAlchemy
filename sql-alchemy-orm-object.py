from sqlalchemy.orm import sessionmaker
from sqlalchemy.ext.declarative import declarative_base
from sqlalchemy import Column, Integer, String
from sqlalchemy import create_engine

engine = create_engine('sqlite:///DevDb.db', echo=False) # 連線
Base = declarative_base() # 取得類似於 Cursor 的物件


class AppInfo(Base): # class 宣告 AppInfo 類別
    __tablename__ = 'app_info' # 表格名稱
    id = Column('id', Integer, primary_key=True) # id 欄位 , Integer 型態 , 主鍵
    name = Column(String) # name 欄位 , String 型態
    version = Column(String) # versione 欄位 , String 型態
    author = Column(String) # author 欄位 , String 型態
    date = Column(Integer) # date 欄位 , String 型態
    remark = Column(String) # remark 欄位 , String 型態


Session = sessionmaker(bind=engine)
session = Session() # 取得 Session 物件
result = session.query(AppInfo).all() # 執行查詢方法

for row in result:
    print(type(row)) # <class '__main__.AppInfo'>
    print("id => ", row.id)
    print("name => ", row.name)