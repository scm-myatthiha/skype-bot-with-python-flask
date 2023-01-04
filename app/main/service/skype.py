from skpy import Skype
from ..skype_id import skype_group

user = 'youremail'
password = 'yourpassword'


def MessageSend(joinUrl, meetingPassword):
    skype_obj = Skype(user, password)
    skype_obj.chats
    skype_obj.chats.recent()
    channel = skype_obj.chats.chat('skye_group_id')
    channel.sendMsg(joinUrl)
    channel.sendMsg("Password is " + meetingPassword)


def AutoMessageSend():
    skype_obj = Skype(user, password)
    skype_obj.chats
    skype_obj.chats.recent()
    channel = skype_obj.chats.chat(skype_group)
    channel.sendMsg("Type your message here...")
