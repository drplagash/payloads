# 🧬 Payload Analysis

`4f2ef20211e23cbbf80e8da298c195d735c210b338a61336d933f143b1a50b55`

## 📌 Resumen

Texto ASCII de 710 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/4f2ef20211e23cbbf80e8da298c195d735c210b338a61336d933f143b1a50b55.md](../../../../../malware-like/oraculo/downloader/4f2ef20211e23cbbf80e8da298c195d735c210b338a61336d933f143b1a50b55.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4f2ef20211e23cbbf80e8da298c195d735c210b338a61336d933f143b1a50b55`
- **SHA1:** `55fa589ee0dcadf894ef094ae21295be770d35e7`
- **MD5:** `26f32bb4ab45f1133895ec509c3c8196`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (710), with no line terminators |
| Tamaño | 710 B |
| Entropía | 5.21 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (710), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://83.142.209.XXX/a3f8d2/adb.sh; | strings |
| ip | 83.142.209.XXX | static_analysis |
| hash | 4f2ef20211e23cbbf80e8da298c195d735c210b338a61336d933f143b1a50b55 | static_analysis |
| ip | 177.22.44.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
