#coding:utf-8
from J2534 import j2534lib
from J2534 import wrapper as func
from J2534.Define import *
from J2534.Error import printerr
import time
devices = j2534lib.getDevices()
print( devices) 
device = devices[1]
j2534lib.setDevice(key = 1)
print(1)
ret, id1 = func.ptOpen()
printerr(ret)
ret, ch1 = func.ptConnect(id1, ProtocolID.ISO15765, 0, 500000)
printerr(ret)

msg = func.ptTxMsg(ProtocolID.ISO15765, 0)

msg.setIDandData(0x241, [0,1,2,3,4,5,6,7,8,9,10])


maskMsg = func.ptMskMsg(0)
maskMsg.setID(0xffffffff)

patternMsg = func.ptPatternMsg(0)
patternMsg.setID(0x641)

flowcontrolMsg = func.ptPatternMsg(0)
flowcontrolMsg.setID(0x241)

ret, fiterid = func.ptStartMsgFilter(ch1, FilterType.FLOW_CONTROL_FILTER ,maskMsg, patternMsg, flowcontrolMsg)
printerr(ret)

ret = func.ptWtiteMsgs(ch1, msg, 1, 100)
printerr(ret)
time.sleep(3)

ret = func.ptDisconnect(ch1)
printerr(ret)
ret = func.ptClose(id1)
printerr(ret)