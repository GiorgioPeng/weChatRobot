from wxpy import *
import random as rd
import corpus #导入语料库

if __name__ == '__main__':
    chicken_soup = corpus.chicken_soup

    b = Bot()
    friends_name = input("请输入要聊天的好友名字：")
    if friends_name == '':
        fr = ''
        print('没有指定需要灌鸡汤的好友！')
    else:
        fr = b.friends().search(friends_name)[0]


    # 回复所有好友信息
    @b.register(Friend)
    def replyAllFriends(msg):
        msg.reply('我是机器人，主人正在忙，请等待回复！')
        print(msg)
        return


    # 回复群里被@的信息
    # @b.register(Group)
    # def replyAtGroupMessage(msg):
        # if msg.is_at:
            # msg.reply('我是机器人，主人正在忙，请等待回复！')
            # print(msg)
            # return


    # 特定好友消息处理函数(给好友喂鸡汤)
    @b.register(fr, TEXT)
    def replySpecialFriend(msg):
        fr.send(chicken_soup[int(rd.random()*len(chicken_soup))])
        print(msg)
        return


    # 阻塞线程和进入调试
    embed()
