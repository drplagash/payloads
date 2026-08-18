<p align="center">
  <img src="assets/payloads.png" alt="Payloads" width="100%">
</p>

# Payloads

Payloads, malware samples, IOCs and analysis collected from controlled honeypot and SOC lab environments.

This repository is part of **Oráculo SOC**. It is not just storage. It is the public evidence layer for a T-Pot based detection and analysis workflow: capture, triage, classify, extract IOCs, document behavior, and turn noisy honeypot telemetry into defensive intelligence.

## What this repository demonstrates

This repository is meant to show practical capabilities, not dump raw folders at people and hope they clap.

It demonstrates:

- T-Pot telemetry review;
- payload and malware triage;
- SHA-based artifact classification;
- IOC extraction;
- command and behavior analysis;
- detection engineering with YARA, Sigma and Suricata style outputs;
- separation of confirmed samples, review material, CTI-only indicators and noise;
- safe handling of captured malware material using inert representations.

## Human-facing areas

| Area | What visitors should look at |
|---|---|
| `showcase/` | Portfolio-style overview of the T-Pot detection and analysis work |
| `case-studies/` | Human-readable examples of analyzed artifacts and triage decisions |
| `payloads/samples/` | Confirmed payload or malware samples with structured evidence |
| `detections/` | Detection engineering material and rule locations |
| `intel/` | CTI context: IPs, URLs, domains, ASNs and related indicators |
| `docs/` | Cleanup status, structure notes and publishing policy |

## Current repository state

```text
Confirmed payload samples:        1
Legacy review entries:        24739
Archived weak/noise entries:  14998
Archived unknown/noise:        4370
Archived false-useful noise:    454
Legacy SHA tree remaining:        0
```

The old `tpot/oraculo/sha256` sprawl was migrated into explicit zones. The main branch now shows the curated, human-readable portfolio. The historical bulk dataset is preserved in the `legacy-bulk-archive` branch for audit and later review.

## Confirmed sample

The first confirmed payload currently promoted into the canonical structure is:

```text
payloads/samples/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/
```

Summary:

```text
Type: ELF32 MIPS payload / malware-like artifact
Size: 448624 bytes
Source: controlled honeypot/lab telemetry
Status: needs_review, quarantined
Evidence: metadata, IOCs, command sightings, raw inert representation, analysis notes
```

## Canonical sample format

Confirmed samples live under:

```text
payloads/samples/<sha256>/
```

A complete sample can include:

```text
README.md
analysis/
evidence/
metadata/
raw/
yara/
```

Raw bytes must remain inert and safe for repository storage. Use controlled representations such as base64 text. Do not publish directly executable live malware.

## Safety model

This repository is for defensive research, malware analysis, SOC workflows and lab-only validation.

Do not execute samples on production systems. Do not run payloads outside an isolated lab. Do not use this material for unauthorized activity.

Captured artifacts are preserved for analysis, detection engineering and incident understanding. They are evidence, not operational tooling.

## Promotion policy

A directory is promoted into `payloads/samples/` only when there is enough evidence to treat it as a real payload or malware sample.

Useful evidence can include:

- inert raw sample material;
- command sightings;
- decoded behavior;
- IOCs;
- analysis notes;
- metadata;
- YARA or other detection logic.

Everything else stays in the historical branch, moves into `intel/`, or gets preserved as archived review material.

## Where the work is visible

Start here:

```text
showcase/
case-studies/
payloads/samples/
detections/
intel/
docs/CLEANUP_STATUS.md
```

Use the historical branch only when the goal is audit, re-triage or forensic review of the old bulk dataset:

```bash
git fetch origin '+refs/heads/*:refs/remotes/origin/*'
git ls-tree -r origin/legacy-bulk-archive | head
```

## Project context

Oráculo SOC is a controlled lab ecosystem for honeypots, CTI, malware triage, IOC enrichment, payload analysis and defensive automation.

This repository is the public-facing payload and malware evidence library for that ecosystem.

## License

MIT License, unless a specific file or directory states otherwise.

## Visible T-Pot findings

The public branch exposes the defensive output of the T-Pot pipeline without dumping the full legacy tree into the root.

- `findings/tpot/`: counts, SHA lists and evidence indexes from legacy T-Pot review.
- `case-studies/tpot-legacy-review/`: curated review cases with command evidence, IOCs, metadata and detection notes.
- `payloads/samples/`: confirmed promoted malware or payload samples.
- `origin/legacy-bulk-archive`: preserved heavy historical tree for audit and recovery.

