# django-trip-tickets #

## 專案介紹 ##

本專案利用Django框架，來開發一日遊票券查詢網頁，透過輸入城市名稱，驅動Python網頁爬蟲即時爬取KKday及KLOOK網站的一日遊票券資訊，並且整合Bootstrap框架來美化網頁，可以搭配[[Django+Python網頁爬蟲教學]打造具有網頁爬蟲功能的關鍵字查詢網頁](https://www.learncodewithmike.com/2020/10/django-web-scraping.html)部落格文章來進行學習。

## 前置作業 ##

將專案複製(Clone)下來後，假設沒有pipenv套件管理工具，可以透過以下指令來進行安裝：

`$ pip install pipenv`

切換到專案目錄下，就可以執行以下指令，來安裝所需的套件：

`$ pipenv install --ignore-pipfile`

接著，登入虛擬環境，執行Django Migration(資料遷移)，並且啟動本地端伺服器：

`$ pipenv shell`

`$ pipenv migrate`

`$ python manage.py runserver`

## 執行畫面 ##

開啟瀏覽器，在本地端伺服器的網址後面加上 /tickets (例：http://127.0.0.1:8000/tickets/) 後，即可輸入城市名稱來查詢Python網頁爬蟲所取得的一日遊票券資訊。

![Alt text](https://1.bp.blogspot.com/-EZAOYcmvtEo/X4CfZpYrwvI/AAAAAAAAELo/N6x9tnTN0koyiyMIog4RlLtKISeCn4_WwCPcBGAYYCw/s1117/django_web_scraping.PNG "Optional title")