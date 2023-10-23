.. _pytoccaz.azure.az_blobcontainer_list_module:


************************************
pytoccaz.azure.az_blobcontainer_list
************************************

**List Azure blobs module**


Version added: 1.0.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Lists the blobs under a specified azure storage container.




Parameters
----------

.. raw:: html

    <table  border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Parameter</th>
            <th>Choices/<font color="blue">Defaults</font></th>
            <th width="100%">Comments</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>container</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of a blob container within the storage account.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: container_name</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>name_starts_with</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Filters the results to return only blobs whose names begin with the specified prefix.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: start_with</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>resource_group</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the resource group to use.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: resource_group_name</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>storage_account_name</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                         / <span style="color: red">required</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Name of the storage account to use.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: account_name, storage_account</div>
                </td>
            </tr>
    </table>
    <br/>




Examples
--------

.. code-block:: yaml

    # List blobs under a container
    - name: List blobs under mycontainer
      az_blobcontainer_list:
        resource_group: myresourcegroup
        account_name: myaccountname
        container: mycontainer



Return Values
-------------
Common return values are documented `here <https://docs.ansible.com/ansible/latest/reference_appendices/common_return_values.html#common-return-values>`_, the following are the fields unique to this module:

.. raw:: html

    <table border=0 cellpadding=0 class="documentation-table">
        <tr>
            <th colspan="1">Key</th>
            <th>Returned</th>
            <th width="100%">Description</th>
        </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>blobs</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">list of dict</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>List of blobs.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;content_length&#x27;: 136532, &#x27;content_settings&#x27;: {&#x27;cache_control&#x27;: None, &#x27;content_disposition&#x27;: None, &#x27;content_encoding&#x27;: None, &#x27;content_language&#x27;: None, &#x27;content_md5&#x27;: None, &#x27;content_type&#x27;: &#x27;application/image&#x27;}, &#x27;last_modified&#x27;: &#x27;09-Mar-2016 22:08:25 +0000&#x27;, &#x27;name&#x27;: &#x27;foo.png&#x27;, &#x27;tags&#x27;: {}, &#x27;type&#x27;: &#x27;BlockBlob&#x27;}]</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="return-"></div>
                    <b>container</b>
                    <a class="ansibleOptionLink" href="#return-" title="Permalink to this return value"></a>
                    <div style="font-size: small">
                      <span style="color: purple">dictionary</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>Facts about the current state of the selected container.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;last_modified&#x27;: &#x27;2016-03-09 19:28:26 +0000&#x27;, &#x27;name&#x27;: &#x27;foo&#x27;, &#x27;tags&#x27;: {}}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Olivier Bernard
