from pydantic import BaseModel


class User(BaseModel):
    ip: str
    username: str
    private_key: str


class Msg(BaseModel):
    ip: str
    msg: str
    from_ip: str
