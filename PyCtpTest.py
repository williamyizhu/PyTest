import os
import sys
# os.chdir('Z:\williamyizhu On My Mac\Documents\workspace\PyCtp2')
sys.path.append(os.path.join(os.path.abspath('..'), 'PyCtp2'))
import CtpQuote
import pandas as pd
sys.path.append(os.path.join(os.path.abspath('..'), 'hf_ctp_py_proxy'))
from py_ctp.ctp_struct import *
# from py_ctp.quote import Quote

class PyCtpTest(CtpQuote.CtpQuote):
    def __init__(self):
        print('init')

    def q_OnRtnDepthMarketData(self, pDepthMarketData = CThostFtdcDepthMarketDataField):
        print('hrerere')
        
        
        
xx = PyCtpTest()
xx.q_OnRtnDepthMarketData()
xx.StartQuote()
