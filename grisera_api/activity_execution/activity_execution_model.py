from typing import Optional, Any, List

from models.relation_information_model import RelationInformation
from pydantic import BaseModel

from property.property_model import PropertyIn


class ActivityExecutionIn(BaseModel):
    """
    Model of activity execution to acquire from client

    Attributes:
    activity_id (int): Id of activity
    arrangement_id (int) : Id of arrangement
    additional_properties (Optional[List[PropertyIn]]): Additional properties for activity execution
    """
    activity_id: int
    arrangement_id: int
    additional_properties: Optional[List[PropertyIn]]


class BasicActivityExecutionOut(BaseModel):
    """
    Basic model of activity execution

    Attributes:
    id (Optional[int]): Id of activity execution returned from graph api
    """
    id: Optional[int]


class ActivityExecutionOut(BasicActivityExecutionOut):
    """
    Model of activity execution to send to client as a result of request

    Attributes:
    relations (List[RelationInformation]): List of relations starting in activity execution node
    reversed_relations (List[RelationInformation]): List of relations ending in activity execution node
    errors (Optional[Any]): Optional errors appeared during query executions
    links (Optional[list]): List of links available from api
    """
    relations: List[RelationInformation] = []
    reversed_relations: List[RelationInformation] = []
    errors: Optional[Any] = None
    links: Optional[list] = None


class ActivityExecutionsOut(BasicActivityExecutionOut):
    """
    Model of activity executions to send to client as a result of request

    Attributes:
    activity_executions (List[BasicActivityExecutionOut]): Activity executions from database
    errors (Optional[Any]): Optional errors appeared during query executions
    links (Optional[list]): List of links available from api
    """
    activity_executions: List[BasicActivityExecutionOut] = []
    errors: Optional[Any] = None
    links: Optional[list] = None
