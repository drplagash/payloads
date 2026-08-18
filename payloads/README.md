# Payloads and malware samples

This is the quick human index for confirmed payload and malware material.

## Visible samples

| Sample | Type | Why it matters |
|---|---|---|
| [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`](samples/cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) | ELF32 MIPS payload / malware-like artifact | Captured from controlled honeypot telemetry and promoted with evidence, metadata, IOCs and analysis notes |

## What belongs here

Only confirmed payload or malware samples with enough context to be useful:

- what was captured,
- where it came from,
- why it was promoted,
- what indicators were extracted,
- what behavior was observed,
- what detection value it has.

## What does not belong here

- Raw hash spam.
- Low-context artifacts.
- CTI-only IP lists.
- Generic review folders.
- Noise from the legacy SHA tree.

Those stay in the historical branch, archive areas or the proper `intel/` and `case-studies/` sections.

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

Raw samples must remain inert and safe for repository storage. Do not publish directly executable live malware.
