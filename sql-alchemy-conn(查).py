from sqlalchemy import *

engine = create_engine('sqlite:///DevDb.db', echo=False)

conn = engine.connect()
db = MetaData()

demo_table = Table(
    'demo_table', db,
    Column('id', Integer, primary_key=True),
    Column('name', String),
    Column('data', String),
)

sql = demo_table.select() # 使用 select 函式

print("sql => ", str(sql), '\n') # 完整 SQL 語句

result = conn.execute(sql) # 執行 SQL 方法

print("result type => ", type(result), '\n') # <class 'sqlalchemy.engine.cursor.LegacyCursorResult'>

for row in result: # 具有 list 型態特性，可回圈迭代
    print(type(row)) # <class 'sqlalchemy.engine.row.LegacyRow'>
    demo_id, demo_name, demo_data = row # 具有 tuple 元素特性，可拆分為參數
    print("id => ", demo_id)
    print("name => ", demo_name)