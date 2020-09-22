"""
@module GameNet.net
@description 一种提供N中输入状态机制的游戏控制网络
"""
from BaseNet import Net


class GameNet(Net):
    name = "GameNet"

    @property
    def net(self):
        pass
