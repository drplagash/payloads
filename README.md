# Payload Analysis

Defensive payload analysis, decoded samples, lab notes and detection context.

## Purpose

This repository contains defensive analysis of suspicious payloads observed in labs, honeypots, CTFs and controlled environments.

The goal is to document behavior, decoding steps, indicators, detection logic and defensive lessons.

## Structure

```text
payload-analysis/
├── templates/
├── tpot/
├── web/
├── malware-like/
├── encoded/
├── yara/
├── sigma/
├── suricata/
├── scripts/
├── reports/
└── sanitized-samples/

## Templates

Available templates:

- `templates/payload_analysis_full_template.md`  
  Full template for defensive payload analysis, decoding, IOC extraction, detection logic and mitigation notes.

Use this template when documenting payloads under:

```text
payload-analysis/tpot/
payload-analysis/web/
payload-analysis/encoded/
payload-analysis/malware-like/
payload-analysis/reports/
