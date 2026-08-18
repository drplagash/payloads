# Router downloader campaign detections

Fuente: `casos/tpot-router-downloader-campaign-91-92-40/`

Esta detección cubre una campaña router/IoT downloader observada en T-Pot y agrupada desde 517 artefactos high-signal.

No todos los artefactos son binarios malware completos. Muchos son payloads HTTP de explotación: comandos inyectados, downloaders, staging en `/tmp`, uso de `wget`, `busybox wget`, `curl`, `chmod` y ejecución con `sh`.

## Comportamiento a detectar

1. Abuso de superficies web de routers o IoT.
2. Inyección de comandos por parámetros HTTP, JSON o headers.
3. Cambio de directorio a `/tmp`.
4. Descarga remota de script o binario.
5. Ejecución con `sh` o pipe-to-shell.
6. Limpieza con `rm -f`.

## Superficies observadas

| Superficie | Pivots útiles |
|---|---|
| HNAP GetDeviceSettings | `/HNAP1/GetDeviceSettings/`, `SOAPAction`, backticks, `wget` |
| Linksys JNAP | `linksys.com/jnap/network/Diagnostics`, `linksys.com/jnap/setup/SetupWizard`, `Ping` |
| Netgear setup.cgi | `/setup.cgi?next_file=netgear.cfg`, `todo=syscmd` |
| syscmd.htm | `/syscmd.htm`, `sysCmd=` |
| ping_test | `todo=ping_test`, `ping_ip=` |
| ttcp_ip | `ttcp_ip=`, `wget`, `sh` |
| weblogin.cgi | `weblogin.cgi?username=`, command separators |

## Pivots de búsqueda

```text
/HNAP1/GetDeviceSettings/
SOAPAction
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
```

## KQL / SIEM hunting draft

```text
url.path : ("/HNAP1/GetDeviceSettings/" or "/setup.cgi" or "/syscmd.htm")
or url.query : ("todo=syscmd" or "todo=ping_test" or "ttcp_ip=" or "username=")
or http.request.body.content : ("wget" or "busybox wget" or "curl -o" or "cd /tmp" or "chmod" or "wget.sh" or "Mozi.m")
```

## Suricata-style HTTP logic

```text
alert http any any -> any any (msg:"ORACULO T-Pot router downloader command injection attempt"; content:"wget"; http_client_body; content:"/tmp"; http_client_body; classtype:web-application-attack; sid:9001001; rev:1;)
```

Uso: regla conceptual para laboratorio. Ajustar `sid`, direcciones, puertos y buffers según el entorno real.

## Sigma-style idea

```yaml
title: Router IoT Downloader Command Injection Pattern
status: experimental
description: Detects HTTP requests containing router/IoT command injection and downloader staging patterns observed in T-Pot telemetry.
logsource:
  category: webserver
selection_surface:
  cs-uri-query|contains:
    - 'todo=syscmd'
    - 'todo=ping_test'
    - 'ttcp_ip='
    - 'username='
selection_downloader:
  cs-uri-query|contains:
    - 'wget'
    - 'busybox wget'
    - 'curl'
    - 'cd /tmp'
    - 'chmod'
condition: selection_surface and selection_downloader
level: high
```

## Evidencia relacionada

- `casos/tpot-router-downloader-campaign-91-92-40/README.md`
- `casos/tpot-router-downloader-campaign-91-92-40/firmas.md`
- `casos/tpot-router-downloader-campaign-91-92-40/evidence/`

## Estado

Detección documentada como pivots y borradores defensivos. Sirve para charla, SOC triage y threat hunting. No reemplaza validación formal en producción.
