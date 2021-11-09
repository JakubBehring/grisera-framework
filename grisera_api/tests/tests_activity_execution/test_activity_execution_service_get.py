import unittest
import unittest.mock as mock

from graph_api_service import GraphApiService
from models.not_found_model import *
from activity_execution.activity_execution_model import *
from activity_execution.activity_execution_service import ActivityExecutionService


class TestActivityExecutionServiceGet(unittest.TestCase):

    @mock.patch.object(GraphApiService, 'get_node')
    @mock.patch.object(GraphApiService, 'get_node_relationships')
    def test_get_activity_execution_without_error(self, get_node_relationships_mock, get_node_mock):
        id_node = 1
        get_node_mock.return_value = {'id': id_node, 'labels': ['Activity Execution'],
                                      'properties': [],
                                      "errors": None, 'links': None}
        get_node_relationships_mock.return_value = {"relationships": [
            {"start_node": id_node, "end_node": 19,
             "name": "testRelation", "id": 0,
             "properties": None},
            {"start_node": 15, "end_node": id_node,
             "name": "testReversedRelation", "id": 0,
             "properties": None}]}
        activity_execution = ActivityExecutionOut(id=id_node,
                                                  relations=[RelationInformation(second_node_id=19, name="testRelation",
                                                                                 relation_id=0)],
                                                  reversed_relations=[RelationInformation(second_node_id=15,
                                                                                          name="testReversedRelation",
                                                                                          relation_id=0)])
        activity_execution_service = ActivityExecutionService()

        result = activity_execution_service.get_activity_execution(id_node)

        self.assertEqual(result, activity_execution)
        get_node_mock.assert_called_once_with(id_node)
        get_node_relationships_mock.assert_called_once_with(id_node)

    @mock.patch.object(GraphApiService, 'get_node')
    def test_get_activity_execution_without_label(self, get_node_mock):
        id_node = 1
        get_node_mock.return_value = {'id': id_node, 'labels': ['Test'], 'properties': None,
                                      "errors": None, 'links': None}
        not_found = NotFoundByIdModel(id=id_node, errors="Node not found.")
        activity_execution_service = ActivityExecutionService()

        result = activity_execution_service.get_activity_execution(id_node)

        self.assertEqual(result, not_found)
        get_node_mock.assert_called_once_with(id_node)

    @mock.patch.object(GraphApiService, 'get_node')
    def test_get_activity_execution_with_error(self, get_node_mock):
        id_node = 1
        get_node_mock.return_value = {'id': id_node, 'errors': ['error'], 'links': None}
        not_found = NotFoundByIdModel(id=id_node, errors=['error'])
        activity_execution_service = ActivityExecutionService()

        result = activity_execution_service.get_activity_execution(id_node)

        self.assertEqual(result, not_found)
        get_node_mock.assert_called_once_with(id_node)

    @mock.patch.object(GraphApiService, 'get_nodes')
    def test_get_activity_executions(self, get_nodes_mock):
        get_nodes_mock.return_value = {'nodes': [{'id': 1, 'labels': ['Activity Execution'],
                                                  'properties': [{'key': 'age', 'value': 5},
                                                                 {'key': 'test', 'value': 'test'}]},
                                                 {'id': 2, 'labels': ['Activity Execution'],
                                                  'properties': [{'key': 'age', 'value': 10},
                                                                 {'key': 'test2', 'value': 'test3'}]}]}
        activity_execution_one = BasicActivityExecutionOut(id=1)
        activity_execution_two = BasicActivityExecutionOut(id=2)
        activity_executions = ActivityExecutionsOut(
            activity_executions=[activity_execution_one, activity_execution_two])
        activity_executions_service = ActivityExecutionService()

        result = activity_executions_service.get_activity_executions()

        self.assertEqual(result, activity_executions)
        get_nodes_mock.assert_called_once_with("`Activity Execution`")

    @mock.patch.object(GraphApiService, 'get_nodes')
    def test_get_activity_executions_empty(self, get_nodes_mock):
        get_nodes_mock.return_value = {'nodes': []}
        activity_executions = ActivityExecutionsOut(activity_execution=[])
        activity_executions_service = ActivityExecutionService()

        result = activity_executions_service.get_activity_executions()

        self.assertEqual(result, activity_executions)
        get_nodes_mock.assert_called_once_with("`Activity Execution`")