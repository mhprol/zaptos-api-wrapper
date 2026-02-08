import pytest
from unittest.mock import MagicMock
from zaptos.endpoints.analytics import analytics as analytics_group
from zaptos.endpoints.conversations import conversations as conversations_group
from zaptos.endpoints.templates import templates as templates_group
from zaptos.endpoints.webhooks import webhooks as webhooks_group

# --- Analytics Tests ---

def test_analytics_summary(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {"total": 10}

    result = runner.invoke(analytics_group, ['summary'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/analytics/summary", params={"period": "day"})

def test_analytics_campaign(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {"stats": {}}

    result = runner.invoke(analytics_group, ['campaign', 'c1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/analytics/campaign/c1")

def test_analytics_messages(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {"count": 100}

    result = runner.invoke(analytics_group, ['messages', '--since', '2023-01-01'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/analytics/messages", params={"since": "2023-01-01"})

def test_analytics_conversations(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {"count": 50}

    result = runner.invoke(analytics_group, ['conversations'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/analytics/conversations", params={})

def test_analytics_export(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {"url": "http://export"}

    result = runner.invoke(analytics_group, ['export', '--format', 'csv'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/analytics/export", params={"format": "csv"})


# --- Conversations Tests ---

def test_conversations_list(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = []

    result = runner.invoke(conversations_group, ['list', '--unread'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/conversations", params={"unread": "true"})

def test_conversations_get(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {}

    result = runner.invoke(conversations_group, ['get', '123'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/conversations/123")

def test_conversations_assign(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {}

    result = runner.invoke(conversations_group, ['assign', '123', '--to', 'user1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/conversations/123/assign", json={"user": "user1"})

def test_conversations_close(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {}

    result = runner.invoke(conversations_group, ['close', '123'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/conversations/123/close", json={})

def test_conversations_search(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = []

    result = runner.invoke(conversations_group, ['search', '--query', 'hello'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/conversations/search", params={"query": "hello"})


# --- Templates Tests ---

def test_templates_list(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = []

    result = runner.invoke(templates_group, ['list'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/templates")

def test_templates_get(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = {}

    result = runner.invoke(templates_group, ['get', 't1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/templates/t1")

def test_templates_create(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"id": "t1"}

    with runner.isolated_filesystem():
        with open('template.json', 'w') as f:
            f.write('{"content": "Hello"}')

        result = runner.invoke(templates_group, ['create', '--name', 'T1', '--file', 'template.json'], obj=ctx_obj)

        assert result.exit_code == 0
        mock_client._post.assert_called_with("/templates", json={"content": "Hello", "name": "T1"})

def test_templates_update(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._put.return_value = {"id": "t1"}

    with runner.isolated_filesystem():
        with open('template.json', 'w') as f:
            f.write('{"content": "Hello Updated"}')

        result = runner.invoke(templates_group, ['update', 'T1', '--file', 'template.json'], obj=ctx_obj)

        assert result.exit_code == 0
        mock_client._put.assert_called_with("/templates/T1", json={"content": "Hello Updated", "name": "T1"})

def test_templates_delete(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._delete.return_value = {}

    result = runner.invoke(templates_group, ['delete', 'T1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._delete.assert_called_with("/templates/T1")

def test_templates_preview(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {}

    result = runner.invoke(templates_group, ['preview', 'T1', '--number', '123'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/templates/T1/preview", json={"number": "123"})


# --- Webhooks Tests ---

def test_webhooks_list(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = []

    result = runner.invoke(webhooks_group, ['list'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/webhooks")

def test_webhooks_create(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {"id": "w1"}

    result = runner.invoke(webhooks_group, ['create', '--url', 'http://hook.com', '--events', 'msg,stat'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/webhooks", json={"url": "http://hook.com", "events": ["msg", "stat"]})

def test_webhooks_delete(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._delete.return_value = {}

    result = runner.invoke(webhooks_group, ['delete', 'w1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._delete.assert_called_with("/webhooks/w1")

def test_webhooks_test(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._post.return_value = {}

    result = runner.invoke(webhooks_group, ['test', 'w1'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._post.assert_called_with("/webhooks/w1/test", json={})
