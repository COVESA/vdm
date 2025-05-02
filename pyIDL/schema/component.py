from pydantic import BaseModel, Field, model_validator
from typing import List, Union
from schema.namespace import NameSpace

class Property(BaseModel):
    name: str
    description: str | None = None
    basetype: str
    min: Union[int, float, None] = None
    max: Union[int, float, None] = None

    @model_validator(mode="after")
    def validate_min(self):
        if self.min and self.max and self.min > self.max:
            raise ValueError("min cannot be greater than max")
        return self

class Component(BaseModel):
    name: str
    description: str
    namespace: str
    properties: List[Property] = Field(default_factory=list)