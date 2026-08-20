# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-20T10:37:35Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 81528 | 763 | 274 | 64 | 1 | 0 |
| Current month | 2408539 | 7776 | 1303 | 278 | 4 | 0 |
| Cumulative | 4267139 | 24409 | 2219 | 1263 | 49 | 0 |

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
| Medium risk | 65 |
| Feed matches | 65 |
| DROP matches | 64 |
| Tor matches | 1 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `45.153.34.112` | 5009 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `91.92.40.44` | 2825 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `92.118.39.77` | 1619 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `213.209.159.115` | 594 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS208137` | `Aneta Kovarova` | `True` | `False` | `False` |
| `77.90.185.21` | 497 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `92.118.39.49` | 279 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `195.178.110.137` | 236 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `193.32.162.27` | 228 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `45.142.193.161` | 75 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |
| `45.142.193.145` | 71 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `45.153.34.112` | 5009 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `91.92.40.44` | 2825 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `92.118.39.77` | 1619 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `213.209.159.115` | 594 | 55 | `AS208137` | `Aneta Kovarova` | `spamhaus_drop` |
| `77.90.185.21` | 497 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `92.118.39.49` | 279 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `195.178.110.137` | 236 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `193.32.162.27` | 228 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `45.142.193.161` | 75 | 55 | `AS213388` | `` | `spamhaus_drop` |
| `45.142.193.145` | 71 | 55 | `AS213388` | `` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 25896 | 12 | 55 | 6 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 2184 | 7 | 55 | 7 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 636 | 4 | 55 | 4 | 0 | `False` |
| `AS213790` | `` | 533 | 3 | 55 | 3 | 0 | `False` |
| `AS48090` | `AD-Tech` | 279 | 4 | 55 | 4 | 0 | `False` |
| `AS51396` | `` | 257 | 9 | 55 | 9 | 0 | `False` |
| `AS213388` | `` | 194 | 5 | 55 | 5 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 152 | 8 | 55 | 8 | 0 | `False` |
| `AS207812` | `MNT-LIR-BG` | 52 | 4 | 55 | 4 | 0 | `False` |
| `AS198953` | `lir-ru-proton66-1-MNT` | 49 | 1 | 55 | 1 | 0 | `False` |

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
