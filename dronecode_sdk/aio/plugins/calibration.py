# -*- coding: utf-8 -*-
from .._base import AsyncBase
from ..generated import calibration_pb2, calibration_pb2_grpc


class CalibrationResult:
    """ Generated by dcsdkgen """

    def __init__(
            self,
            result,
            result_str):
        """ Initializes the CalibrationResult object """
        self.result = result
        self.result_str = result_str

    def __equals__(self, to_compare):
        """ Checks if two CalibrationResult are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # CalibrationResult object
            return \
                (self.result == to_compare.result) and \
                (self.result_str == to_compare.result_str)

        except AttributeError:
            return False

    def __repr__(self):
        """ CalibrationResult in string representation """
        return "CalibrationResult" + ", ".join(
                self.result,
                self.result_str)

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return CalibrationResult(
                response.calibration_result.result,
                response.calibration_result.result_str)


class ProgressData:
    """ Generated by dcsdkgen """

    def __init__(
            self,
            has_progress,
            progress,
            has_status_text,
            status_text):
        """ Initializes the ProgressData object """
        self.has_progress = has_progress
        self.progress = progress
        self.has_status_text = has_status_text
        self.status_text = status_text

    def __equals__(self, to_compare):
        """ Checks if two ProgressData are the same """
        try:
            # Try to compare - this likely fails when it is compared to a non
            # ProgressData object
            return \
                (self.has_progress == to_compare.has_progress) and \
                (self.progress == to_compare.progress) and \
                (self.has_status_text == to_compare.has_status_text) and \
                (self.status_text == to_compare.status_text)

        except AttributeError:
            return False

    def __repr__(self):
        """ ProgressData in string representation """
        return "ProgressData" + ", ".join(
                self.has_progress,
                self.progress,
                self.has_status_text,
                self.status_text)

    @staticmethod
    def parse_response(response):
        """ Parses a gRPC response """
        return ProgressData(
                response.progress_data.has_progress,
                response.progress_data.progress,
                response.progress_data.has_status_text,
                response.progress_data.status_text)


class Calibration(AsyncBase):
    """ Generated by dcsdkgen - DronecodeSDK Calibration API """

    # Plugin name
    name = "Calibration"

    def _setup_stub(self, channel):
        """ Setups the api stub """
        self._stub = calibration_pb2_grpc.CalibrationServiceStub(channel)

    def _response_success(self, response):
        """ Checks if the request was successfull """
        return (response.action_result.result ==
                calibration_pb2.ActionResult.SUCCESS)

    async def calibrate_gyro(self):
        """ Generated by dcsdkgen """
        async for response in self._stub.SubscribeCalibrateGyro(
                    calibration_pb2.SubscribeCalibrateGyroRequest()):
                yield ProgressData.parse_response(response)

    async def calibrate_accelerometer(self):
        """ Generated by dcsdkgen """
        async for response in self._stub.SubscribeCalibrateAccelerometer(
                    calibration_pb2.SubscribeCalibrateAccelerometerRequest()):
                yield ProgressData.parse_response(response)

    async def calibrate_magnetometer(self):
        """ Generated by dcsdkgen """
        async for response in self._stub.SubscribeCalibrateMagnetometer(
                    calibration_pb2.SubscribeCalibrateMagnetometerRequest()):
                yield ProgressData.parse_response(response)

    async def calibrate_gimbal_accelerometer(self):
        """ Generated by dcsdkgen """
        async for response in self._stub.SubscribeCalibrateGimbalAccelerometer(
                    calibration_pb2.SubscribeCalibrateGimbalAccelerometerRequest()):
                yield ProgressData.parse_response(response)