# 🧬 Payload Analysis

`6f2664e036c0586b4127ca302ebae692ccfae18dc9e23c2c3d0c61b2cab44061`

## 📌 Resumen

Texto ASCII de 696 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `encoding` en `hxxp://schemas[.]xmlsoap[.]org/soap/encoding/`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/6f2664e036c0586b4127ca302ebae692ccfae18dc9e23c2c3d0c61b2cab44061.md](../../../../../malware-like/oraculo/downloader/6f2664e036c0586b4127ca302ebae692ccfae18dc9e23c2c3d0c61b2cab44061.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6f2664e036c0586b4127ca302ebae692ccfae18dc9e23c2c3d0c61b2cab44061`
- **SHA1:** `a3542578907f7f003a45d5f28da2a9807bfa6fe2`
- **MD5:** `3236641629b94f744872aea1efbdebfd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | XML 1.0 document, ASCII text, with very long lines (696), with no line terminators |
| Tamaño | 696 B |
| Entropía | 5.2 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=XML 1.0 document, ASCII text, with very long lines (696), with no line terminators; iocs=5

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/encoding/ | strings |
| url | hxxp://212.7.202.XXX:2025/adb; | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| ip | 212.7.202.XXX | static_analysis |
| hash | 6f2664e036c0586b4127ca302ebae692ccfae18dc9e23c2c3d0c61b2cab44061 | static_analysis |
| ip | 51.158.97.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | html response |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
