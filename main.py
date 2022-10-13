import time
from time import sleep
import requests
import json
import os
import chromedriver_binary
from selenium import webdriver
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.common.by import By
import subprocess
from subprocess import PIPE
import pyperclip

# 自分のAtCoderのユーザーIDを設定する
userID = "ruymtnw"

# 現在のunix_secondの取得
now = int(time.time())

# unix_secondの取得
if os.path.exists("unix_second.txt"):
    f = open("unix_second.txt", 'r', encoding='UTF-8')
    unix_second = f.read()
else:
    unix_second = "0"

# AtCoderのAPIのURL
api_path = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=" + \
    userID + "&from_second=" + unix_second


def main():
    submissions = getSubmissionData()
    if len(submissions) == 0:
        print("提出履歴がありません")
        return
    pro_bar = ' ' * len(submissions)
    print('\r[{0}] {1}/{2}'.format(pro_bar, 0, len(submissions)), end='')
    makeSubmissionFolder(submissions)
    insertAnswers(submissions)
    print("\n取得が完了しました")


def getSubmissionData():
    """
    AtCoderのAPIを叩いて、自分の提出履歴を取得する
    """
    api_url = api_path
    response = requests.get(api_url)
    jsonData = response.json()
    jsonData = list(
        filter(lambda x: x["result"] == "AC" and "Python" in x["language"], jsonData))
    return jsonData


def makeSubmissionFolder(submissions):
    """
    提出データのフォルダを作成する
    """
    for submission in submissions:
        contest_id = submission["contest_id"].upper()
        os.makedirs("submissions/" + contest_id, exist_ok=True)


def insertAnswers(submissions):
    """
    1. 提出コードの画面を開く
    2. コードを取得
    3. コードを自動整形
    4. ファイルを保存

    Parameters:
    submissions (list): 提出データのリスト
    """

    options = Options()
    # ブラウザを表示しない
    options.headless = True
    driver = webdriver.Chrome(options=options)
    for i, submission in enumerate(submissions):
        contest_id = submission["contest_id"].upper()
        problem_id = submission["problem_id"][-1]
        sub_url = "https://atcoder.jp/contests/" + \
            contest_id + "/submissions/" + str(submission["id"])

        # 提出コードの取得
        driver.get(sub_url)
        copy_btn = driver.find_elements(By.CLASS_NAME, "btn-copy")[1]
        copy_btn.click()
        code = pyperclip.paste()

        # ファイルパスの設定
        path = "submissions/" + contest_id + "/" + problem_id + ".py"

        # 既にファイルが存在する場合はスキップ
        with open(path, "w") as f:
            f.write(code)

        # 自動整形
        subprocess.run("autopep8 -i " + path, shell=True,
                       stdout=PIPE, stderr=PIPE, text=True)

        # 負荷軽減のために3秒待機
        sleep(3)

        # 進捗を表示
        pro_size = len(submissions)
        pro_bar = ('=' * (i + 1)) + (' ' * (pro_size - i - 1))
        print('\r[{0}] {1}/{2}'.format(pro_bar, i + 1, pro_size), end='')
        time.sleep(0.5)

    driver.quit()

    with open("unix_second.txt", "w") as f:
        f.write(str(now))


if __name__ == "__main__":
    print("取得中...")
    main()
