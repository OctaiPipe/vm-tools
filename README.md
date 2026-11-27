# vm-tools

Throwaway VMs for engineers.

## Getting a VM

1. Go to **Actions**, choose **Provision VM**, and press **Run workflow**.
2. Give it a name, say whether you need a GPU, and say how many hours you
   need it for. The VM is named `dev-` followed by the name you gave.
3. The VM approves itself on the VPN.
4. Connect to it over the VPN, or by SSH to its public address.

VMs are deleted automatically once their hours are up.

## Layout

- `.github/workflows/provision-vm.yml`: starts a VM.
- `.github/workflows/teardown.yml`: runs every night and deletes expired VMs.
- `scripts/teardown.py`: the clean-up script.
- `iam/provisioner-policy.json`: what the workflows may do in AWS.
- `iam/provisioner-trust.json`: who may use those permissions.
