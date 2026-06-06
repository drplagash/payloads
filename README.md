# Payload Analysis

Defensive payload analysis, decoded samples, lab notes and detection context.

## Purpose

This repository contains defensive analysis of suspicious payloads observed in labs, honeypots, CTFs and controlled environments.

The goal is to document behavior, decoding steps, indicators, detection logic, mitigation ideas and defensive lessons.

## Structure

```text
payload-analysis/
├── templates/
├── tpot/
├── web/
├── malware-like/
├── encoded/
├── yara/
├── sigma/
├── suricata/
├── scripts/
├── reports/
└── sanitized-samples/
```

## Categories

- `tpot`: payloads observed in honeypot/lab telemetry.
- `web`: SQLi, XSS, LFI, RFI, command injection and web attack payloads.
- `malware-like`: suspicious payloads analyzed safely without publishing live malware.
- `encoded`: encoded or obfuscated samples.
- `yara`: YARA rules.
- `sigma`: Sigma detection rules.
- `suricata`: IDS/IPS rules.
- `scripts`: helper scripts for decoding and parsing.
- `reports`: Markdown analysis reports.
- `sanitized-samples`: neutralized, redacted or safely represented examples.

## Templates

Available templates:

- `templates/payload_analysis_full_template.md`  
  Full template for defensive payload analysis, decoding, IOC extraction, detection logic and mitigation notes.

Use this template when documenting payloads under:

```text
payload-analysis/tpot/
payload-analysis/web/
payload-analysis/encoded/
payload-analysis/malware-like/
payload-analysis/reports/
```

## Analysis folder format

Each payload analysis can use this structure when needed:

```text
payload-name-or-date/
├── README.md
├── raw-redacted/
├── decoded/
├── iocs/
├── rules/
├── screenshots/
└── notes.md
```

## Analysis sections

Each payload report should include:

```text
# Payload Analysis - Title

## Summary
Brief description of the observed payload.

## Source
Where the payload came from: T-Pot, CTF, web log, lab or controlled source.

## Scope
Defensive analysis only.

## Raw Payload
Sanitized, redacted or neutralized payload content.

## Decoding Steps
Encoding type, transformations and tools used.

## Decoded Content
Decoded or partially decoded payload.

## Behavior
Intent, technique, targeted service and expected behavior.

## Indicators
IPs, domains, URLs, hashes, user agents, filenames or paths.

## Detection
YARA, Sigma, Suricata, log queries or search patterns.

## Mitigation
Controls, blocking options, hardening and monitoring.

## Confidence
Analyst confidence and limitations.

## Conclusion
Final assessment and recommended actions.
```

## Rules

- Defensive and educational use only.
- Authorized labs only.
- No live malware binaries.
- No weaponized payloads.
- No credentials, tokens, dumps or sensitive data.
- No third-party targeting.
- No unsafe samples.
- No private infrastructure details.
- Samples must be sanitized, redacted, neutralized or represented safely.
- Include detection and mitigation context whenever possible.

## Payload handling policy

Do not publish:

- Live malware binaries.
- Real credentials.
- API keys.
- Tokens.
- Session cookies.
- Private keys.
- Dumps.
- Leaked data.
- Personal data.
- Sensitive screenshots.
- Private infrastructure details.
- Payloads ready for direct abuse against third-party systems.

Prefer publishing:

- Hashes.
- Redacted logs.
- Sanitized snippets.
- Decoded explanations.
- Behavioral summaries.
- Detection rules.
- Mitigation guidance.
- Defensive context.

## Recommended commands

### URL decode

```bash
python3 - <<'PY'
from urllib.parse import unquote
payload = '''PASTE_PAYLOAD_HERE'''
print(unquote(payload))
PY
```

### Base64 decode

```bash
echo 'BASE64_HERE' | base64 -d
```

### Hex decode

```bash
echo 'HEX_HERE' | xxd -r -p
```

### Strings

```bash
strings sample.bin
```

### Hashing

```bash
sha256sum sample
```

### Grep search

```bash
grep -R "PATTERN" /path/to/logs/
```

### JSON filtering

```bash
jq 'select(.url | contains("PATTERN"))' events.json
```

## Detection rule locations

Store detection logic in the correct folder:

```text
payload-analysis/yara/
payload-analysis/sigma/
payload-analysis/suricata/
```

Use `reports/` for written analysis and `sanitized-samples/` for safe examples.

## Analysis goals

Each analysis should try to answer:

- What does the payload attempt to do?
- Where was it observed?
- How is it encoded or obfuscated?
- What technique does it suggest?
- What service or component is targeted?
- What indicators can be extracted?
- How could it be detected?
- How could it be mitigated?
- What is the confidence level?
- What limitations exist?

## Publishing checklist

Before publishing a payload analysis:

- [ ] Payload is sanitized.
- [ ] No secrets are included.
- [ ] No credentials are included.
- [ ] No tokens or cookies are included.
- [ ] No live malware is included.
- [ ] No sensitive screenshots are included.
- [ ] Internal infrastructure is redacted if needed.
- [ ] Source is described.
- [ ] Decoding steps are documented.
- [ ] Behavior is explained.
- [ ] IOCs are extracted when available.
- [ ] Detection ideas are included.
- [ ] Mitigation notes are included.
- [ ] Confidence level is stated.

## Disclaimer

This repository is for educational, defensive and authorized analysis only.

Do not use any material from this repository against systems you do not own or do not have explicit permission to test.

Do not publish or execute live malware, weaponized payloads, stolen credentials, dumps, tokens or sensitive data.

**Menos humo, más evidencia.**
