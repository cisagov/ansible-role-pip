"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_pip2(host):
    """Test that the appropriate pip2 packages were installed."""
    debian_buster_pkgs = ["python-pip", "python2-dev"]
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        if host.system_info.codename in ["buster"]:
            assert all([host.package(pkg).is_installed for pkg in debian_buster_pkgs])
        else:
            # pip2 is not installed in this case
            pass
    elif host.system_info.distribution in ["amzn", "fedora"]:
        # pip2 is not installed in this case
        pass
    else:
        assert False, f"Unknown distribution {host.system_info.distribution}"
