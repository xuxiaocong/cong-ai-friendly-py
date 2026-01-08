from datetime import datetime
from zoneinfo import ZoneInfo
from sqlmodel import SQLModel, Field, Integer, Boolean, TIMESTAMP
from src.core.config import get_config

tz = ZoneInfo(get_config().TIME_ZONE)


class BaseModel(SQLModel):
    """数据库基础模型
    """
    id: int | None = Field(
        sa_type=Integer,
        default=None,
        primary_key=True,
        sa_column_kwargs={
            "comment": "主键",
            "autoincrement": True
        },
    )
    create_time: datetime = Field(
        sa_type=TIMESTAMP(timezone=True),
        default_factory=lambda: datetime.now(tz),
        sa_column_kwargs={"comment": "创建时间"},
    )
    update_time: datetime = Field(
        sa_type=TIMESTAMP(timezone=True),
        default_factory=lambda: datetime.now(tz),
        sa_column_kwargs={
            "comment": "更新时间",
            "onupdate": lambda: datetime.now(tz)
        },
    )
    is_deleted: bool = Field(
        sa_type=Boolean,
        default=False,
        sa_column_kwargs={"comment": "是否删除"},
    )
