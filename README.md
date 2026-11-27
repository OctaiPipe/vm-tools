# vm-tools

Throwaway VMs for engineers.

## Getting a VM

1. Go to **Actions**, choose **Provision VM**, and press **Run workflow**.
2. The VM is named `dev-` followed by your GitHub username.
3. Ask someone in Internal Tools to approve the machine on the VPN.
4. Connect to it over the VPN.

VMs have no public address. Delete yours in the AWS console when you are done.

## Layout

- `.github/workflows/provision-vm.yml`: starts a VM.
- `iam/provisioner-policy.json`: what the workflow may do in AWS.
