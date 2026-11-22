from pydantic import BaseModel, ConfigDict


class BaseCS2Model(BaseModel):
    model_config = ConfigDict(
        strict=True,
        extra="forbid",
        frozen=True,
    )
