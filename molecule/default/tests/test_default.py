"""Module containing the tests for the default scenario."""

import os

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_pip(host):
    """Test that the appropriate pip packages were installed."""
    if host.system_info.distribution == "debian":
        pkgs = ["python-pip", "python-dev", "python3-pip", "python3-dev"]
    elif host.system_info.distribution == "fedora":
        pkgs = ["python2-pip", "python2-devel", "python3-pip", "python3-devel"]
    elif host.system_info.distribution == "amzn":
        pkgs = ["python27-pip", "python27-devel", "python36-pip", "python36-devel"]
    else:
        pkgs = []
    packages = [host.package(pkg) for pkg in pkgs]
    installed = [package.is_installed for package in packages]
    assert len(pkgs) != 0
    assert all(installed)
