import logging
import telnetlib
import time


class CryptoClient():
    def __init__(self,):
        self.tn = telnetlib.Telnet()
        self.balance = -1

    def login_host(self, host_ip, host_port=23, token="", print_info=True):
        try:
            self.tn.open(host_ip, port=host_port)
        except:
            if print_info:
                logging.warning('%s网络连接失败' % host_ip)
            return False
        self.tn.read_until(b'Please input your token: ', timeout=10)
        self.tn.write(token.encode('ascii') + b'\n')
        time.sleep(1)
        self.output_bytes = self.tn.read_very_eager()
        strResult = self.output_bytes.decode('ascii')
        if 'Invalid token' in strResult:
            if print_info:
                logging.warning('%s 登录失败,token 错误' % host_ip)
            return False
        elif 'Player connection rate limit exceeded' in strResult:
            if print_info:
                logging.warning('%s 登录失败，连接频率达到上限' % host_ip)
            return False
        else:
            x = strResult.find('New balance: ') + len('New balance: ')
            self.balance = int(strResult[x:].split('. ')[0])
            if print_info:
                logging.warning('%s 登录成功 (balance: %d)' % (host_ip, self.balance))
            self.output = strResult.split(
                'Launching challenge...\n')[-1].strip()
            return True

    def execute_some_command(self, command, show_log=False, wait=0.1):
        if type(command) is not bytes:
            if type(command) is not str:
                command = str(command)
            command = command.encode('ascii')
        self.tn.write(command+b'\n')
        # time.sleep(wait)
        # self.output = self.tn.read_very_eager().decode('ascii').split('\n')[0]
        self.output_bytes = self.tn.read_very_eager()
        while len(self.output_bytes) == 0:
            time.sleep(0.01)
            self.output_bytes = self.tn.read_very_eager()
        # time.sleep(wait)
        try:
            self.output_bytes += self.tn.read_very_eager()
        except:
            logging.warning('telnet connection closed')
        self.output = self.output_bytes.decode('ascii')
        if show_log:
            logging.warning('命令执行结果：\n%s' % self.output)
        self.output = self.output[:self.output.rfind('\n')]

    def execute(self, cmd, wit=0.1):
        self.execute_some_command(command=cmd, wait=wit)
        return self.output

    # 退出telnet
    def logout_host(self):
        self.tn.close()

host_ip='crypto-nc.sqrt-1.me'
token='105:MEUCIQC3VeCk1Qj8nNQ4oiIs1Jg/ARGieLOIp8t8cymzXZ6ymQIgEv/wY5Et5ONc8iQ046mVWkUkOYdHhHnvcuNdV5blrCs='
telnet_client=CryptoClient()
"""
通过不断计算2^i*encrypted_flag%n的奇偶性来得到n的大致范围
以i=1为例：
若为1，则flag>(n/2)
若为0，则flag<(n/2)
再在以上基础之上再次缩小范围
最终在循环3000次之后得到准确数值
仅仅循环ln（n）次得到的数据仍较难通过循环计算

"""

if telnet_client.login_host(host_ip,10016,token):
    s=telnet_client.output
    encrypted_flag,n=s.split('\n')
    n=int(n)
    encrypted_flag=int(encrypted_flag)
    print(n)
    print(encrypted_flag)
    e = 65537
    i=1
    _0_1=[]
    while i<=3000:
        a=pow(2**i,e,n)
        x=pow(a*encrypted_flag,1,n)
        out=telnet_client.execute(x)
        _0_1.append(out)
        """
        这里是试图在循环中直接得出n的范围
        但由于n太大无法计算故只能取end=2**1000
        但这样计算出的数据十分不精确
        所以采用的方法是先计算0，1的数组
        再通过sage进一步计算n值
        即以下部分在sage完成
        global start,end
        start=0
        end=2**1000
        middle=(end+start)/2
        if out=='0':
            
            end=middle
        else:
            start=middle
        """
        i=i+1  
    print(_0_1)

