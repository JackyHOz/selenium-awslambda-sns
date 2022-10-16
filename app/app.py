import json
import boto3
import os
from selenium.webdriver.chrome.service import Service
from selenium import webdriver
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options


def handler(event, context):
    """Sample pure Lambda function

    Parameters
    ----------
    event: dict, required
        API Gateway Lambda Proxy Input Format

        Event doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html#api-gateway-simple-proxy-for-lambda-input-format

    context: object, required
        Lambda Context runtime methods and attributes

        Context doc: https://docs.aws.amazon.com/lambda/latest/dg/python-context-object.html

    Returns
    ------
    API Gateway Lambda Proxy Output Format: dict

        Return doc: https://docs.aws.amazon.com/apigateway/latest/developerguide/set-up-lambda-proxy-integrations.html
    """
    chrome_options = webdriver.ChromeOptions()
    chrome_options.binary_location = "/opt/chrome/chrome"
    chrome_options.add_argument("--headless")
    chrome_options.add_argument("--no-sandbox")
    chrome_options.add_argument("--disable-dev-shm-usage")
    chrome_options.add_argument("--disable-gpu")
    chrome_options.add_argument("--disable-dev-tools")
    chrome_options.add_argument("--no-zygote")
    chrome_options.add_argument("--single-process")
    chrome_options.add_argument("window-size=2560x1440")
    chrome_options.add_argument("--user-data-dir=/tmp/chrome-user-data")
    chrome_options.add_argument("--remote-debugging-port=9222")
    driver = webdriver.Chrome("/opt/chromedriver", options=chrome_options)
    # for another website, you can update your code below
    # the link of website
    url = 'https://aws.amazon.com/deepracer/schedule-and-standings/leaderboard-2022-10-open/'
    driver.get(url)
    tmp = []
    print(driver.get(url))
    for num in range(2,5):
        l = driver.find_elements(By.CSS_SELECTOR, f'div.m-row:nth-child({num})')
        for i in l:
            print(i.text)
            tmp.append(i.text)
    
    driver.close()
    driver.quit()
    print(tmp)
    msg = tmp
    # update result to sns
    client = boto3.client('sns')
    response = client.publish(
        TopicArn=os.environ['SNStopic'],
        Message=json.dumps({'default': json.dumps(msg)}),
        MessageStructure='json'
    )
    return response
