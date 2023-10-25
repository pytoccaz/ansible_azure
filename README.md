# Ansible Collection - pytoccaz.azure

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.13.13**.

For collections that support Ansible 2.9, please ensure you update your `network_os` to use the
fully qualified collection name (for example, `cisco.ios.ios`).
Plugins and modules within a collection may be tested with only specific Ansible versions.
A collection may contain metadata that identifies these versions.
PEP440 is the schema used to describe the versions of Ansible.
<!--end requires_ansible-->

This collection has been tested against `azure.azcollection` version **1.18.1**.

## Installation

Collection `azure.azcollection` is required. 

Download from Galaxy:

```bash
ansible-galaxy collection install pytoccaz.azure
```

## Collection content

<!--start collection content-->
### Modules
Name | Description
--- | ---
[pytoccaz.azure.az_blobcontainer_list](https://github.com/pytoccaz/ansible_azure/blob/v1.1.0/docs/pytoccaz.azure.az_blobcontainer_list_module.rst)|List Azure blobs module

<!--end collection content-->

## Credits
This program is inspired by and contains code snippets from `azure.azcollection.azure_rm_storageshare` module by Andrii Bilorus.

It also contains documentation fragments from `azure.azcollection.azure` doc_fragments file by Matt Davis and Chris Houseknecht.
