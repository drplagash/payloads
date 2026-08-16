# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-16T06:36:01Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 535020 | 1746 | 462 | 87 | 0 | 0 |
| Current month | 1354879 | 4818 | 950 | 176 | 0 | 0 |
| Cumulative | 3213479 | 22263 | 1970 | 1215 | 46 | 0 |

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
| Medium risk | 87 |
| Feed matches | 87 |
| DROP matches | 87 |
| Tor matches | 0 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `45.153.34.149` | 8365 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `45.156.87.253` | 6695 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `77.90.185.30` | 4673 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `92.118.39.77` | 2602 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `195.178.110.26` | 1407 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `77.90.185.21` | 1141 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `45.148.10.183` | 956 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `80.94.95.211` | 883 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS204428` | `` | `True` | `False` | `False` |
| `91.92.40.24` | 857 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `193.32.162.84` | 751 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `45.153.34.149` | 8365 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `45.156.87.253` | 6695 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `77.90.185.30` | 4673 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `92.118.39.77` | 2602 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `195.178.110.26` | 1407 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `77.90.185.21` | 1141 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `45.148.10.183` | 956 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `80.94.95.211` | 883 | 55 | `AS204428` | `` | `spamhaus_drop` |
| `91.92.40.24` | 857 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `193.32.162.84` | 751 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 17969 | 14 | 55 | 12 | 0 | `False` |
| `AS213790` | `` | 5897 | 4 | 55 | 4 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 4629 | 10 | 55 | 8 | 0 | `False` |
| `AS48090` | `AD-Tech` | 4040 | 11 | 55 | 11 | 0 | `False` |
| `AS215925` | `Administration` | 2216 | 18 | 55 | 1 | 0 | `False` |
| `AS204428` | `` | 928 | 3 | 55 | 3 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 807 | 12 | 55 | 12 | 0 | `False` |
| `AS213388` | `` | 738 | 1 | 55 | 1 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 714 | 3 | 55 | 3 | 0 | `False` |
| `AS202412` | `` | 698 | 4 | 55 | 4 | 0 | `False` |

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
