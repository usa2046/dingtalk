import requests as req
import json,time


def dingtalk(text):
    """
    推送钉钉消息。
    :param data: 要推送的数据内容，字符串格式
    :return:
    """
    json_text = {
        "msgtype": "text",
        "at": {
            "atMobiles": [
                ""
            ],
            "isAtAll": True
        },
        "text": {
            "content": text
        }
    }

    headers = {'Content-Type': 'application/json;charset=utf-8'}
    api_url = "https://oapi.dingtalk.com/robot/send?access_token=ba63349a096a9d8ba7c2a8bd9bc2dfa75285e78eeba2127c939754a73b84f541"
    dingtalk_result = req.post(api_url, json.dumps(json_text), headers=headers).content    # 发送钉钉消息并返回发送结果
    with open('log.txt', mode='a+', encoding='gbk') as f:
        f.write("时间：" + str(time.localtime()) + "  发送状态：" + str(dingtalk_result) + "发送内容：" + str(text))
    print(dingtalk_result)
if __name__ == '__main__':
    while True:
        dingtalk('Stock : ##sdfghjnkjnlk')
        time.sleep(60 )