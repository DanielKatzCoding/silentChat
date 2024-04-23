from pydantic import BaseModel


class User(BaseModel):
    ip: str
    username: str
    private_key: str


class Msgs(BaseModel):
    username: str
    msg: str
    send_to_username: str
    # In seconds
    timer_del: int
