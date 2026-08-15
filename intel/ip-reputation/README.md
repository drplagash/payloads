# Oraculo IP Reputation / ASN / BPH Intel

Passive rankings generated from observed honeypot/lab telemetry.

## Views

- `latest-24h/`: rolling 24-hour view, updated every 4 hours.
- `monthly/YYYY-MM/`: current month view, updated every 4 hours.
- `cumulative/`: all-time view, updated every 4 hours.

## Current summaries

| Scope | Sightings | Unique IPs | Unique ASNs | BPH ASNs |
|---|---:|---:|---:|---:|
| `24h` | 18 | 16 | 1 | 0 |
| `month` | 18 | 16 | 1 | 0 |
| `cumulative` | 18 | 16 | 1 | 0 |

## Policy

- Passive telemetry only.
- No active scanning.
- ASN/BPH tags are context, not legal attribution.
- BPH labels require explicit curation in `/etc/oraculo/bph-asn.list`.
