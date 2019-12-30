import os
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ['MOLECULE_INVENTORY_FILE']).get_hosts('icinga2master')


def test_master_config(host):
    """ basic configuration checks
    """
    with host.sudo():
        # Check if zone is configured
        file = host.file('/etc/icinga2/zones.conf')
        assert file.exists
        assert file.user == 'icinga'
        assert file.group == 'icinga'
        assert file.mode == 0o644
        assert file.contains('object Endpoint "')

        # Check if global templates are set
        assert host.file('/etc/icinga2/zones.d/global-templates/commands.conf').exists
        assert host.file('/etc/icinga2/zones.d/global-templates/groups.conf').exists
        assert host.file('/etc/icinga2/zones.d/global-templates/templates.conf').exists

        # Check if config dirs exist
        assert host.file('/etc/icinga2/zones.d/global-templates/groups').is_directory
        assert host.file('/etc/icinga2/zones.d/master').is_directory

        # Check if features are enables
        assert host.file('/etc/icinga2/features-enabled/api.conf').is_symlink
        assert host.file('/etc/icinga2/features-enabled/ido-mysql.conf').is_symlink

        # Check if config is active
        zones = host.run('icinga2 object list --type zone')
        assert "Object 'global-templates' of type 'Zone'" in zones.stdout
        assert "Object 'director-global' of type 'Zone'" in zones.stdout
        assert "Object 'master' of type 'Zone'" in zones.stdout
