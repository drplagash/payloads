# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-17T22:37:16Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 450895 | 1402 | 363 | 95 | 3 | 0 |
| Current month | 2166474 | 6540 | 1159 | 242 | 3 | 0 |
| Cumulative | 4025074 | 23512 | 2117 | 1246 | 47 | 0 |

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
| Medium risk | 98 |
| Feed matches | 98 |
| DROP matches | 95 |
| Tor matches | 3 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `91.92.40.153` | 7935 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `91.92.40.37` | 4324 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `91.92.40.46` | 4272 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `213.209.159.115` | 1790 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS208137` | `Aneta Kovarova` | `True` | `False` | `False` |
| `77.90.185.21` | 1597 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `77.90.185.30` | 1028 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `77.90.185.20` | 772 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `80.94.92.179` | 725 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `94.154.43.210` | 542 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS219502` | `Storm Industries LLC` | `True` | `False` | `False` |
| `195.178.110.217` | 514 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `91.92.40.153` | 7935 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `91.92.40.37` | 4324 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `91.92.40.46` | 4272 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `213.209.159.115` | 1790 | 55 | `AS208137` | `Aneta Kovarova` | `spamhaus_drop` |
| `77.90.185.21` | 1597 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `77.90.185.30` | 1028 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `77.90.185.20` | 772 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `80.94.92.179` | 725 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `94.154.43.210` | 542 | 55 | `AS219502` | `Storm Industries LLC` | `spamhaus_drop` |
| `195.178.110.217` | 514 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 26813 | 16 | 55 | 11 | 0 | `False` |
| `AS213790` | `` | 3490 | 7 | 55 | 7 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 1818 | 3 | 55 | 3 | 0 | `False` |
| `AS215925` | `Administration` | 1514 | 15 | 55 | 2 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 1272 | 8 | 55 | 8 | 0 | `False` |
| `AS48090` | `AD-Tech` | 1214 | 7 | 55 | 7 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 768 | 13 | 55 | 13 | 0 | `False` |
| `AS135377` | `` | 413 | 7 | 55 | 1 | 0 | `False` |
| `AS213388` | `` | 392 | 7 | 55 | 7 | 0 | `False` |
| `AS51396` | `` | 356 | 7 | 55 | 7 | 0 | `False` |

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
