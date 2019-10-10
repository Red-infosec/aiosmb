from aiosmb.commons.smbtargetproxy import SMBTargetProxyServerType
from aiosmb.network.network import TCPSocket
from aiosmb.network.socks5network import Socks5ProxyConnection
from aiosmb.network.multiplexornetwork import MultiplexorProxyConnection


class NetworkSelector:
    def __init__(self):
        pass

    @staticmethod
    async def select(target):
        if target.proxy is None:
            return TCPSocket()
        elif target.proxy.proxy_type in [SMBTargetProxyServerType.SOCKS5, SMBTargetProxyServerType.SOCKS5_SSL]:
            return Socks5ProxyConnection(target = target)

        elif target.proxy.proxy_type in [SMBTargetProxyServerType.MULTIPLEXOR, SMBTargetProxyServerType.MULTIPLEXOR_SSL]:
            mpc = MultiplexorProxyConnection(target)
            socks_proxy = await mpc.connect()
            return socks_proxy

        return None