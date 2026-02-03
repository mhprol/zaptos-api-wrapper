from click.testing import CliRunner
from zaptos.cli import cli
import json
import os
from unittest.mock import patch

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
    # Mocking a campaign creation
    with runner.isolated_filesystem():
        # Patch get_campaigns_file to use a local file in the isolated fs
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
    # We can't easily test interactive prompt in this simple way without inputs
    # But we can test help
    result = runner.invoke(cli, ['flows', 'test', '--help'])
    assert result.exit_code == 0
    assert '--simulate' in result.output
