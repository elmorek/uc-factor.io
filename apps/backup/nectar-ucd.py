
def create_backup(device=None, backup_file=None):
    """
    :type device: dict
    :type backup_file: str
    """
    from apps.config import config
    from netmiko import ConnectHandler
    from netmiko.ssh_exception import NetMikoTimeoutException, NetMikoAuthenticationException
    assert isinstance(device, dict)
    assert isinstance(backup_file, str)
    config = config('DEV')
    backup_folder = config['backups_location']
    try:
        ucd_connect = ConnectHandler(**device)
    except (NetMikoTimeoutException, NetMikoAuthenticationException) as e:
        raise e
    running_config = ucd_connect.send_command('show run')
    with open('{}{}'.format(backup_folder, backup_file), 'w') as file:
        assert isinstance(running_config, str)
        file.write(running_config)
