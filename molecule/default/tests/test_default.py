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
    amazon_pkgs = ["python2-pip", "python-devel"]
    debian_stretch_pkgs = ["python-pip", "python-dev"]
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        # We treat Debian 9 as a special case because the CyHy AMIs
        # (and only the CyHy AMIs) are built on it.  Therefore it
        # requires python2.
        if (
            host.system_info.distribution == "debian"
            and host.system_info.codename == "stretch"
        ):
            assert all([host.package(pkg).is_installed for pkg in debian_stretch_pkgs])
    elif host.system_info.distribution in ["amzn", "fedora"]:
        # Amazon Linux 2 is woefully behind the times and requires
        # Python 2 to support its antiquated version of the yum
        # package manager.
        if host.system_info.distribution == "amzn":
            assert all([host.package(pkg).is_installed for pkg in amazon_pkgs])
    else:
        assert False, f"Unknown distribution {host.system_info.distribution}"


def test_pip3(host):
    """Test that the appropriate pip3 packages were installed."""
    debian_pkgs = ["python3-pip", "python3-dev"]
    redhat_pkgs = ["python3-pip", "python3-devel"]
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        assert all([host.package(pkg).is_installed for pkg in debian_pkgs])
    elif host.system_info.distribution in ["amzn", "fedora"]:
        assert all([host.package(pkg).is_installed for pkg in redhat_pkgs])
    else:
        assert False, f"Unknown distribution {host.system_info.distribution}"
