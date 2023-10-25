from enum import Enum

hostIpPath = "hostip.txt"
CARRIAGE = "\n"
def GetHostIpList():
    content = ""
    with open(hostIpPath) as f:
        content = f.read()
    return content.split(CARRIAGE)

class BoardCmd(Enum):
    PING = 0
    SHELL_PING = 1
    VERSION = 2


cmdList = []
def StubBoardResponse(hostip, cmd : BoardCmd):
    hostIpList = GetHostIpList()
    for ip in hostIpList:
        if ip == hostip:
            if cmd == BoardCmd.PING:
                return "Reply from 172.26.96.1: bytes=32 time<1ms TTL=128"
            elif cmd == BoardCmd.VERSION:
                return "V300R024C00"
            elif cmd == BoardCmd.SHELL_PING:
                return " ok\n".join(hostIpList)
            else:
                return ""
    print("no such hostip")
