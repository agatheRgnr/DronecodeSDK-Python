# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import discovery_pb2, discovery_pb2_grpc


class SystemInfo:
    """ Generated by dcsdkgen """

    def __init__(
            self,
            uuid,
            address,
            port,
            is_core_instance):
        """ Initializes the SystemInfo object """
        self.uuid = uuid
        self.address = address
        self.port = port
        self.is_core_instance = is_core_instance

    def __equals__(self, to_compare):
        """ Checks if two SystemInfo are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # SystemInfo object
            return \
                (self.uuid == to_compare.uuid) and \
                (self.address == to_compare.address) and \
                (self.port == to_compare.port) and \
                (self.is_core_instance == to_compare.is_core_instance)

        except AttributeError:
            return False

    def __repr__(self):
        """ SystemInfo in string representation """
        return "SystemInfo" + ", ".join(
                self.uuid,
                self.address,
                self.port,
                self.is_core_instance)

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return SystemInfo(
                response.system_info.uuid,
                response.system_info.address,
                response.system_info.port,
                response.system_info.is_core_instance)


class Discovery(AsyncBase):
    """ Generated by dcsdkgen - DronecodeSDK Discovery API """

    # Plugin name
    name = "Discovery"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = discovery_pb2_grpc.DiscoveryServiceStub(channel)

    def _response_success(self, response):
        """ Checks if the request was successfull """
        return (response.action_result.result ==
                discovery_pb2.ActionResult.SUCCESS)

    async def discovered_systems(self):
        """ Generated by dcsdkgen """
        async for response in self._stub.SubscribeDiscoveredSystems(
                    discovery_pb2.SubscribeDiscoveredSystemsRequest()):
                yield SystemInfo.parse_response(response)