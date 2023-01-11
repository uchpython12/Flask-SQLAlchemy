# Flask-SQLAlchemy

# Flask-SQLAlchemy Flask_SQLAlchemy 套件
此範例使用Flask-SQLAlchemy,SQLAlchemy ORM 框架。將數據儲存起來，並使用 Flask 建置 使用 SQLite 連線 MySQL。

## Getting Started
### Clone Project
你可以在本機直接使用 git 指令 clone 此專案並執行。

```
git clone https://github.com/uchpython12/Flask-SQLAlchemy
cd https://github.com/uchpython12/Flask-SQLAlchemy
```

### Docker Build Image
#### Docker自動打包image,本地端安裝請跳至Installation
docker run過後可直接訪問 [localhost:5000](http://localhost:5000/).

```
docker build -t Flask-SQLAlchemy .
docker run -p 5000:5000 Flask-SQLAlchemy
```

### Installation
此專案下載至桌面後，使用以下指令安裝必要套件。

```
pip install -r requirements.txt
```

### Running the Project
套件安裝成功後，即可開始執行本專案。

```
python Flask_DbDao/DbDao.py 
```

running locally! Your app should now be running on [localhost:5000](http://localhost:5000/).
