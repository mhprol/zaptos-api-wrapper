from click.testing import CliRunner
from zaptos.cli import cli
from zaptos.config import config as zaptos_config
import json
import os
import pytest
from unittest.mock import patch
import click
from contextlib import contextmanager

@pytest.fixture(autouse=True)
def reset_config():
    # Save original values
    original_instance = zaptos_config.zaptos_instance
    original_token = zaptos_config.zaptos_token
    original_ghl_key = zaptos_config.ghl_api_key
    original_ghl_location = zaptos_config.ghl_location_id
    original_output = zaptos_config.output

    yield

    # Restore
    zaptos_config.zaptos_instance = original_instance
    zaptos_config.zaptos_token = original_token
    zaptos_config.ghl_api_key = original_ghl_key
    zaptos_config.ghl_location_id = original_ghl_location
    zaptos_config.output = original_output

@contextmanager
def temporary_command(group, name):
    """Context manager to add a temporary command to a click group."""
    @group.command(name=name)
    @click.pass_context
    def cmd(ctx):
        click.echo(json.dumps({
            'instance': ctx.obj.config.zaptos_instance,
            'token': ctx.obj.config.zaptos_token,
            'ghl_key': ctx.obj.config.ghl_api_key,
            'ghl_location': ctx.obj.config.ghl_location_id,
            'output': ctx.obj.config.output
        }))
    yield
    if name in group.commands:
        del group.commands[name]

@contextmanager
def temporary_noop_command(group, name):
    """Context manager to add a temporary no-op command."""
    @group.command(name=name)
    def cmd():
        pass
    yield
    if name in group.commands:
        del group.commands[name]

def test_cli_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['--help'])
    assert result.exit_code == 0
    assert 'Zaptos WhatsApp API CLI Wrapper' in result.output

def test_messages_help():
    runner = CliRunner()
    result = runner.invoke(cli, ['messages', '--help'])
    assert result.exit_code == 0
    assert 'Manage and send messages' in result.output

def test_campaigns_create():
    runner = CliRunner()
    with runner.isolated_filesystem():
        with patch('zaptos.endpoints.campaigns.get_campaigns_file', return_value='zaptos_campaigns.json'):
            result = runner.invoke(cli, [
                'campaigns', 'create',
                '--name', 'Test Campaign',
                '--ghl-tag', 'test_tag',
                '--template', 'Hello {{name}}'
            ])
            assert result.exit_code == 0
            output = json.loads(result.output)
            assert output['status'] == 'created'
            assert output['id'] is not None

            # Check if file created
            assert os.path.exists('zaptos_campaigns.json')
            with open('zaptos_campaigns.json', 'r') as f:
                data = json.load(f)
                assert data[output['id']]['name'] == 'Test Campaign'

def test_flows_simulator():
    runner = CliRunner()
    result = runner.invoke(cli, ['flows', 'test', '--help'])
    assert result.exit_code == 0
    assert '--simulate' in result.output

def test_config_overrides():
    runner = CliRunner()

    with temporary_command(cli, 'test-config'):
        with patch('zaptos.cli.ZaptosClient') as MockZaptosClient:
            result = runner.invoke(cli, [
                '--instance', 'inst1',
                '--token', 'tok1',
                '--ghl-key', 'key1',
                '--ghl-location', 'loc1',
                '--output', 'text',
                'test-config'
            ])

            assert result.exit_code == 0
            data = json.loads(result.output)
            assert data['instance'] == 'inst1'
            assert data['token'] == 'tok1'
            assert data['ghl_key'] == 'key1'
            assert data['ghl_location'] == 'loc1'
            assert data['output'] == 'text'

            MockZaptosClient.assert_called_with(instance='inst1', token='tok1')

def test_client_initialization_partial():
    runner = CliRunner()

    with temporary_noop_command(cli, 'test-partial'):
        with patch('zaptos.cli.ZaptosClient') as MockZaptosClient:
             # Ensure clean state for config before invocation (handled by fixture)
             # But reset_config restores AFTER test, we need clean start too if env polluted config initially
             # We can manually reset config fields here to ensure no carry over from environment
             zaptos_config.zaptos_instance = ""
             zaptos_config.zaptos_token = ""

             result = runner.invoke(cli, [
                '--instance', 'inst1',
                # No token provided, and config cleared
                'test-partial'
             ])

             assert result.exit_code == 0
             MockZaptosClient.assert_not_called()

def test_ghl_client_initialization():
    runner = CliRunner()

    with temporary_noop_command(cli, 'test-ghl'):
        with patch('zaptos.cli.GHLClient') as MockGHLClient:
            # Clear existing config
            zaptos_config.ghl_api_key = ""
            zaptos_config.ghl_location_id = ""

            result = runner.invoke(cli, [
                '--ghl-key', 'ghl_key_1',
                '--ghl-location', 'ghl_loc_1',
                'test-ghl'
            ])

            assert result.exit_code == 0
            MockGHLClient.assert_called_with(api_key='ghl_key_1', location_id='ghl_loc_1')
