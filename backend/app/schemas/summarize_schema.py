import json
from pydantic import BaseModel, field_validator


class SummarizeSchema(BaseModel):
    """
    SummarizeSchema is used as request, 
    fields - text: str 
    """
    text: str
    
    @field_validator("text")
    def escape_quotes(cls, v: str):
        """
        created for fixing 422 erorr, when text has breaklines
        """
        return json.dumps(v)