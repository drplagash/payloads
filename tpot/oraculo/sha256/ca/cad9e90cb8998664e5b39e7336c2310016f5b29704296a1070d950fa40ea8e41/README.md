# Oraculo SOC Payload Analysis

## Summary

Artifact `82064` was recovered by Oraculo safe-fetch and stored locally in quarantine. This repository entry publishes defensive analysis material only. The raw executable sample is not included.

## Identifiers

| Field | Value |
|---|---|
| Artifact ID | `82064` |
| SHA256 | `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41` |
| SHA1 | `5e848778ec4fbfddc94b5a76e5a56bf2e5173ce3` |
| MD5 | `620c007093f64dfe672252c0bd483f25` |
| Size | `448624` bytes |
| Type | `payload` |
| Magic | `ELF32 big-endian executable/shared object, machine=MIPS, entry=0x400260` |
| Source URL | `hxxp://154[.]90[.]70[.]23/mips` |

## Observed context

| Field | Value |
|---|---|
| First seen | `2026-08-15 15:42:02` |
| Last seen | `2026-08-15 16:08:03` |
| Analysis state | `needs_review` |
| Quarantined | `1` |
| Payload observation | `3632` |
| Novelty | `new_artifact` |

## Defensive artifacts

- `metadata/artifact.json`
- `metadata/observation.json`
- `analysis/iocs.json`
- `analysis/strings.txt`
- `analysis/hexdump_head.txt`
- `analysis/readelf_header.txt`
- `analysis/readelf_segments.txt`
- `yara/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41.yar`

## Safety note

No raw executable malware is published here. Any text excerpts are defanged and non-complete. This entry is intended for defensive analysis, detection engineering, hunting, and incident response.

## Initial assessment

The artifact was recovered from an attacker-referenced URL and is treated as high-risk malware. Current automated handling keeps it quarantined, records hashes and observation metadata, and avoids execution. Any further dynamic analysis must remain inside an isolated malware-analysis environment.
