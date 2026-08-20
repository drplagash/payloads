# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-20T14:37:40Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 62991 | 535 | 212 | 54 | 1 | 0 |
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
| Medium risk | 55 |
| Feed matches | 55 |
| DROP matches | 54 |
| Tor matches | 1 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `91.92.40.44` | 2825 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `92.118.39.77` | 1174 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `77.90.185.21` | 497 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `213.209.159.115` | 379 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS208137` | `Aneta Kovarova` | `True` | `False` | `False` |
| `92.118.39.49` | 279 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `193.32.162.27` | 228 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `195.178.110.137` | 123 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `45.135.193.159` | 59 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |
| `176.120.22.123` | 49 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS198953` | `lir-ru-proton66-1-MNT` | `True` | `False` | `False` |
| `45.142.193.145` | 45 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `91.92.40.44` | 2825 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `92.118.39.77` | 1174 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `77.90.185.21` | 497 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `213.209.159.115` | 379 | 55 | `AS208137` | `Aneta Kovarova` | `spamhaus_drop` |
| `92.118.39.49` | 279 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `193.32.162.27` | 228 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `195.178.110.137` | 123 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `45.135.193.159` | 59 | 55 | `AS51396` | `` | `spamhaus_drop` |
| `176.120.22.123` | 49 | 55 | `AS198953` | `lir-ru-proton66-1-MNT` | `spamhaus_drop` |
| `45.142.193.145` | 45 | 55 | `AS213388` | `` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 20830 | 10 | 55 | 5 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 1718 | 5 | 55 | 5 | 0 | `False` |
| `AS213790` | `` | 527 | 3 | 55 | 3 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 421 | 4 | 55 | 4 | 0 | `False` |
| `AS51396` | `` | 181 | 9 | 55 | 9 | 0 | `False` |
| `AS48090` | `AD-Tech` | 152 | 4 | 55 | 4 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 136 | 7 | 55 | 7 | 0 | `False` |
| `AS213388` | `` | 121 | 5 | 55 | 5 | 0 | `False` |
| `AS198953` | `lir-ru-proton66-1-MNT` | 49 | 1 | 55 | 1 | 0 | `False` |
| `AS207812` | `MNT-LIR-BG` | 38 | 3 | 55 | 3 | 0 | `False` |

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
