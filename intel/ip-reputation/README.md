# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-15T22:35:55Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 625946 | 1805 | 470 | 86 | 0 | 0 |
| Current month | 1257934 | 4429 | 904 | 163 | 0 | 0 |
| Cumulative | 3116534 | 21988 | 1945 | 1209 | 46 | 0 |

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
| Medium risk | 86 |
| Feed matches | 86 |
| DROP matches | 86 |
| Tor matches | 0 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `45.153.34.149` | 8365 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `77.90.185.30` | 5608 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `92.118.39.77` | 2131 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |
| `195.178.110.26` | 1407 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `77.90.185.21` | 1257 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `91.92.40.202` | 1051 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `45.148.10.183` | 956 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `213.209.159.154` | 883 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS208137` | `Aneta Kovarova` | `True` | `False` | `False` |
| `91.92.40.24` | 857 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS197170` | `TechTies Inc.` | `True` | `False` | `False` |
| `45.142.193.164` | 851 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `45.153.34.149` | 8365 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `77.90.185.30` | 5608 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `92.118.39.77` | 2131 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |
| `195.178.110.26` | 1407 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `77.90.185.21` | 1257 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `91.92.40.202` | 1051 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `45.148.10.183` | 956 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `213.209.159.154` | 883 | 55 | `AS208137` | `Aneta Kovarova` | `spamhaus_drop` |
| `91.92.40.24` | 857 | 55 | `AS197170` | `TechTies Inc.` | `spamhaus_drop` |
| `45.142.193.164` | 851 | 55 | `AS213388` | `` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 14936 | 12 | 55 | 9 | 0 | `False` |
| `AS213790` | `` | 6909 | 4 | 55 | 4 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 4482 | 11 | 55 | 9 | 0 | `False` |
| `AS48090` | `AD-Tech` | 3466 | 10 | 55 | 10 | 0 | `False` |
| `AS215925` | `Administration` | 2314 | 18 | 55 | 1 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 1631 | 4 | 55 | 4 | 0 | `False` |
| `AS135377` | `` | 1235 | 17 | 55 | 1 | 0 | `False` |
| `AS202412` | `` | 1035 | 4 | 55 | 4 | 0 | `False` |
| `AS213388` | `` | 858 | 2 | 55 | 2 | 0 | `False` |
| `AS51396` | `` | 306 | 7 | 55 | 7 | 0 | `False` |

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
