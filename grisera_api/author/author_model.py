from pydantic import BaseModel
from typing import Optional, Any


class AuthorIn(BaseModel):
    """
    Model of author to acquire from client

    Attributes:
        name (str): Name and Surname of author
        institution (Optional[str]): Name of the institution
    """
    name: str
    institution: Optional[str]


class AuthorOut(AuthorIn):
    """
    Model of author to send to client as a result of request

    Attributes:
        id (Optional[int]): Id of author returned from graph api
        errors (Optional[Any]): Optional errors appeared during query executions
        links (Optional[list]): List of links available from api
    """
    id: Optional[int]
    errors: Optional[Any] = None
    links: Optional[list] = None