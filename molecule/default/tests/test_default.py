"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize("pkg", ["python-pip", "python-dev"])
def test_python_debian(host, pkg):
    """Test that the appropriate packages were installed.

    We treat Debian 9 and 10 as special cases because the CyHy AMIs (and
    only the CyHy AMIs) are built on them.  Therefore they require
    python2.
    """
    if host.system_info.distribution == "debian" and (
        host.system_info.codename == "stretch" or host.system_info.codename == "buster"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3-pip", "python3-dev"])
def test_python3_debian(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "debian":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3-pip", "python3-devel"])
def test_python3_redhat(host, pkg):
    """Test that the appropriate packages were installed."""
    if (
        host.system_info.distribution == "fedora"
        or host.system_info.distribution == "amzn"
    ):
        assert host.package(pkg).is_installed
