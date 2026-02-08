import pytest
from unittest.mock import MagicMock
from zaptos.endpoints.flows import flows as flows_group

def test_flows_list(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = [{"id": "f1", "name": "Flow 1"}]

    result = runner.invoke(flows_group, ['list'], obj=ctx_obj)

    assert result.exit_code == 0
    assert "Flow 1" in result.output
    mock_client._get.assert_called_with("/flows")

def test_flows_get(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {"id": "f1", "name": "Flow 1"}

    result = runner.invoke(flows_group, ['get', 'f1'], obj=ctx_obj)

    assert result.exit_code == 0
    assert "Flow 1" in result.output
    mock_client._get.assert_called_with("/flows/f1")

def test_flows_create(runner, mock_client):
    yaml_content = "name: New Flow\nsteps: []"
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"id": "new", "status": "created"}

    with runner.isolated_filesystem():
        with open('flow.yaml', 'w') as f:
            f.write(yaml_content)

        result = runner.invoke(flows_group, ['create', '--name', 'New Flow', '--file', 'flow.yaml'], obj=ctx_obj)

        assert result.exit_code == 0
        assert "created" in result.output
        mock_client._post.assert_called()
        args = mock_client._post.call_args[1]
        assert args['json']['name'] == 'New Flow'

def test_flows_update(runner, mock_client):
    yaml_content = "name: Updated Flow\nsteps: []"
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._put.return_value = {"status": "updated"}

    with runner.isolated_filesystem():
        with open('flow.yaml', 'w') as f:
            f.write(yaml_content)

        result = runner.invoke(flows_group, ['update', 'f1', '--file', 'flow.yaml'], obj=ctx_obj)

        assert result.exit_code == 0
        assert "updated" in result.output
        mock_client._put.assert_called()

def test_flows_enable(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"status": "enabled"}

    result = runner.invoke(flows_group, ['enable', 'f1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/flows/f1/enable", json={})

def test_flows_disable(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"status": "disabled"}

    result = runner.invoke(flows_group, ['disable', 'f1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/flows/f1/disable", json={})

def test_flows_test_server(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"status": "testing"}

    result = runner.invoke(flows_group, ['test', 'f1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/flows/f1/test", json={})

def test_flows_simulate(runner, mock_client):
    flow_data = {
        "id": "f1",
        "name": "Sim Flow",
        "steps": [
            {
                "id": "s1",
                "message": {"type": "text", "text": "Hello"},
                "next": "s2"
            },
            {
                "id": "s2",
                "message": {"type": "buttons", "buttons": [{"text": "Yes", "id": "btn1", "next": "s3"}]},
                "next": None # Button determines next
            },
            {
                "id": "s3",
                "message": {"type": "text", "text": "Bye"},
                "next": None
            }
        ]
    }

    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = flow_data

    # Simulate user input "1" for the button choice
    result = runner.invoke(flows_group, ['test', 'f1', '--simulate'], obj=ctx_obj, input="1\n")

    assert result.exit_code == 0
    assert "Simulating Flow: Sim Flow" in result.output
    assert "[Bot]: Hello" in result.output
    assert "Choose an option" in result.output
    assert "1. Yes (ID: btn1)" in result.output
    assert "[Bot]: Bye" in result.output
    assert "--- End of Flow ---" in result.output
