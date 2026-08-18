# 0efc1c23e770b1317e0ffa4b44560c907f6f0526047e912e65907636d21f13f0

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `0efc1c23e770b1317e0ffa4b44560c907f6f0526047e912e65907636d21f13f0` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
cd /tmp || cd /var/ || cd /var/run || cd /mnt || cd /root || cd /;/bin/busybox echo -ne '\x45\x4c\x46'
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
