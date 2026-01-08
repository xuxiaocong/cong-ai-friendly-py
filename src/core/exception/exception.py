class BizException(Exception):
    """业务异常
    """

    def __init__(self, *, err_code: str = "ERROR", err_message: str = "业务异常"):
        self.err_code = err_code
        self.err_message = err_message


class SysException(Exception):
    """系统异常
    """

    def __init__(self, *, err_code: str = "ERROR", err_message: str = "系统错误"):
        self.err_code = err_code
        self.err_message = err_message
