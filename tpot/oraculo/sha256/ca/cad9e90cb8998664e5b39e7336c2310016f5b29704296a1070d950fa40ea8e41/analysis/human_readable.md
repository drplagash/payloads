# Human-readable Malware Analysis

## Summary

This artifact is a quarantined compiled MIPS payload. The repo entry now includes a human-readable analysis layer instead of only JSON, raw strings and byte dumps.

The original source code is not available because the sample is compiled. What follows is the safest readable representation: grouped strings, indicators, partial disassembly and analyst notes.

## Identity

| Field | Value |
|---|---|
| Artifact ID | `82064` |
| SHA256 | `cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41` |
| SHA1 | `5e848778ec4fbfddc94b5a76e5a56bf2e5173ce3` |
| MD5 | `620c007093f64dfe672252c0bd483f25` |
| Size | `448624` bytes |
| Format | `ELF32 big-endian, machine=MIPS, entry=0x400260` |
| Source URL | `hxxp://154[.]90[.]70[.]23/mips` |
| Analysis state | `needs_review` |
| Quarantined | `1` |

## Most useful human files

- `strings_annotated.md`
- `pseudocode_notes.md`
- `disassembly_entry.txt`
- `operator_notes.md`
- `iocs.json`
- YARA rule under `yara/`

## Network URLs

- No clear URLs found in extracted strings.


## IP addresses

- `Mozilla/5[.]0 (Windows NT 10[.]0; Win64; x64) AppleWebKit/537[.]36 (KHTML, like Gecko) Chrome/120[.]0[.]0[.]0 Safari/537[.]36`
- `Mozilla/5[.]0 (X11; Linux x86_64) AppleWebKit/537[.]36 (KHTML, like Gecko) Chrome/119[.]0[.]0[.]0 Safari/537[.]36`
- `Mozilla/5[.]0 (Windows NT 10[.]0; Win64; x64) AppleWebKit/537[.]36 (KHTML, like Gecko) Chrome/120[.]0[.]0[.]0 Safari/537[.]36 Edg/120[.]0[.]0[.]0`


## Command hints

- `User-Agent: curl/8.0`
- `/system/bin/sh`
- `/apex/com.android.runtime/bin/sh`
- `/vendor/bin/sh`
- `/usr/bin/sh`


## Path hints

- `C/0$Q/0$`
- `4$Q/ $`
- `GET %s HTTP/1.1`
- `Accept: */*`
- `HEAD %s HTTP/1.1`
- `POST %s HTTP/1.1`
- `Content-Type: application/x-www-form-urlencoded`
- `POST /client HTTP/1.1`
- `User-Agent: CitizenFX/1`
- `GET /info.json HTTP/1.1`
- `User-Agent: Mozilla/5.0 (Windows NT 10.0; rv:78.0) Gecko/20100101 Firefox/78.0`
- `Mozilla/5.0 (Windows NT 10.0; Win64; x64; rv:121.0) Gecko/20100101 Firefox/121.0`
- `Mozilla/5.0 (Macintosh; Intel Mac OS X 10_15_7) AppleWebKit/605.1.15 (KHTML, like Gecko) Version/17.0 Safari/605.1.15`
- `POST %s HTTP/1.0`
- `Accept: application/json`
- `Content-Type: application/json`
- `HTTP/1.`
- `/proc/self/comm`
- `%s%s/comm`
- `%s%s/cmdline`
- `%s%s/oom_score_adj`
- `/usr/`
- `/bin/`
- `/sbin/`
- `/system/`
- `%s%s/maps`
- `/proc`
- `/proc/`
- `/lib/`
- `/proc/net/route`
- `/etc/resolv.conf`
- `/system/bin/toybox`
- `/proc/sys/kernel/hostname`
- `/dev/ptmx`
- `/sbin:/system/sbin:/system/bin:/system/xbin:/vendor/bin:/bin:/usr/bin:/usr/local/bin`
- `/usr/bin/bash`
- `/data/local/tmp/sh`
- `/sbin/sh`
- `/system/build.prop`
- `/vendor/build.prop`
- `/product/build.prop`
- `/odm/build.prop`
- `/system/bin/getprop`
- `/vendor/bin/getprop`
- `/bin/getprop`
- `local/tmp`
- `/data/local/tmp`
- `%s/local/tmp`
- `/proc/mounts`
- `%s/%s`
- `/dev/urandom`
- `%)+/5;=CGIOSYaegkmq`
- `/etc/passwd`
- `Input/output error`
- `Remote I/O error`
- `/dev/pts/`
- `/dev/null`
- `/etc/config/resolv.conf`
- `RPC: Program/version mismatch`
- `/etc/hosts`
- `/etc/config/hosts`


## Runtime/process hints

- `Connection: keep-alive`
- `execcmdshere`
- `Connection: close`
- `noexec`
- `Exec format error`
- `Cannot exec a shared library directly`
- `Socket operation on non-socket`
- `Protocol wrong type for socket`
- `Socket type not supported`
- `Network dropped connection on reset`
- `Software caused connection abort`
- `Connection reset by peer`
- `Transport endpoint is already connected`
- `Transport endpoint is not connected`
- `Connection timed out`
- `Connection refused`
- `__get_myaddress: socket`


## Analyst conclusion

This is suitable for CTI, hunting, detection engineering and manual reversing. Full behavioral claims require deeper reversing in an isolated lab.
