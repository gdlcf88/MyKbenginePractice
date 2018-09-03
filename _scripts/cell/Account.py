# -*- coding: utf-8 -*-
try:
    import KBEngine
except ImportError as e:
    from KBEngineTips.BaseApp import KBEngine
from KBEDebug import *

class Account(KBEngine.Entity):
    """
    Account实体的cell部分
    """

    def __init__(self):
        KBEngine.Entity.__init__(self)