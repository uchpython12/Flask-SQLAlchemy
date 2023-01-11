from sqlalchemy import *

engine = create_engine('sqlite:///DevDb.db', echo=True) # 建立連線

db = MetaData() # 取得類似於 Cursor 的物件

demo_table = Table( # 代表資料表數據的物件
    'demo_table', db,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('data', String),
)
db.create_all(engine) # 創建資料表