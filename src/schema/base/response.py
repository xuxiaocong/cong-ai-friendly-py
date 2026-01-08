from typing import Any, TypeVar, Generic
from pydantic import BaseModel, Field

T = TypeVar("T")


class Response(BaseModel):
    """基础响应类
    场景: 无响应数据、响应异常
    例如: Response() 、 Response(success=False, err_code="AUTH_ERROR", err_message="鉴权失败")
    """
    success: bool = Field(default=True, title="是否成功")
    err_code: str = Field(default="SUCCESS", title="错误码")
    err_message: str = Field(default="OK", title="错误信息")


class SingleResponse(Response, Generic[T]):
    """单条数据响应
    场景: 响应单条数据
    例如: SingleResponse(data=User(id=1, name="张三"))
    """
    data: T | None = Field(default=None, title="数据")


class MultiResponse(Response, Generic[T]):
    """多条数据响应
    场景: 响应多条数据
    例如: MultiResponse(data=[User(id=1, name="张三"), User(id=2, name="李四")])
    """
    data: list[T] = Field(default=[], title="数据")


class PageResponse(Response, Generic[T]):
    """分页数据响应
    场景: 响应分页数据
    例如: PageResponse(total_count=100, data=[User(id=1, name="张三"), User(id=2, name="李四")])
    """
    total_count: int = Field(default=0, title="数据总数")
    data: list[T] = Field(default=[], title="当前分页数据")
