"""Storage module for class Logging"""
import logging


class Logging:
    """Errors checking class"""

    @staticmethod
    def error_info(response_status_code: int, response_reason: str) -> None:
        """
        Method gets error information
        :param response_status_code: number of response status code
        :param response_reason: error handling
        :return: error information
        """
        return logging.error(f'status code - {response_status_code}, error type - {response_reason}')
