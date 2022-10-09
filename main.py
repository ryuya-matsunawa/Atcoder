from time import sleep
import requests
import json
import os
from selenium import webdriver
import chromedriver_binary
from selenium.webdriver.common.by import By
import subprocess
from subprocess import PIPE
import pyperclip

userID = "ruymtnw"  # 自分のAtCoderのユーザーIDを設定する
unix_second = 0
api_path = "https://kenkoooo.com/atcoder/atcoder-api/v3/user/submissions?user=" + \
    userID + "&from_second=" + str(unix_second)


def main():
    submissions = getSubmissionData()
    makeSubmissionFolder(submissions)
    insertAnswers(submissions)


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

    driver = webdriver.Chrome()
    for submission in submissions:
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

    driver.quit()


if __name__ == "__main__":
    main()
