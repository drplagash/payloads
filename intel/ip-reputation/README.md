# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-18T06:36:06Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 324066 | 1095 | 316 | 85 | 3 | 0 |
| Current month | 2221971 | 6641 | 1168 | 248 | 3 | 0 |
| Cumulative | 4080571 | 23586 | 2125 | 1248 | 49 | 0 |

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
| Medium risk | 88 |
| Feed matches | 88 |
| DROP matches | 85 |
| Tor matches | 3 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `91.92.40.153` | 7935 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `213.209.159.115` | 1199 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS208137` | `Aneta Kovarova` | `True` | `False` | `False` |
| `77.90.185.21` | 1054 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `80.94.92.179` | 725 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `94.154.43.210` | 542 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS219502` | `Storm Industries LLC` | `True` | `False` | `False` |
| `195.178.110.217` | 514 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `80.94.92.55` | 424 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `195.178.110.137` | 263 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `93.123.109.228` | 259 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `45.142.193.164` | 205 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `91.92.40.153` | 7935 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `213.209.159.115` | 1199 | 55 | `AS208137` | `Aneta Kovarova` | `spamhaus_drop` |
| `77.90.185.21` | 1054 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `80.94.92.179` | 725 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `94.154.43.210` | 542 | 55 | `AS219502` | `Storm Industries LLC` | `spamhaus_drop` |
| `195.178.110.217` | 514 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `80.94.92.55` | 424 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `195.178.110.137` | 263 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `93.123.109.228` | 259 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `45.142.193.164` | 205 | 55 | `AS213388` | `` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 24147 | 10 | 55 | 6 | 0 | `False` |
| `AS48090` | `AD-Tech` | 1539 | 10 | 55 | 10 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 1230 | 5 | 55 | 5 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 1220 | 3 | 55 | 3 | 0 | `False` |
| `AS213790` | `` | 1107 | 3 | 55 | 3 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 672 | 12 | 55 | 12 | 0 | `False` |
| `AS213388` | `` | 380 | 6 | 55 | 6 | 0 | `False` |
| `AS51396` | `` | 256 | 7 | 55 | 7 | 0 | `False` |
| `AS401626` | `` | 176 | 9 | 55 | 9 | 0 | `False` |
| `AS135377` | `` | 100 | 5 | 55 | 1 | 0 | `False` |

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
