from unittest.mock import patch


with patch('sys.stdout') as mock_stdout:
    print('hello')
    assert mock_stdout.write.called


print('world')
