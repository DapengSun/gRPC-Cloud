# -*- coding: utf-8 -*-

import sys
sys.path.append('..')
from ConsulConf import consul_resolver,consul_host,consul_post,beat_check_tcp
from dns.exception import DNSException
import consul

def Register(server_name, ip, port,service_id):
    c = consul.Consul(host=consul_host,port=consul_post,scheme='http')  # 连接consul 服务器，默认是127.0.0.1，可用host参数指定host
    print(f"开始注册服务{server_name}")
    check = consul.Check.tcp(ip, port, beat_check_tcp)  # 健康检查的ip，端口，检查时间
    c.agent.service.register(server_name, service_id=service_id,address=ip, port=port, check=check)  # 注册服务部分
    print(f"注册服务{server_name}成功")

def Unregister(server_name, ip, port):
    c = consul.Consul(host=consul_host,port=consul_post,scheme='http')
    print(f"开始退出服务{server_name}")
    c.agent.service.deregister(f'{server_name}-{ip}-{port}')

def GetIpPort(server_name):
    try:
        dnsanswer = consul_resolver.query(f'{server_name}.service.consul', "A")
        dnsanswer_srv = consul_resolver.query(f"{server_name}.service.consul", "SRV")
    except DNSException as ex:
        return ex.msg
    return dnsanswer[0].address, dnsanswer_srv[0].port