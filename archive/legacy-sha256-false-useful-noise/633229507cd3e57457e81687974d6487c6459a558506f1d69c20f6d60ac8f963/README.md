# 🧬 Payload Analysis

`633229507cd3e57457e81687974d6487c6459a558506f1d69c20f6d60ac8f963`

## 📌 Resumen

Texto ASCII de 625 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `envelope` en `hxxp://schemas[.]xmlsoap[.]org/soap/envelope/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/633229507cd3e57457e81687974d6487c6459a558506f1d69c20f6d60ac8f963.md](../../../../../malware-like/oraculo/downloader/633229507cd3e57457e81687974d6487c6459a558506f1d69c20f6d60ac8f963.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `633229507cd3e57457e81687974d6487c6459a558506f1d69c20f6d60ac8f963`
- **SHA1:** `67f79042f36a2b6f1af566fbd33b4e4dc770ccb4`
- **MD5:** `f7a2845c64ddcf3f771b6ca460f14c1a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (625), with no line terminators |
| Tamaño | 625 B |
| Entropía | 5.38 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (625), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://203.101.186.XXX:60296/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| ip | 203.101.186.XXX | static_analysis |
| hash | 633229507cd3e57457e81687974d6487c6459a558506f1d69c20f6d60ac8f963 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
