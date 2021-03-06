# -*- coding: utf-8 -*-
try:
    import KBEngine
except ImportError as e:
    from KBEngineTips.BaseApp import KBEngine
from KBEDebug import *

class FirstEntity(KBEngine.Entity):
    def hello(self, exposed, content):
        """
        接受客户端hello的指令
        :param exposed: 调用者的id
        :param content: hello的内容
        :return:
        """
        sender_entity = KBEngine.entities[exposed]
        if sender_entity is None:
            ERROR_MSG("FirstEntity[%i]:: can not find sender with exposedvalue=[%i]!" % (self.id, exposed))
            return

        INFO_MSG("FirstEntity[%i]::Hello %s[%i]! I'm in space[%i]. I got your content=%s" % (
            self.id, sender_entity.__class__.__name__, sender_entity.id, self.spaceID, content))

       # 调用发送方的客户端方法onFirstEntityHello
       sender_entity.client.onFirstEntityHello("Hi, my master. I'm your first entity!")