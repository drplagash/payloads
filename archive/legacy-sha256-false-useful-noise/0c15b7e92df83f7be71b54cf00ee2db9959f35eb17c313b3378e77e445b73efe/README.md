# 🧬 Payload Analysis

`0c15b7e92df83f7be71b54cf00ee2db9959f35eb17c313b3378e77e445b73efe`

## 📌 Resumen

Texto ASCII de 704 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/0c15b7e92df83f7be71b54cf00ee2db9959f35eb17c313b3378e77e445b73efe.md](../../../../../malware-like/oraculo/downloader/0c15b7e92df83f7be71b54cf00ee2db9959f35eb17c313b3378e77e445b73efe.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:22:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0c15b7e92df83f7be71b54cf00ee2db9959f35eb17c313b3378e77e445b73efe`
- **SHA1:** `907f643f88dfd28e7d598828d21b4dc0a267e875`
- **MD5:** `376a51a0f948314871c34843cc4c0083`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (704), with no line terminators |
| Tamaño | 704 B |
| Entropía | 5.2 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (704), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://176.65.149.XXX/adb.sh; | strings |
| ip | 176.65.149.XXX | static_analysis |
| hash | 0c15b7e92df83f7be71b54cf00ee2db9959f35eb17c313b3378e77e445b73efe | static_analysis |
| ip | 39.104.63.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
