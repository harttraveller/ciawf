from pydantic import BaseModel, validator


class State:
    name: str
    code: str
