"""
参考 https://www.cnblogs.com/LY-C/p/9089331.html

端口：操作系统为本机上内一个运行的程序都会随机分配一个端口，其他电脑上的程序可以通过端口获取到这个程序。
ip地址+端口：能唯一找到某台电脑上的某一个服务程序。
路由器：连接不同网段，路由
网关：类似一个局域网的入口和出口
网段：一个局域网内的ip地址范围
子网掩码：子网掩码 & ip地址  得到网段

osi五层模型：
			应用层：http/https/ftp协议等（应用程序）
			传输层：tcp/udp协议（选择应用程序之间的通讯协议）
			网络层：ip协议（给被传输的信息加上ip信息）
			数据链路层：arp协议（根据ip信息找到目标服务器的mac地址，网关等信息）
			物理层：传输电信号
粘包现象：
	场景：发送端不断发送数据，但接收端不知道数据量大小，因此不知道如何去接受，造成的一种数据混乱的现象。
"""

