# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-15T18:58:48Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 18 | 16 | 13 | 4 | 0 | 0 |
| Current month | 18 | 16 | 13 | 4 | 0 | 0 |
| Cumulative | 18 | 16 | 13 | 4 | 0 | 0 |

## Download lists

| Dataset | CSV | JSONL/JSON | ZIP bundle |
|---|---|---|---|
| Latest 24h all attacker IPs | [CSV](downloads/latest-24h-attacker_ips.csv) | [JSONL](downloads/latest-24h-attacker_ips.jsonl) | [ZIP](downloads/latest-24h-bundle.zip) |
| Latest 24h medium risk | [CSV](downloads/latest-24h-medium-risk.csv) | [JSONL](downloads/latest-24h-medium-risk.jsonl) | [ZIP](downloads/latest-24h-bundle.zip) |
| Latest 24h DROP matches | [CSV](downloads/latest-24h-drop-matches.csv) | [JSONL](downloads/latest-24h-drop-matches.jsonl) | [ZIP](downloads/latest-24h-bundle.zip) |
| Latest 24h Tor matches | [CSV](downloads/latest-24h-tor-matches.csv) | [JSONL](downloads/latest-24h-tor-matches.jsonl) | [ZIP](downloads/latest-24h-bundle.zip) |
| Latest 24h ASN ranking | [CSV](downloads/latest-24h-asn_ranking.csv) | [JSON](downloads/latest-24h-asn_ranking.json) | [ZIP](downloads/latest-24h-bundle.zip) |
| Current month bundle | [CSV](downloads/monthly-current-attacker_ips.csv) | [JSONL](downloads/monthly-current-attacker_ips.jsonl) | [ZIP](downloads/monthly-current-bundle.zip) |
| Cumulative bundle | [CSV](downloads/cumulative-attacker_ips.csv) | [JSONL](downloads/cumulative-attacker_ips.jsonl) | [ZIP](downloads/cumulative-bundle.zip) |

## Latest 24h risk overview

| Metric | Count |
|---|---:|
| High risk | 0 |
| Medium risk | 4 |
| Feed matches | 4 |
| DROP matches | 4 |
| Tor matches | 0 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `176.65.148.93` | 2 | 40 | `medium` | `repeated_attacks_ge_2;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |
| `94.154.43.230` | 2 | 40 | `medium` | `repeated_attacks_ge_2;spamhaus_drop_match` | `AS219502` | `Storm Industries LLC` | `True` | `False` | `False` |
| `91.92.40.18` | 1 | 30 | `medium` | `spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `94.154.43.158` | 1 | 30 | `medium` | `spamhaus_drop_match` | `AS219502` | `Storm Industries LLC` | `True` | `False` | `False` |
| `102.208.240.251` | 1 | 0 | `low` | `` | `AS329440` | `Tianhoun Lossi` | `False` | `False` | `False` |
| `103.63.101.24` | 1 | 0 | `low` | `` | `AS150273` | `Johani Fauzi` | `False` | `False` | `False` |
| `167.71.243.84` | 1 | 0 | `low` | `` | `AS14061` | `DigitalOcean, LLC` | `False` | `False` | `False` |
| `169.239.130.20` | 1 | 0 | `low` | `` | `AS49870` | `AS49870 B.V.` | `False` | `False` | `False` |
| `186.3.151.116` | 1 | 0 | `low` | `` | `AS27947` | `Telconet S.A` | `False` | `False` | `False` |
| `198.98.53.110` | 1 | 0 | `low` | `` | `AS53667` | `FranTech Solutions` | `False` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `176.65.148.93` | 2 | 40 | `AS51396` | `` | `spamhaus_drop` |
| `94.154.43.230` | 2 | 40 | `AS219502` | `Storm Industries LLC` | `spamhaus_drop` |
| `91.92.40.18` | 1 | 30 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `94.154.43.158` | 1 | 30 | `AS219502` | `Storm Industries LLC` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS219502` | `Storm Industries LLC` | 3 | 2 | 40 | 2 | 0 | `False` |
| `AS51396` | `` | 2 | 1 | 40 | 1 | 0 | `False` |
| `AS197170` | `TechTies Inc.` | 2 | 2 | 30 | 1 | 0 | `False` |
| `AS45102` | `security trouble` | 2 | 2 | 0 | 0 | 0 | `False` |
| `AS14061` | `DigitalOcean, LLC` | 1 | 1 | 0 | 0 | 0 | `False` |
| `AS150273` | `Johani Fauzi` | 1 | 1 | 0 | 0 | 0 | `False` |
| `AS205463` | `ALPMEDYA-MNT` | 1 | 1 | 0 | 0 | 0 | `False` |
| `AS26042` | `FiberState, LLC` | 1 | 1 | 0 | 0 | 0 | `False` |
| `AS27947` | `Telconet S.A` | 1 | 1 | 0 | 0 | 0 | `False` |
| `AS30036` | `Mediacom Communications Corp` | 1 | 1 | 0 | 0 | 0 | `False` |

## Machine-readable views

- [Latest 24h](latest-24h/)
- [Current month](monthly/2026-08/)
- [Cumulative](cumulative/)

## Policy

- Passive telemetry only.
- External feeds are local reference data only.
- This repository publishes matches against Oraculo-observed IPs, not full third-party lists.
- ASN/BPH labels are operational context, not legal attribution.
- BPH labels require local curation in `/etc/oraculo/bph-asn.list`.
