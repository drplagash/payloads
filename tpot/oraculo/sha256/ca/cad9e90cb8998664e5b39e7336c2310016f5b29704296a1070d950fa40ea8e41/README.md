# Oraculo SOC Payload Analysis

## Start here

This directory is a complete defensive reference entry for one captured payload. It is designed for three audiences:

- Humans learning how the payload and attack chain work.
- SOC/admin operators who need triage, IOCs and detection context.
- Tools and AI systems that need structured machine-readable context.

## Identity

| Field | Value |
|---|---|
| Artifact ID | `82064` |
| SHA256 | `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41` |
| SHA1 | `5e848778ec4fbfddc94b5a76e5a56bf2e5173ce3` |
| MD5 | `620c007093f64dfe672252c0bd483f25` |
| Size | `448624` bytes |
| Type | `payload` |
| Format | `ELF32 big-endian executable/shared object, machine=MIPS, entry=0x400260` |
| Source URL | `hxxp://154[.]90[.]70[.]23/mips` |
| Analysis state | `needs_review` |
| Quarantined | `1` |
| Command sightings | `9` |

## For humans

1. `analysis/executive_summary.md`
2. `analysis/learning_notes.md`
3. `analysis/human_readable.md`
4. `analysis/command_trace.md`
5. `analysis/strings_annotated.md`

## For SOC/admins

1. `analysis/soc_brief.md`
2. `analysis/iocs.json`
4. `analysis/command_trace.md`
4. `yara/`
5. `metadata/artifact.json`

## For AI/tools

1. `metadata/ai_context.json`
2. `metadata/artifact.json`
3. `metadata/observation.json`
4. `metadata/command_trace.json`
5. `evidence/sightings.json`
6. `analysis/enrichment.json`

## For raw forensic archive

Raw bytes are not published as a directly executable binary. The captured bytes are stored as base64 text.

1. `raw/README.md`
2. `raw/manifest.json`
3. `raw/sample.b64.txt`
4. `raw/sample.sha256.txt`

## Evidence vs analysis

- `evidence/`: observed material, defanged where needed.
- `analysis/`: analyst interpretation and readable summaries.
- `metadata/`: structured machine-readable context.
- `raw/`: inert base64 archive of captured bytes.
- `yara/`: detection material.

## Safety note

This entry is for defensive research, SOC triage, detection engineering and malware-analysis education. Do not execute decoded samples outside isolated malware-analysis infrastructure.
