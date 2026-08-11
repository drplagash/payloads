# 🧬 Payload Analysis

`d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2`

## 📌 Resumen

Texto ASCII de 572 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `secext` en `hxxp://schemas[.]xmlsoap[.]org/ws/2002/04/secext`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2.md](../../../../../malware-like/oraculo/downloader/d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2`
- **SHA1:** `5bb017a3285980260781c618d39ec48a0170e444`
- **MD5:** `72a225cf16ce29fbcc863fc876e844ef`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text |
| Tamaño | 572 B |
| Entropía | 5.05 |
| Strings | 19 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/ws/2002/04/secext | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| hash | d12206ee341c6db2db0afc9ff112357212d3c6af9cdb61c10ab4654707418be2 | static_analysis |
| ip | 185.16.38.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
