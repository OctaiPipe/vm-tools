"""Delete dev VMs that have expired. Runs every night."""
from datetime import datetime, timezone

import boto3

ec2 = boto3.client("ec2", region_name="eu-west-2")


def expired(instance):
    tags = {t["Key"]: t["Value"] for t in instance.get("Tags", [])}
    expires = tags.get("ExpiresAt", "1970-01-01T00:00:00Z")
    return datetime.fromisoformat(expires.replace("Z", "+00:00")) < datetime.now(timezone.utc)


def main():
    found = ec2.describe_instances(
        Filters=[
            {"Name": "tag:Name", "Values": ["dev-*"]},
            {"Name": "instance-state-name", "Values": ["running", "stopped"]},
        ]
    )
    ids = [
        i["InstanceId"]
        for r in found["Reservations"]
        for i in r["Instances"]
        if expired(i)
    ]
    if ids:
        ec2.terminate_instances(InstanceIds=ids)
    print(f"Deleted {len(ids)} VMs: {ids}")


if __name__ == "__main__":
    main()
