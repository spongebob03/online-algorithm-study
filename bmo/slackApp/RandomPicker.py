from slack_sdk import WebClient
from slack_sdk.errors import SlackApiError
import os
import logging

from bs4 import BeautifulSoup
from urllib.request import urlopen
import random

# 모의 코테 문제 선별 크롤러
# solved.ac의 알고리즘 유형별, 많이 푼 순서로 소팅된 페이지 정보를 긁어옵니다
# 지나치게 많은 트래픽을 발생시키는 경우에는 사이트 이용이 정지된다고 합니다
# 그래서인지 여러번 실행하면 아무 정보가 들어오지 않는다. 하지만 solvedac인데 왜..?

def getData(url):
    html = urlopen(url)
    source = html.read()
    html.close()

    soup = BeautifulSoup(source, "lxml")
    problems = soup.select("a[href^='https://www.acmicpc.net/problem/']")
    # problems = soup.select('.hover_underline')
    pools = []
    for p in problems[1::2]:
        href = p.attrs['href']
        pools.append(p.text + ":" + href)
    return pools

def random_problem(array):
    tag = array[random.randrange(0, 5)]
    url = "https://solved.ac/search?query=tag%3A"+tag+"&sort=solved&direction=desc&page=1"
    pools = getData(url)
    return pools[random.randrange(0, len(pools))] if pools else "크롤링 실패,,,"

def sendToSlack(arr1, arr2):
    f = open('bmo/slackApp/token.txt')
    key = f.readline()
    # client = WebClient(token=os.environ.get(token))
    client = WebClient(token=key)
    logger = logging.getLogger(__name__)

    channel_id = "#모의-코테"
    # slack = Slacker(token) # invalid_auth 문제: 21년부터 slackerㄴㄴ
    # slack.chat.post_message("#모의-코테", "슬랙 챗봇으로 문제를 선택!", as_user=True)
    try:
        result = client.chat_postMessage(
            channel = channel_id,
            text = "🍉모의 코딩테스트 문제입니다🍉\n" + arr1 + "\n" + arr2
        )
        logger.info(result)
    except SlackApiError as e:
        logger.error(f"Error posting messgage: {e}")

if __name__ == '__main__':
    array = ["dfs", "bfs", "binary_search", "dijkstra", "graphs"]
    print("모의 코딩테스트 문제입니다~^^~")
    arr1 = random_problem(array)
    arr2 = random_problem(array)
    sendToSlack(arr1, arr2)