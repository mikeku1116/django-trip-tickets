from abc import ABC, abstractmethod
from bs4 import BeautifulSoup
import requests


# 票券網站抽象類別
class Website(ABC):

    def __init__(self, city_name):
        self.city_name = city_name  # 城市名稱屬性

    @abstractmethod
    def scrape(self):  # 爬取票券抽象方法
        pass


# KLOOK客路網站
class Klook(Website):

    def scrape(self):

        result = []  # 回傳結果

        if self.city_name:  # 如果城市名稱非空值

            # 取得傳入城市的所有一日遊&導賞團票券
            response = requests.get(
                f"https://www.klook.com/zh-TW/search/?keyword={self.city_name}&template_id=2&start=1")
            soup = BeautifulSoup(response.text, "lxml")

            # 取得五個票券卡片(Card)元素
            activities = soup.find_all(
                "div", {"class", "j_activity_item_link j_activity_item_click_action"}, limit=5)

            for activity in activities:

                # 票券名稱
                title = activity.find(
                    "a", {"class": "title"}).getText().strip()

                # 票券詳細內容連結
                link = "https://www.klook.com" + \
                    activity.find("a", {"class": "title"}).get("href")

                # 票券價格
                price = activity.find(
                    "span", {"class": "latest_price"}).getText().strip()

                # 最早可使用日期
                booking_date = activity.find(
                    "span", {"class": "g_right j_card_date"}).get("data-serverdate")

                # 評價
                star = activity.find(
                    "span", {"class": "t14 star_score"}).getText().strip()

                result.append(
                    dict(title=title, link=link, price=price, booking_date=booking_date, star=star, source="KLOOK"))

        return result
