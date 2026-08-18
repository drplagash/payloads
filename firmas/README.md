# Firmas

Listado humano de payloads, malware y artifacts high-signal observados por Oraculo SOC.

Una firma puede ser un binario confirmado, un payload HTTP, un downloader, un comando de explotación o un artifact útil para detección.

## Confirmadas

| Firma / SHA256 | Tipo | Resumen |
|---|---|---|
| [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`](cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) | ELF32 MIPS payload / malware-like artifact | Capturado desde honeypot controlado y promovido con evidencia, metadata, IOCs y análisis |

## Campañas con firmas agrupadas

| Campaña | Firmas |
|---|---|
| [`tpot-router-downloader-campaign-91-92-40`](../casos/tpot-router-downloader-campaign-91-92-40/firmas.md) | 517 high-signal artifacts |

## Regla

Nada de hash spam sin contexto.

Pero tampoco esconder el volumen real. Las firmas útiles deben estar listadas, agrupadas y navegables.
