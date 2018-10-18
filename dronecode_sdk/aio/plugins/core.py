# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import core_pb2, core_pb2_grpc


class PluginInfo:
    """ Generated by dcsdkgen """

    def __init__(
            self,
            name,
            address,
            port):
        """ Initializes the PluginInfo object """
        self.name = name
        self.address = address
        self.port = port

    def __equals__(self, to_compare):
        """ Checks if two PluginInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # PluginInfo object
            return \
                (self.name == to_compare.name) and \
                (self.address == to_compare.address) and \
                (self.port == to_compare.port)

        except AttributeError:
            return False

    def __repr__(self):
        """ PluginInfo in string representation """
        return "PluginInfo" + ", ".join(
                self.name,
                self.address,
                self.port)

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return PluginInfo(
                response.plugin_info.name,
                response.plugin_info.address,
                response.plugin_info.port)


class Core(AsyncBase):
    """ Generated by dcsdkgen - DronecodeSDK Core API """

    # Plugin name
    name = "Core"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = core_pb2_grpc.CoreServiceStub(channel)

    def _response_success(self, response):
        """ Checks if the request was successfull """
        return (response.action_result.result ==
                core_pb2.ActionResult.SUCCESS)

    async def discover(self):
        """ Generated by dcsdkgen """
        async for response in self._stub.SubscribeDiscover(
                    core_pb2.SubscribeDiscoverRequest()):
                yield response.uuid

    async def subscribeTimeout(self):
        """ Generated by dcsdkgen

        :returns: Tuple[Success, Response]
        """

        response = await self._stub.SubscribeTimeout(core_pb2.SubscribeTimeoutRequest())

        return self._response_success(response), response

    async def listRunningPlugins(self):
        """ Generated by dcsdkgen

        :returns: requested value
        """

        response = await self._stub.listRunningPlugins(core_pb2.ListRunningPluginsRequest())

        return response