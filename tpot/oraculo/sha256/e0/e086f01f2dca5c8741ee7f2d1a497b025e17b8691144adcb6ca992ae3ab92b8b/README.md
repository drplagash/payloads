# 🧬 Payload Analysis

`e086f01f2dca5c8741ee7f2d1a497b025e17b8691144adcb6ca992ae3ab92b8b`

## 📌 Resumen

Artefacto de 548 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `Status_404` en `hxxp://[internal-ip-redacted]/Status_404`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/e086f01f2dca5c8741ee7f2d1a497b025e17b8691144adcb6ca992ae3ab92b8b.md](../../../../../malware-like/oraculo/downloader/e086f01f2dca5c8741ee7f2d1a497b025e17b8691144adcb6ca992ae3ab92b8b.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:01.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e086f01f2dca5c8741ee7f2d1a497b025e17b8691144adcb6ca992ae3ab92b8b`
- **SHA1:** `8f8bce5ddc7aac895ff32574df17677c9030ccae`
- **MD5:** `377c928d9ed11060f6014ef4f237aaf5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 548 B |
| Entropía | 5.37 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]/Status_404 | strings |
| ip | [internal-ip-redacted] | static_analysis |
| hash | e086f01f2dca5c8741ee7f2d1a497b025e17b8691144adcb6ca992ae3ab92b8b | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
