# 🧬 Payload Analysis

`2030dd018caec80226e84853a31d67071416844271dbb072f3f526f28b675424`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:13:23+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2030dd018caec80226e84853a31d67071416844271dbb072f3f526f28b675424`
- **SHA1:** `3a7c116327841c17a2dfd858069ac22b1d5577a9`
- **MD5:** `b6459e81c0b145b3d211c404475ff44c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.47 |
| Strings | 30 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; high_entropy=7.5; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0 | strings |
| url | hxxp://crl[.]globalsign[.]com/root-r3.crl0! | strings |
| url | hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J | strings |
| url | hxxp://ocsp2[.]globalsign[.]com/rootr30; | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/gsatlasr3dvtlsca2025q4.crt0 | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/root-r3.crt06 | strings |
| url | hxxps://www[.]globalsign[.]com/repository/0 | strings |
| hash | 2030dd018caec80226e84853a31d67071416844271dbb072f3f526f28b675424 | static_analysis |
| ip | 151.101.2.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
