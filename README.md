<p align="center">
  <img src="assets/payloads.png" alt="Payloads" width="100%">
</p>

# Payloads

Payloads, malware samples, IOCs and analysis collected from controlled honeypot and SOC lab environments.

This repository is part of **Oráculo SOC**. It preserves evidence from honeypots, controlled experiments and defensive research workflows, then separates actual payloads from noise, review material and plain intelligence.

The goal is simple: keep useful evidence, make it understandable, and avoid turning a malware repository into a landfill with a README.

## What belongs here

| Area | Purpose |
|---|---|
| `payloads/samples/` | Confirmed payloads and malware samples |
| `review/` | Legacy material that still needs analyst review |
| `archive/` | Preserved low-value or noisy legacy material |
| `intel/` | IPs, domains, URLs, ASNs and CTI context |
| `detections/` | YARA, Sigma, Suricata and detection logic |
| `audit/` | Migration logs and triage manifests |
| `docs/` | Policy, structure and cleanup notes |

## Current repository state

```text
Confirmed payload samples:        1
Legacy review entries:        24739
Archived weak/noise entries:  14998
Archived unknown/noise:        4370
Archived false-useful noise:    454
Legacy SHA tree remaining:        0
```

The old `tpot/oraculo/sha256` sprawl was migrated into explicit zones. Confirmed payloads now live in the canonical structure. Review material is preserved but no longer presented as finished analysis.

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

Everything else stays in `review/`, moves to `intel/`, or gets preserved in `archive/`.

## Project context

Oráculo SOC is a controlled lab ecosystem for honeypots, CTI, malware triage, IOC enrichment, payload analysis and defensive automation.

This repository is the public-facing payload and malware evidence library for that ecosystem.

## License

MIT License, unless a specific file or directory states otherwise.
