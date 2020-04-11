"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import pytest
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "pkg", ["python2-pip", "python-devel", "python3-pip", "python3-devel"]
)
def test_python_amazon(host, pkg):
    """Test that the appropriate packages were installed.

    Amazon Linux is behind Fedora, so that is why we need a separate
    test for that distribution.  If we tested an older version of
    Fedora it would use this test as well.
    """
    if host.system_info.distribution == "amzn":
        assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "pkg", ["python-pip", "python-dev", "python3-pip", "python3-dev"]
)
def test_python_debian(host, pkg):
    """Test that the appropriate packages were installed."""
    # host.system_info.release can be None if the release is still a
    # testing release that has not been officially released yet.  This
    # is currently (2020/03/27) the case for Debian 11 (Bullseye).
    if host.system_info.distribution == "debian" and (
        host.system_info.release is not None and int(host.system_info.release) < 11
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize("pkg", ["python3-pip", "python3-dev"])
def test_python_kali_and_debian_bullseye_and_later(host, pkg):
    """Test that the appropriate packages were installed.

    The packages python-pip and python-dev no longer exist in Bullseye
    or later.
    """
    # host.system_info.release can be None if the release is still a
    # testing release that has not been officially released yet.  This
    # is currently (2020/03/27) the case for Debian 11 (Bullseye).
    if (
        host.system_info.distribution == "debian"
        and (host.system_info.release is None or int(host.system_info.release) >= 11)
        or host.system_info.distribution == "kali"
    ):
        assert host.package(pkg).is_installed


@pytest.mark.parametrize(
    "pkg", ["python2-pip", "python2-devel", "python3-pip", "python3-devel"]
)
def test_python_fedora(host, pkg):
    """Test that the appropriate packages were installed."""
    if host.system_info.distribution == "fedora":
        assert host.package(pkg).is_installed
