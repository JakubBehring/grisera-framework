from typing import Set, Optional, Any
from pydantic import BaseModel


class NodeIn(BaseModel):
    """
    Model of node to acquire from client

    Attributes:
        labels (Optional[Set[str]]): Labels added to node in graph DB
    """
    labels: Optional[Set[str]] = []


class NodeOut(NodeIn):
    """
    Model of node to send to client as a result of request

    Attributes:
        id (Optional[int]): Id of node returned from graph database
        errors (Optional[Any]): Optional errors appeared during query executions
    """
    id: Optional[int]
    errors: Optional[Any] = None
