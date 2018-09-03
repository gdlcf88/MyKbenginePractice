# -*- coding: utf-8 -*-
try:
    import KBEngine
except ImportError as e:
    from KBEngineTips.BaseApp import KBEngine
from KBEDebug import *


class FirstEntity(KBEngine.Entity):
    """
    第一个实体的base部分的实现
    """
    def __init__(self):
        KBEngine.Entity.__init__(self)

    def hello(self, content):
        """
        say hello
        :param content:内容
        :return:
        """
        INFO_MSG("Hello ComblockEngine! I'm %s. I got your content=%s" % (self.name, content))

    def createCell(self, sceneCell):
        """
        创建cell部分
        :param sceneCell:场景的cellEntityCall
        """
        # API：创建该实体的cell部分
        self.createCellEntity(sceneCell)