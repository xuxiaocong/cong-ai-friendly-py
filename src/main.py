from datetime import datetime

from fastapi import FastAPI
from src.core.lifespan import lifespan
from src.core.config import get_config
from src.core.exception.exception import BizException, SysException
from src.core.exception.exception_handler import biz_exception_handler, sys_exception_handler, unknown_exception_handler
from src.schema.base.response import Response

config = get_config()

app = FastAPI(
    lifespan=lifespan,
    openapi_url=config.SWAGGER_OPENAPI_URL,
    docs_url=config.SWAGGER_DOCS_URL,
    redoc_url=config.SWAGGER_REDOC_URL,
    responses={
        400: {
            "model": Response,
            "description": "请求参数错误",
        },
        500: {
            "model": Response,
            "description": "服务器内部错误",
        }
    },
)

# 全局异常处理
app.add_exception_handler(BizException, biz_exception_handler)
app.add_exception_handler(SysException, sys_exception_handler)
app.add_exception_handler(Exception, unknown_exception_handler)


@app.get("/api/health", summary="健康检查", description="检查服务是否正常运行")
def read_root():
    return {"status": "ok", "time": datetime.now().strftime("%Y-%m-%d %H:%M:%S.%f")}
