# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-18T22:37:59Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 109543 | 522 | 188 | 56 | 0 | 0 |
| Current month | 2277004 | 6863 | 1194 | 257 | 3 | 0 |
| Cumulative | 4135604 | 23739 | 2144 | 1250 | 49 | 0 |

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
| Medium risk | 56 |
| Feed matches | 56 |
| DROP matches | 56 |
| Tor matches | 0 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `77.90.185.21` | 616 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `93.123.109.228` | 359 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `195.178.110.228` | 140 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `195.178.110.137` | 130 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `101.36.106.134` | 55 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS135377` | `` | `True` | `False` | `False` |
| `45.135.194.113` | 52 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |
| `176.65.148.146` | 38 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |
| `195.178.110.218` | 38 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `45.148.10.240` | 33 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `45.142.193.18` | 32 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `77.90.185.21` | 616 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `93.123.109.228` | 359 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `195.178.110.228` | 140 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `195.178.110.137` | 130 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `101.36.106.134` | 55 | 55 | `AS135377` | `` | `spamhaus_drop` |
| `45.135.194.113` | 52 | 55 | `AS51396` | `` | `spamhaus_drop` |
| `176.65.148.146` | 38 | 55 | `AS51396` | `` | `spamhaus_drop` |
| `195.178.110.218` | 38 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `45.148.10.240` | 33 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `45.142.193.18` | 32 | 55 | `AS213388` | `` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS197170` | `TechTies Inc.` | 5832 | 5 | 55 | 3 | 0 | `False` |
| `AS48090` | `AD-Tech` | 749 | 9 | 55 | 9 | 0 | `False` |
| `AS213790` | `` | 657 | 4 | 55 | 4 | 0 | `False` |
| `AS135377` | `` | 512 | 7 | 55 | 1 | 0 | `False` |
| `AS51396` | `` | 161 | 6 | 55 | 6 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 88 | 5 | 55 | 5 | 0 | `False` |
| `AS213388` | `` | 86 | 4 | 55 | 4 | 0 | `False` |
| `AS205759` | `Administration` | 57 | 5 | 55 | 5 | 0 | `False` |
| `AS219502` | `Storm Industries LLC` | 47 | 4 | 55 | 4 | 0 | `False` |
| `AS202412` | `` | 38 | 3 | 55 | 3 | 0 | `False` |

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
