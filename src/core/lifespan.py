from loguru import logger
from fastapi import FastAPI
from fastapi.concurrency import asynccontextmanager
from src.core.config import get_config


@asynccontextmanager
async def lifespan(app: FastAPI):
    """生命周期管理器"""
    logger.add("logs/info.log", rotation="00:00", retention="7 days")
    logger.add("logs/error.log", rotation="00:00", retention="7 days", level="ERROR")

    logger.info("正在启动程序...")
    logger.info("当前配置：{}", get_config())
    yield
    logger.info("程序停止运行")
