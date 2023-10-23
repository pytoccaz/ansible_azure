# Ansible Collection - pytoccaz.azure

<!--start requires_ansible-->
## Ansible version compatibility

This collection has been tested against following Ansible versions: **>=2.13.13**.

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
[pytoccaz.azure.az_blobcontainer_list](https://github.com/pytoccaz/ansible_azure/blob/master/docs/pytoccaz.azure.az_blobcontainer_list_module.rst)|List Azure blobs module

<!--end collection content-->

## Credits
This program is inspired by and contains code snippets from `azure.azcollection.azure_rm_storageshare` module by Andrii Bilorus.

It also contains documentation fragments from `azure.azcollection.azure` doc_fragments file by Matt Davis and Chris Houseknecht.
