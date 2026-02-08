import pytest
from unittest.mock import MagicMock
from zaptos.endpoints.messages import messages as messages_group

def test_messages_send_text(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_text.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--text', 'Hello'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_text.assert_called_with('123', 'Hello')

def test_messages_send_image(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_image.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--image', 'http://img.com', '--caption', 'Cap'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_image.assert_called_with('123', 'http://img.com', 'Cap')

def test_messages_send_buttons_json(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_buttons.return_value = {"id": "m1"}

    buttons_json = '{"title": "T", "buttons": [{"id": "b1", "text": "Yes"}]}'
    result = runner.invoke(messages_group, ['send', '123', '--buttons', buttons_json], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_buttons.assert_called_with('123', 'T', [{"id": "b1", "text": "Yes"}], None)

def test_messages_send_list_json(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_list.return_value = {"id": "m1"}

    list_json = '{"title": "T", "sections": [], "buttonText": "Show"}'
    result = runner.invoke(messages_group, ['send', '123', '--list', list_json], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_list.assert_called_with('123', 'T', [], "Show", None)

def test_messages_send_carousel_file(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_carousel.return_value = {"id": "m1"}
    carousel_json = '{"cards": [{"title": "C1"}]}'

    with runner.isolated_filesystem():
        with open('carousel.json', 'w') as f:
            f.write(carousel_json)

        result = runner.invoke(messages_group, ['send', '123', '--carousel', 'carousel.json'], obj=ctx_obj)

        assert result.exit_code == 0
        mock_client.send_carousel.assert_called_with('123', [{"title": "C1"}])

def test_messages_send_location(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_location.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--location', '40,-70', '--address', 'Addr', '--caption', 'Name'], obj=ctx_obj)

    assert result.exit_code == 0
    # Note: --caption is passed as name to send_location in messages.py
    mock_client.send_location.assert_called_with('123', '40', '-70', 'Addr', name='Name')

def test_messages_send_contact(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_contact.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--contact-name', 'John', '--contact-number', '999'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_contact.assert_called_with('123', 'John', '999')

def test_messages_send_document(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_document.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--document', 'http://doc.pdf', '--filename', 'doc.pdf', '--caption', 'Cap'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_document.assert_called_with('123', 'http://doc.pdf', 'doc.pdf', 'Cap')

def test_messages_send_audio(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_audio.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--audio', 'http://aud.mp3'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_audio.assert_called_with('123', 'http://aud.mp3')

def test_messages_send_video(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_video.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--video', 'http://vid.mp4', '--caption', 'Cap'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_video.assert_called_with('123', 'http://vid.mp4', 'Cap')

def test_messages_send_sticker(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client.send_sticker.return_value = {"id": "m1"}

    result = runner.invoke(messages_group, ['send', '123', '--sticker', 'http://stick.webp'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client.send_sticker.assert_called_with('123', 'http://stick.webp')

def test_messages_list(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client
    mock_client._get.return_value = []

    result = runner.invoke(messages_group, ['list', '--contact', '123'], obj=ctx_obj)

    assert result.exit_code == 0
    mock_client._get.assert_called_with("/messages", params={'contact': '123'})

def test_messages_send_error(runner, mock_client):
    ctx_obj = MagicMock()
    ctx_obj.client = mock_client

    result = runner.invoke(messages_group, ['send', '123'], obj=ctx_obj)

    assert result.exit_code == 0 # Command doesn't fail exit code, but prints error
    assert "Error: No message content provided" in result.output
