from pydantic import BaseModel, Field


class PageRequest(BaseModel):
    """分页请求参数
    """
    page_index: int = Field(default=1, ge=1, title="页码", description="从1开始")
    page_size: int = Field(default=10, ge=1, title="每页数量", description="保证性能建议100以下")

    def get_offset(self) -> int:
        """偏移，用于数据库查询

        Returns:
            int: 分页后的偏移量
        """
        return (self.page_index - 1) * self.page_size

    def get_limit(self) -> int:
        """每页数量，用于数据库查询

        Returns:
            int: 每页数量
        """
        return self.page_size
