# T-Pot Detection Showcase

This is the human-facing overview of the work behind this repository.

The purpose is to show the defensive process used in Oráculo SOC: collect noisy T-Pot telemetry, identify payload-relevant artifacts, separate junk from useful evidence, and document what can be turned into CTI, detections or malware analysis.

## What was done

The legacy payload collection was reviewed and reorganized into a cleaner model:

```text
Confirmed payload samples:        1
Legacy review entries:        24739
Archived weak/noise entries:  14998
Archived unknown/noise:        4370
Archived false-useful noise:    454
Legacy SHA tree remaining:        0
```

This matters because raw honeypot output is mostly noise. The actual skill is not collecting folders. The skill is deciding what is evidence, what is just telemetry, what is CTI-only, and what is safe to publish.

## Detection and analysis capabilities shown

```text
T-Pot telemetry review
payload triage
malware-like artifact classification
IOC extraction
command-sighting review
safe raw artifact handling
repository hygiene for public research
legacy evidence preservation
promotion policy for confirmed samples
```

## Public result

The main branch now shows only the curated public surface:

```text
showcase/
case-studies/
payloads/samples/
detections/
intel/
docs/
```

The bulk historical dataset is preserved in:

```text
legacy-bulk-archive
```

That branch exists for audit and future triage. It is not the portfolio view.

## Highlighted artifact

The currently promoted confirmed sample is:

```text
payloads/samples/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/
```

High-level summary:

```text
Type: ELF32 MIPS payload / malware-like artifact
Size: 448624 bytes
Source: controlled honeypot/lab telemetry
State: needs_review
Safety: quarantined, raw bytes stored in inert representation
Evidence: command sightings, metadata, IOCs, raw representation and analysis notes
```

## Why this is useful

This repository demonstrates the full path from honeypot noise to defensive output:

```text
capture -> triage -> classify -> extract -> document -> detect -> preserve
```

That is the part worth showing. Nobody needs to see thousands of SHA folders on the front page unless they are trying to punish themselves professionally.
