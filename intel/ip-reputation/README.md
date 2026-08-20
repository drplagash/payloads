# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-20T22:37:49Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 8736 | 92 | 61 | 11 | 0 | 0 |
| Current month | 2408539 | 7776 | 1303 | 279 | 4 | 0 |
| Cumulative | 4267139 | 24409 | 2219 | 1264 | 49 | 0 |

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
| Medium risk | 11 |
| Feed matches | 11 |
| DROP matches | 11 |
| Tor matches | 0 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `91.92.40.44` | 2825 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `85.11.167.7` | 28 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `64.89.163.89` | 16 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS401626` | `` | `True` | `False` | `False` |
| `64.89.160.135` | 10 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS205759` | `Administration` | `True` | `False` | `False` |
| `45.142.193.161` | 7 | 50 | `medium` | `repeated_attacks_ge_5;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |
| `45.148.10.230` | 7 | 50 | `medium` | `repeated_attacks_ge_5;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `79.124.62.126` | 7 | 50 | `medium` | `repeated_attacks_ge_5;spamhaus_drop_match` | `AS207812` | `MNT-LIR-BG` | `True` | `False` | `False` |
| `79.124.62.134` | 7 | 50 | `medium` | `repeated_attacks_ge_5;spamhaus_drop_match` | `AS207812` | `MNT-LIR-BG` | `True` | `False` | `False` |
| `94.154.43.24` | 7 | 50 | `medium` | `repeated_attacks_ge_5;spamhaus_drop_match` | `AS219502` | `Storm Industries LLC` | `True` | `False` | `False` |
| `45.135.193.194` | 6 | 50 | `medium` | `repeated_attacks_ge_5;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `91.92.40.44` | 2825 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `85.11.167.7` | 28 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `64.89.163.89` | 16 | 55 | `AS401626` | `` | `spamhaus_drop` |
| `64.89.160.135` | 10 | 55 | `AS205759` | `Administration` | `spamhaus_drop` |
| `45.142.193.161` | 7 | 50 | `AS213388` | `` | `spamhaus_drop` |
| `45.148.10.230` | 7 | 50 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `79.124.62.126` | 7 | 50 | `AS207812` | `MNT-LIR-BG` | `spamhaus_drop` |
| `79.124.62.134` | 7 | 50 | `AS207812` | `MNT-LIR-BG` | `spamhaus_drop` |
| `94.154.43.24` | 7 | 50 | `AS219502` | `Storm Industries LLC` | `spamhaus_drop` |
| `45.135.193.194` | 6 | 50 | `AS51396` | `` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 5384 | 4 | 55 | 2 | 0 | `False` |
| `AS401626` | `` | 16 | 1 | 55 | 1 | 0 | `False` |
| `AS205759` | `Administration` | 10 | 1 | 55 | 1 | 0 | `False` |
| `AS207812` | `MNT-LIR-BG` | 14 | 2 | 50 | 2 | 0 | `False` |
| `AS213388` | `` | 7 | 1 | 50 | 1 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 7 | 1 | 50 | 1 | 0 | `False` |
| `AS48090` | `AD-Tech` | 7 | 1 | 50 | 1 | 0 | `False` |
| `AS213790` | `` | 6 | 1 | 50 | 1 | 0 | `False` |
| `AS51396` | `` | 6 | 1 | 50 | 1 | 0 | `False` |
| `AS31898` | `Oracle Corporation` | 457 | 1 | 25 | 0 | 0 | `False` |

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
