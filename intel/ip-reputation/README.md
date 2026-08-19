# Oraculo IP Reputation / ASN / BPH Intel

Passive telemetry dashboard generated from Oraculo-observed attacks.

**Last generated UTC:** `2026-08-19T02:37:09Z`

## Quick status

| Window | Sightings | Unique IPs | Unique ASNs | DROP hits | Tor hits | High/Critical |
|---|---:|---:|---:|---:|---:|---:|
| Latest 24h | 64133 | 583 | 193 | 57 | 0 | 0 |
| Current month | 2287580 | 7001 | 1199 | 261 | 3 | 0 |
| Cumulative | 4146180 | 23834 | 2147 | 1252 | 49 | 0 |

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
| Medium risk | 57 |
| Feed matches | 57 |
| DROP matches | 57 |
| Tor matches | 0 |
| ASN-DROP matches | 0 |
| Curated BPH matches | 0 |

## Latest 24h top attacker IPs

| IP | Attacks | Risk | Level | Reasons | ASN | Org | DROP | Tor | BPH |
|---|---:|---:|---|---|---|---|---|---|---|
| `80.94.95.211` | 883 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS204428` | `` | `True` | `False` | `False` |
| `77.90.185.21` | 624 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213790` | `` | `True` | `False` | `False` |
| `195.178.110.137` | 130 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `93.123.109.228` | 100 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS48090` | `AD-Tech` | `True` | `False` | `False` |
| `204.76.203.49` | 58 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |
| `45.142.193.161` | 56 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS213388` | `` | `True` | `False` | `False` |
| `101.36.106.134` | 55 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS135377` | `` | `True` | `False` | `False` |
| `185.242.3.191` | 52 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS401626` | `` | `True` | `False` | `False` |
| `45.135.194.113` | 52 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS51396` | `` | `True` | `False` | `False` |
| `2.57.122.238` | 34 | 55 | `medium` | `repeated_attacks_ge_10;spamhaus_drop_match` | `AS47890` | `UNMANAGED LTD` | `True` | `False` | `False` |

## Latest 24h feed matches

| IP | Attacks | Risk | ASN | Org | Feed hits |
|---|---:|---:|---|---|---|
| `80.94.95.211` | 883 | 55 | `AS204428` | `` | `spamhaus_drop` |
| `77.90.185.21` | 624 | 55 | `AS213790` | `` | `spamhaus_drop` |
| `195.178.110.137` | 130 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `93.123.109.228` | 100 | 55 | `AS48090` | `AD-Tech` | `spamhaus_drop` |
| `204.76.203.49` | 58 | 55 | `AS51396` | `` | `spamhaus_drop` |
| `45.142.193.161` | 56 | 55 | `AS213388` | `` | `spamhaus_drop` |
| `101.36.106.134` | 55 | 55 | `AS135377` | `` | `spamhaus_drop` |
| `185.242.3.191` | 52 | 55 | `AS401626` | `` | `spamhaus_drop` |
| `45.135.194.113` | 52 | 55 | `AS51396` | `` | `spamhaus_drop` |
| `2.57.122.238` | 34 | 55 | `AS47890` | `UNMANAGED LTD` | `spamhaus_drop` |

## Latest 24h ASN ranking

| ASN | Org/name | Attacks | Unique IPs | Max risk | DROP hits | Tor exits | BPH |
|---|---|---:|---:|---:|---:|---:|---|
| `AS204428` | `` | 883 | 1 | 55 | 1 | 0 | `False` |
| `AS213790` | `` | 685 | 5 | 55 | 5 | 0 | `False` |
| `AS135377` | `` | 607 | 9 | 55 | 1 | 0 | `False` |
| `AS48090` | `AD-Tech` | 304 | 7 | 55 | 7 | 0 | `False` |
| `AS51396` | `` | 192 | 7 | 55 | 7 | 0 | `False` |
| `AS213388` | `` | 118 | 4 | 55 | 4 | 0 | `False` |
| `AS47890` | `UNMANAGED LTD` | 93 | 5 | 55 | 5 | 0 | `False` |
| `AS401626` | `` | 72 | 3 | 55 | 3 | 0 | `False` |
| `AS208137` | `Aneta Kovarova` | 52 | 5 | 55 | 5 | 0 | `False` |
| `AS205759` | `Administration` | 50 | 4 | 55 | 4 | 0 | `False` |

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
