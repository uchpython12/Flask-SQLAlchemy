# 建置最基礎的image也就是python3.9
FROM python:3.9
# 定義當前的目錄位置
WORKDIR /Flask-SQLAlchemy
# 將內容複製到工作目錄中
ADD . /Flask-SQLAlchemy
# 運行pip3來安裝Flask應用程序的依賴套件
RUN pip3 install -r requirements.txt
# 執行python的指令語法
CMD ["python3","Flask_DbDao/DbDao.py"]