# T-Pot router downloader campaign: multi-surface command injection

## Executive summary

This case study documents a router and IoT downloader campaign observed through T-Pot telemetry and processed by the Oraculo SOC payload workflow.

The campaign abused multiple exposed web management surfaces to inject shell commands, move into `/tmp`, download remote shell scripts or binaries, execute them with `sh`, and remove temporary artifacts.

This is not presented as 517 independent malware samples. It is presented as a campaign-level detection and triage result built from 517 high-signal payload artifacts.

## Why this matters

The value of the analysis is not the raw number of hashes. The value is the conversion of noisy honeypot payloads into a defensive story:

- common attacker behavior,
- affected device surfaces,
- command execution patterns,
- downloader infrastructure,
- reusable detection pivots,
- sanitized evidence suitable for public reporting.

## Dataset summary

- High-signal candidates: 517
- HNAP GetDeviceSettings cases: 8
- Linksys JNAP SetupWizard / Diagnostics cases: 18
- TTCP parameter injection cases: 17
- syscmd.htm command execution cases: 4
- ping_test command injection cases: 2
- weblogin.cgi command injection cases: 1
- Additional downloader patterns grouped as other: 467

The full historical tree remains preserved in the `legacy-bulk-archive` branch.

## Observed behavior

The payloads consistently show:

- command injection through HTTP parameters or headers,
- staging in `/tmp`,
- remote retrieval with `wget`, `busybox wget`, or `curl`,
- pipe-to-shell execution,
- explicit `chmod` and `sh` execution in some variants,
- temporary file cleanup with `rm -f`,
- architecture or bot-family hints in execution arguments.

## Representative attack surfaces

| Surface | Example behavior |
|---|---|
| HNAP GetDeviceSettings | SOAPAction command injection with remote downloader |
| Linksys JNAP Diagnostics / SetupWizard | JSON command field abuse with shell injection |
| Netgear setup.cgi | `todo=syscmd` execution leading to Mozi downloader retrieval |
| ping_test | ping parameter injection followed by downloader execution |
| syscmd.htm | direct command execution through sysCmd |
| ttcp_ip | TTCP parameter injection with `wget | sh` |
| weblogin.cgi | username parameter injection with downloader staging |

## Downloader infrastructure

The most repeated downloader infrastructure in this case uses:

- `91.92.40.XXX/wget.sh`
- `160.30.142.XXX:60115/Mozi.m`

The public repository intentionally keeps IPs partially redacted when needed. The goal is defensive evidence without turning the repository into an operational abuse feed for bored goblins with keyboards.

## Detection pivots

Useful pivots from the campaign:

```text
/HNAP1/GetDeviceSettings/
linksys.com/jnap/network/Diagnostics
linksys.com/jnap/setup/SetupWizard
/setup.cgi?next_file=netgear.cfg&todo=syscmd
/syscmd.htm
weblogin.cgi?username=
todo=ping_test&ping_ip=
ttcp_ip=
cd /tmp
wget http
busybox wget
curl -o
chmod 777
sh .s
wget.sh
Mozi.m








