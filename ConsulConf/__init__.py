# -*- coding: utf-8 -*-

from dns import resolver

# docker运行consul服务
# docker run -d -p 8500:8500 -p 8600:8600/udp consul consul agent -data-dir=/consul/data -config-dir=/consul/config -dev -client=0.0.0.0 -bind=0.0.0.0

# 连接服务配置
consul_host = '192.168.7.121'
# consul_host = '127.0.0.1'
consul_post = 8500

# 命名解析 DNS配置
consul_resolver = resolver.Resolver()
consul_resolver.port = 8600
# consul_resolver.nameservers = ["192.168.0.192"]
consul_resolver.nameservers = ["127.0.0.1"]

# 服务心跳监测时长
beat_check_tcp = '10s'

# 主机IP地址
addr_ip = '192.168.7.121'
# addr_ip = '127.0.0.1'