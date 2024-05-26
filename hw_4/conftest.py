from datetime import datetime
import pytest
from sshcheckers import data, ssh_getout, ssh_checkout


@pytest.fixture()
def start_time():
    """
    fixture for showing time
    :return:
    """
    return datetime.now().strftime('%Y-%m-%d %H:%M:%S')

# @pytest.fixture()
# def clear_programs():
#     return ssh_checkout(data['host'], data['user'], data['passwd'], f"echo {data['passwd']} | sudo -S dpkg -r /home/{data['user']}/{data['pocket_name']}", "")