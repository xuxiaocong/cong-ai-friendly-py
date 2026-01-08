from loguru import logger
from fastapi import Request
from fastapi.responses import JSONResponse
from src.core.exception.exception import BizException, SysException
from src.schema.base.response import Response


async def biz_exception_handler(request: Request, exc: BizException):
    """业务逻辑异常
    例如：参数校验失败、业务逻辑处理失败等，通常是用户操作错误导致的异常
    """
    resp = Response(success=False, err_code=exc.err_code, err_message=exc.err_message)
    return JSONResponse(status_code=400, content=resp.model_dump())


async def sys_exception_handler(request: Request, exc: SysException):
    """系统异常
    例如：数据库连接失败、文件读写失败等，通常是系统环境问题导致的异常
    """
    logger.error(f"系统异常，请求：[{request.method}] {request.url.path}，异常信息：[{exc.err_code}] {exc.err_message}")
    logger.exception(exc)
    resp = Response(success=False, err_code=exc.err_code, err_message=exc.err_message)
    return JSONResponse(status_code=500, content=resp.model_dump())


async def unknown_exception_handler(request: Request, exc: Exception):
    """未知异常
    例如：未处理的异常、未预料到的异常等，通常是代码bug导致的异常
    """
    logger.error(f"未知异常，请求：[{request.method}] {request.url.path}，异常信息：{exc}")
    logger.exception(exc)
    resp = Response(success=False, err_code="sys_error", err_message="系统异常")
    return JSONResponse(status_code=500, content=resp.model_dump())
