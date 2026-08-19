# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-19T22:37:48Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 122767 | 1312 | 361 | 89 | 1 | 0 |
| Current month | 2399803 | 7725 | 1292 | 277 | 4 | 0 |
| Cumulative | 4258403 | 24363 | 2211 | 1262 | 49 | 0 |

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
| Medium risk | 90 |
| Feed matches | 90 |
| DROP matches | 89 |
| Tor matches | 1 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `91.92.40.202` | 7526 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `45.156.87.13` | 7351 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `45.153.34.112` | 5009 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `92.118.39.77` | 2191 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `213.209.159.115` | 1194 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS208137` | `Aneta Kovarova` | `True` | `False` | `False` |
| `77.90.185.21` | 1035 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `80.94.95.211` | 883 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS204428` | `` | `True` | `False` | `False` |
| `2.57.122.209` | 619 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `93.123.109.228` | 396 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `195.178.110.137` | 363 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `91.92.40.202` | 7526 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `45.156.87.13` | 7351 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `45.153.34.112` | 5009 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `92.118.39.77` | 2191 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `213.209.159.115` | 1194 | 55 | `AS208137` | `Aneta Kovarova` | `spamhaus_drop` |
| `77.90.185.21` | 1035 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `80.94.95.211` | 883 | 55 | `AS204428` | `` | `spamhaus_drop` |
| `2.57.122.209` | 619 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `93.123.109.228` | 396 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `195.178.110.137` | 363 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 35491 | 11 | 55 | 7 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 3459 | 10 | 55 | 10 | 0 | `False` |
| `AS215925` | `Administration` | 1493 | 15 | 55 | 1 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 1278 | 4 | 55 | 4 | 0 | `False` |
| `AS213790` | `` | 1110 | 3 | 55 | 3 | 0 | `False` |
| `AS204428` | `` | 939 | 4 | 55 | 4 | 0 | `False` |
| `AS48090` | `AD-Tech` | 843 | 7 | 55 | 7 | 0 | `False` |
| `AS135377` | `` | 731 | 12 | 55 | 1 | 0 | `False` |
| `AS51396` | `` | 474 | 12 | 55 | 12 | 0 | `False` |
| `AS213388` | `` | 343 | 6 | 55 | 6 | 0 | `False` |

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
