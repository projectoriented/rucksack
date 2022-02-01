"""Resources required to run VCFAnno"""
import toml

from pydantic import BaseModel
from typing import (
    List, Optional
)


class ConfigToml(BaseModel):
    block: str = "annotation"
    fields: List[str] = ["GQ"]
    ops: List[str] = ["self"]
    names: List[str] = ["exac"]
    columns: Optional[int] = None
    type: Optional[str] = None


def generate_toml():
    pass


def generate_lua():
    pass


def serialize(obj_model):
    serial_item = toml.dumps(obj_model)
    received_toml = toml.loads(serial_item)
    return received_toml


def write_toml(serialized):
    with open("data.txt", "w") as writer:
        writer.write(serialized)
