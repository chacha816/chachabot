from rtmbot import RtmBot
from rtmbot.core import Plugin

class HelloPlugin(Plugin):
    def process_message(self, data):
        print(data)


config = {
    "SLACK_TOKEN" : "xoxb-...",          # xoxb-...에 자신의 토큰키 입력
    "ACTIVE_PLUGINS" : []
}
bot = RtmBot(config)
bot.start()


print("^o^ ^o^ ^o^ ^o^")
print("배고프다")
