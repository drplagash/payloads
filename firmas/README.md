# Firmas

Listado humano de payloads, malware y artifacts high-signal observados por Oraculo SOC.

## Publicado y visible

| Grupo | Cantidad | Entrada |
|---|---:|---|
| High-signal T-Pot artifacts | 517 | [`high-signal/`](high-signal/) |
| Payloads confirmados completos | 1 | [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/`](cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) |

## Qué es una firma

Una firma puede ser:

- un binario confirmado,
- un payload HTTP,
- un downloader,
- un comando de explotación,
- un artifact útil para detección,
- evidencia con IOCs, metadata o detecciones.

## Confirmada completa

| Firma / SHA256 | Tipo | Resumen |
|---|---|---|
| [`cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41`](cad9e90cb8998664e5b39e7336c2310016f5b29704296a1070d950fa40ea8e41/) | ELF32 MIPS payload / malware-like artifact | Capturado desde honeypot controlado y promovido con evidencia, metadata, IOCs, raw inerte, análisis y YARA |

## Campañas con firmas agrupadas

| Campaña | Firmas |
|---|---:|
| [`tpot-router-downloader-campaign-91-92-40`](../casos/tpot-router-downloader-campaign-91-92-40/firmas.md) | 517 |

## Regla

Nada de hash spam sin contexto.

Pero el volumen útil tiene que estar publicado y visible.
