.. _pytoccaz.azure.az_blobcontainer_list_module:


************************************
pytoccaz.azure.az_blobcontainer_list
************************************

**List Azure blobs module**


Version added: 1.1.0

.. contents::
   :local:
   :depth: 1


Synopsis
--------
- Lists the blobs under a specified azure storage container.



Requirements
------------
The below requirements are needed on the host that executes this module.

- python >= 2.7
- The host that executes this module must have the azure.azcollection collection installed via galaxy
- All python packages listed in collection's requirements-azure.txt must be installed via pip on the host that executes modules from azure.azcollection
- Full installation instructions may be found https://galaxy.ansible.com/azure/azcollection


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
                    <b>ad_user</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Active Directory username. Use when authenticating with an Active Directory user rather than service principal.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>adfs_authority_url</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Azure AD authority url. Use when authenticating with Username/password, and has your own ADFS authority.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>api_profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"latest"</div>
                </td>
                <td>
                        <div>Selects an API profile to use when communicating with Azure services. Default value of <code>latest</code> is appropriate for public clouds; future values will allow use with Azure Stack.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>auth_source</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li><div style="color: blue"><b>auto</b>&nbsp;&larr;</div></li>
                                    <li>cli</li>
                                    <li>credential_file</li>
                                    <li>env</li>
                                    <li>msi</li>
                        </ul>
                </td>
                <td>
                        <div>Controls the source of the credentials to use for authentication.</div>
                        <div>Can also be set via the <code>ANSIBLE_AZURE_AUTH_SOURCE</code> environment variable.</div>
                        <div>When set to <code>auto</code> (the default) the precedence is module parameters -&gt; <code>env</code> -&gt; <code>credential_file</code> -&gt; <code>cli</code>.</div>
                        <div>When set to <code>env</code>, the credentials will be read from the environment variables</div>
                        <div>When set to <code>credential_file</code>, it will read the profile from <code>~/.azure/credentials</code>.</div>
                        <div>When set to <code>cli</code>, the credentials will be sources from the Azure CLI profile. <code>subscription_id</code> or the environment variable <code>AZURE_SUBSCRIPTION_ID</code> can be used to identify the subscription ID if more than one is present otherwise the default az cli subscription is used.</div>
                        <div>When set to <code>msi</code>, the host machine must be an azure resource with an enabled MSI extension. <code>subscription_id</code> or the environment variable <code>AZURE_SUBSCRIPTION_ID</code> can be used to identify the subscription ID if the resource is granted access to more than one subscription, otherwise the first subscription is chosen.</div>
                        <div>The <code>msi</code> was added in Ansible 2.6.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cert_validation_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <ul style="margin: 0; padding: 0"><b>Choices:</b>
                                    <li>ignore</li>
                                    <li>validate</li>
                        </ul>
                </td>
                <td>
                        <div>Controls the certificate validation behavior for Azure endpoints. By default, all modules will validate the server certificate, but when an HTTPS proxy is in use, or against Azure Stack, it may be necessary to disable this behavior by passing <code>ignore</code>. Can also be set via credential file profile or the <code>AZURE_CERT_VALIDATION</code> environment variable.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>client_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Azure client ID. Use when authenticating with a Service Principal.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>cloud_environment</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"AzureCloud"</div>
                </td>
                <td>
                        <div>For cloud environments other than the US public cloud, the environment name (as defined by Azure Python SDK, eg, <code>AzureChinaCloud</code>, <code>AzureUSGovernment</code>), or a metadata discovery endpoint URL (required for Azure Stack). Can also be set via credential file profile or the <code>AZURE_CLOUD_ENVIRONMENT</code> environment variable.</div>
                </td>
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
                    <b>datetime_format</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">-</span>
                    </div>
                </td>
                <td>
                        <b>Default:</b><br/><div style="color: blue">"%Y-%m-%d %H:%M:%S"</div>
                </td>
                <td>
                        <div>Rendering format for last_modified container and blobs date.</div>
                        <div style="font-size: small; color: darkgreen"><br/>aliases: start_with</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_mode</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Parent argument.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>log_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Parent argument.</div>
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
                    <b>password</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Active Directory user password. Use when authenticating with an Active Directory user rather than service principal.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>profile</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Security profile found in ~/.azure/credentials file.</div>
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
                    <b>secret</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Azure client secret. Use when authenticating with a Service Principal.</div>
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
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>subscription_id</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Your Azure subscription Id.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>tenant</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Azure tenant ID. Use when authenticating with a Service Principal.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>thumbprint</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">string</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>The thumbprint of the private key specified in <em>x509_certificate_path</em>.</div>
                        <div>Use when authenticating with a Service Principal.</div>
                        <div>Required if <em>x509_certificate_path</em> is defined.</div>
                </td>
            </tr>
            <tr>
                <td colspan="1">
                    <div class="ansibleOptionAnchor" id="parameter-"></div>
                    <b>x509_certificate_path</b>
                    <a class="ansibleOptionLink" href="#parameter-" title="Permalink to this option"></a>
                    <div style="font-size: small">
                        <span style="color: purple">path</span>
                    </div>
                </td>
                <td>
                </td>
                <td>
                        <div>Path to the X509 certificate used to create the service principal in PEM format.</div>
                        <div>The certificate must be appended to the private key.</div>
                        <div>Use when authenticating with a Service Principal.</div>
                </td>
            </tr>
    </table>
    <br/>


Notes
-----

.. note::
   - For authentication with Azure you can pass parameters, set environment variables, use a profile stored in ~/.azure/credentials, or log in before you run your tasks or playbook with ``az login``.
   - Authentication is also possible using a service principal or Active Directory user.
   - To authenticate via service principal, pass subscription_id, client_id, secret and tenant or set environment variables AZURE_SUBSCRIPTION_ID, AZURE_CLIENT_ID, AZURE_SECRET and AZURE_TENANT.
   - To authenticate via Active Directory user, pass ad_user and password, or set AZURE_AD_USER and AZURE_PASSWORD in the environment.
   - Alternatively, credentials can be stored in ~/.azure/credentials. This is an ini file containing a [default] section and the following keys: subscription_id, client_id, secret and tenant or subscription_id, ad_user and password. It is also possible to add additional profiles. Specify the profile by passing profile or setting AZURE_PROFILE in the environment.


See Also
--------

.. seealso::

   `Sign in with Azure CLI <https://docs.microsoft.com/en-us/cli/azure/authenticate-azure-cli?view=azure-cli-latest>`_
       How to authenticate using the ``az login`` command.


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
                      <span style="color: purple">list</span>
                    </div>
                </td>
                <td>always</td>
                <td>
                            <div>List of blobs.</div>
                    <br/>
                        <div style="font-size: smaller"><b>Sample:</b></div>
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">[{&#x27;content_length&#x27;: 136532, &#x27;content_settings&#x27;: {&#x27;cache_control&#x27;: None, &#x27;content_disposition&#x27;: None, &#x27;content_encoding&#x27;: None, &#x27;content_language&#x27;: None, &#x27;content_md5&#x27;: None, &#x27;content_type&#x27;: &#x27;application/image&#x27;}, &#x27;last_modified&#x27;: &#x27;09-Mar-2016 22:08:25&#x27;, &#x27;name&#x27;: &#x27;foo.png&#x27;, &#x27;tags&#x27;: {}, &#x27;type&#x27;: &#x27;BlockBlob&#x27;}]</div>
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
                        <div style="font-size: smaller; color: blue; word-wrap: break-word; word-break: break-all;">{&#x27;last_modified&#x27;: &#x27;2016-03-09 19:28:26&#x27;, &#x27;name&#x27;: &#x27;foo&#x27;, &#x27;tags&#x27;: {}}</div>
                </td>
            </tr>
    </table>
    <br/><br/>


Status
------


Authors
~~~~~~~

- Olivier Bernard (@pytoccaz)
