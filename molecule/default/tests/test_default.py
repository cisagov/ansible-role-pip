import os
import pytest

import testinfra.utils.ansible_runner

testinfra_hosts = testinfra.utils.ansible_runner.AnsibleRunner(
    os.environ["MOLECULE_INVENTORY_FILE"]
).get_hosts("all")


@pytest.mark.parametrize(
    "pkgs",
    [
        ["python-pip", "python27-pip"],
        ["python3-pip", "python36-pip"],
        ["python-dev", "python27-devel"],
        ["python3-dev", "python36-devel"],
    ],
)
def test_pip(host, pkgs):
    packages = [host.package(pkg) for pkg in pkgs]
    installed = [package.is_installed for package in packages]
    assert any(installed)
