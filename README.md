<p align="center">
  <img src="assets/payloads.png" alt="Payloads" width="100%">
</p>

# Payloads

Public evidence library for Oraculo SOC payload and malware analysis.

This repository is meant to be readable by a human visitor in less than one minute. The front page points to the work first: confirmed payloads, malware evidence, and campaign case studies. Bulk review material stays out of the way.

## Quick access

| I want to see | Go here | What it shows |
|---|---|---|
| Confirmed payloads and malware samples | [`payloads/samples/`](payloads/samples/) | Promoted artifacts with structured evidence |
| Malware/payload index | [`payloads/README.md`](payloads/README.md) | Short human map of the active sample area |
| Campaign analysis | [`case-studies/`](case-studies/) | Human-readable writeups from T-Pot telemetry |
| Featured campaign | [`T-Pot router downloader campaign`](case-studies/tpot-router-downloader-campaign-91-92-40/) | 517 high-signal downloader artifacts grouped into one analysis |
| Confirmed MIPS sample | [`cad9e90...`](payloads/samples/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) | ELF32 MIPS payload evidence and notes |
| Detection material | [`detections/`](detections/) | Detection engineering area |
| CTI context | [`intel/`](intel/) | IP, URL, ASN and related intelligence |

## What this repository demonstrates

- T-Pot telemetry review.
- Payload and malware triage.
- SHA-based artifact classification.
- IOC extraction.
- Command and behavior analysis.
- Detection engineering with YARA, Sigma and Suricata-style outputs.
- Separation of confirmed samples, review material, CTI-only indicators and noise.
- Safe handling of captured malware material using inert representations.

## Featured T-Pot campaign analysis

- [`T-Pot router downloader campaign`](case-studies/tpot-router-downloader-campaign-91-92-40/)  
  Campaign-level analysis of 517 high-signal downloader payloads abusing HNAP, JNAP, Netgear setup.cgi, ping_test, syscmd.htm, ttcp_ip and weblogin.cgi surfaces.

## Confirmed payload / malware sample

Current promoted sample:

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

## Repository state

```text
Confirmed payload samples:        1
Legacy review entries:        24739
Archived weak/noise entries:  14998
Archived unknown/noise:        4370
Archived false-useful noise:    454
Legacy SHA tree remaining:        0
```

The old SHA sprawl was moved out of the main visitor path. The main branch shows the curated portfolio. The historical bulk dataset remains in `legacy-bulk-archive` for audit and re-triage.

## Safety model

This repository is for defensive research, malware analysis, SOC workflows and lab-only validation.

Do not execute samples on production systems. Do not run payloads outside an isolated lab. Captured artifacts are evidence, not operational tooling.

Raw bytes must remain inert and safe for repository storage, such as base64 text or other controlled representations.

## Project context

Oraculo SOC is a controlled lab ecosystem for honeypots, CTI, malware triage, IOC enrichment, payload analysis and defensive automation.

This repository is the public-facing payload and malware evidence library for that ecosystem.

## License

MIT License, unless a specific file or directory states otherwise.
