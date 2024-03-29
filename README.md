# ansible-role-pip #

[![GitHub Build Status](https://github.com/cisagov/ansible-role-pip/workflows/build/badge.svg)](https://github.com/cisagov/ansible-role-pip/actions)
[![CodeQL](https://github.com/cisagov/ansible-role-pip/workflows/CodeQL/badge.svg)](https://github.com/cisagov/ansible-role-pip/actions/workflows/codeql-analysis.yml)

This is an Ansible role for installing [pip](https://pip.pypa.io).

## Requirements ##

This role uses the `package` Ansible module, so [its
requirements](https://docs.ansible.com/ansible/latest/modules/package_module.html#requirements)
apply.

## Role Variables ##

| Variable | Description | Default | Required |
|----------|-------------|---------|----------|
| pip_install_pip2 | A boolean indicating whether or not to install pip2 alongside pip3.  Note that this is only possible for Debian Buster; therefore, this role variable is ignored for any other distribution. | `false` | No |

## Dependencies ##

None.

## Installation ##

This role can be installed via the command:

```console
ansible-galaxy install --role-file path/to/requirements.yml
```

where `requirements.yml` looks like:

```yaml
---
- name: pip
  src: https://github.com/cisagov/ansible-role-pip
```

and may contain other roles as well.

For more information about installing Ansible roles via a YAML file,
please see [the `ansible-galaxy`
documentation](https://docs.ansible.com/ansible/latest/galaxy/user_guide.html#installing-multiple-roles-from-a-file).

## Example Playbook ##

Here's how to use it in a playbook:

```yaml
- hosts: all
  become: true
  become_method: sudo
  tasks:
    - name: Install pip
      ansible.builtin.include_role:
        name: pip
```

## Contributing ##

We welcome contributions!  Please see [`CONTRIBUTING.md`](CONTRIBUTING.md) for
details.

## License ##

This project is in the worldwide [public domain](LICENSE).

This project is in the public domain within the United States, and
copyright and related rights in the work worldwide are waived through
the [CC0 1.0 Universal public domain
dedication](https://creativecommons.org/publicdomain/zero/1.0/).

All contributions to this project will be released under the CC0
dedication. By submitting a pull request, you are agreeing to comply
with this waiver of copyright interest.

## Author Information ##

Shane Frasier - <jeremy.frasier@gwe.cisa.dhs.gov>
