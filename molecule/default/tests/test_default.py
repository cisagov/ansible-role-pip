"""Module containing the tests for the default scenario."""

# Standard Python Libraries
import os

# Third-Party Libraries
import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


def test_pip3(host):
    """Test that the appropriate pip3 packages were installed."""
    debian_pkgs = [
        "python3-dev",
        "python3-pip",
        "python3-setuptools",
    ]
    redhat_pkgs = ["python3-pip", "python3-devel"]
    if host.system_info.distribution in ["debian", "kali", "ubuntu"]:
        assert all(host.package(pkg).is_installed for pkg in debian_pkgs)
    elif host.system_info.distribution in ["amzn", "fedora"]:
        assert all(host.package(pkg).is_installed for pkg in redhat_pkgs)
    else:
        raise AssertionError(f"Unknown distribution {host.system_info.distribution}")


# Test that pip3 version is at least 19.0, which is the minimum version that
# supports pyproject.toml (required for installing some packages).
def test_pip3_version(host):
    """Test that pip3 version is at least 19.0."""
    pip3_version = host.check_output("pip3 --version").split()[1]
    major, minor, *_ = pip3_version.split(".")
    assert (int(major), int(minor)) >= (
        19,
        0,
    ), f"pip3 version {pip3_version} is less than 19.0"
