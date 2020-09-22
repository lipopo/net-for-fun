"""
@module BaseNet.net
@description 基础的神经网路模型
"""


class Net:
    name = None

    @property
    def net(self):
        """
        @property net
        @description 基础的网络模型
        """
        raise NotImplementedError
