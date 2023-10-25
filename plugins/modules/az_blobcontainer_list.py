#!/usr/bin/python

# Copyright: (c) 2023, Olivier BERNARD
# GNU General Public License v3.0+ (see COPYING or https://www.gnu.org/licenses/gpl-3.0.txt)
from __future__ import (absolute_import, division, print_function)

__metaclass__ = type

DOCUMENTATION = r'''
---
module: az_blobcontainer_list

short_description: List Azure blobs module

version_added: "1.0.0"

description: Lists the blobs under a specified azure storage container.

options:
    resource_group:
        description:
            - Name of the resource group to use.
        required: true
        aliases:
            - resource_group_name
        version_added: '1.0.0'
    storage_account_name:
        description:
            - Name of the storage account to use.
        required: true
        aliases:
            - account_name
            - storage_account
        version_added: '1.0.0'
    container:
        description:
            - Name of a blob container within the storage account.
        required: true
        aliases:
            - container_name
        version_added: '1.0.0'
    name_starts_with:
        description:
            - Filters the results to return only blobs whose names begin with the specified prefix.
        required: false
        aliases:
            - start_with
        version_added: '1.0.0'
    datetime_format:
        description:
            - Rendering format for last_modified container and blobs date.
        required: false
        default: '%Y-%m-%d %H:%M:%S'
        aliases:
            - dt_format
        version_added: '1.1.0'

extends_documentation_fragment:
    - pytoccaz.azure.azure

author:
    - Olivier Bernard (@pytoccaz)

'''

EXAMPLES = r'''
# List blobs under a container
- name: List blobs under mycontainer
  az_blobcontainer_list:
    resource_group: myresourcegroup
    account_name: myaccountname
    container: mycontainer

'''

RETURN = r'''
blobs:
    description:
        - List of blobs.
    returned: always
    type: list
    sample:
        [
            {
                "content_length": 136532,
                "content_settings": {
                    "cache_control": null,
                    "content_disposition": null,
                    "content_encoding": null,
                    "content_language": null,
                    "content_md5": null,
                    "content_type": "application/image"
                },
                "last_modified": "09-Mar-2016 22:08:25",
                "name": "foo.png",
                "tags": {},
                "type": "BlockBlob"
            }
        ]
container:
    description:
        - Facts about the current state of the selected container.
    returned: always
    type: dict
    sample: {
        "last_modified": "2016-03-09 19:28:26",
        "name": "foo",
        "tags": {}
    }

'''
from ansible_collections.azure.azcollection.plugins.module_utils.azure_rm_common import AzureRMModuleBase
import re

try:
    from azure.core.exceptions import ResourceNotFoundError
except ImportError:
    # This is handled in azure_rm_common
    pass


class AzureBlobContainerList(AzureRMModuleBase):

    def __init__(self):

        self.module_arg_spec = dict(
            storage_account_name=dict(required=True, type='str', aliases=[
                                      'account_name', 'storage_account']),
            container=dict(required=True, type='str',
                           aliases=['container_name']),
            resource_group=dict(required=True, type='str',
                                aliases=['resource_group_name']),
            name_starts_with=dict(required=False, type='str',
                                  aliases=['starts_with']),
            datetime_format=dict(required=False, type='str',
                                 default='%Y-%m-%d %H:%M:%S',
                                 aliases=['dt_format']),
        )
        self.resource_group = None
        self.storage_account_name = None
        self.container = None
        self.container_client = None
        self.name_starts_with = None
        self.results = dict(
            changed=False,
            container=dict(),
            blobs=list(),
        )
        self.valide_container_name = re.compile(
            "^[a-z0-9]([a-z0-9]|-(?!-)){1,61}[a-z0-9]$")
        self.datetime_format = None

        super(AzureBlobContainerList, self).__init__(derived_arg_spec=self.module_arg_spec,
                                                     supports_check_mode=True,
                                                     supports_tags=False)

    def exec_module(self, **kwargs):

        for key in list(self.module_arg_spec.keys()):
            setattr(self, key, kwargs[key])

        if not self.valide_container_name.match(self.container):
            self.fail(
                "Container name {0} is not a valid string".format(
                    self.container)
            )

        self.results['check_mode'] = self.check_mode

        self.results["container"] = self.container

        self.blob_service_client = self.get_blob_service_client(
            self.resource_group, self.storage_account_name)

        self.container_client = self.blob_service_client.get_container_client(
            container=self.container)

        try:
            container_props = self.container_client.get_container_properties()

        except ResourceNotFoundError:
            self.fail("Container {0} not found".format(self.container))

        self.results["container"] = dict(
            name=container_props["name"],
            tags=container_props["metadata"],
            last_modified=container_props["last_modified"].strftime(
                self.datetime_format),
        )

        blob_list = self.container_client.list_blobs(
            name_starts_with=self.name_starts_with, include="metadata")
        for blob in blob_list:
            blob_result = dict(
                name=blob["name"],
                tags=blob["metadata"],
                last_modified=blob["last_modified"].strftime(
                    self.datetime_format),
                type=blob["blob_type"],
                content_length=blob["size"],
                content_settings=dict(
                    content_type=blob["content_settings"]["content_type"],
                    content_encoding=blob["content_settings"]["content_encoding"],
                    content_language=blob["content_settings"]["content_language"],
                    content_disposition=blob["content_settings"]["content_disposition"],
                    cache_control=blob["content_settings"]["cache_control"],
                    content_md5=blob["content_settings"]["content_md5"].hex(
                    ) if blob["content_settings"]["content_md5"] else None,
                )
            )

            self.results["blobs"].append(blob_result)

        return self.results


def main():
    AzureBlobContainerList()


if __name__ == '__main__':
    main()
