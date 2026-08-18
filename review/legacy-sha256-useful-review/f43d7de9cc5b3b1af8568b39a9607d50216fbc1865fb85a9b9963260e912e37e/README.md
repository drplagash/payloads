# 🧬 Payload Analysis

`f43d7de9cc5b3b1af8568b39a9607d50216fbc1865fb85a9b9963260e912e37e`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `0` en `hxxps://www[.]globalsign[.]com/repository/0`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/f43d7de9cc5b3b1af8568b39a9607d50216fbc1865fb85a9b9963260e912e37e.md](../../../../../malware-like/oraculo/downloader/f43d7de9cc5b3b1af8568b39a9607d50216fbc1865fb85a9b9963260e912e37e.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f43d7de9cc5b3b1af8568b39a9607d50216fbc1865fb85a9b9963260e912e37e`
- **SHA1:** `dd5eb45ca2a53ee2475859275f387dbb13ab3d2d`
- **MD5:** `467a449e683fb83a85bb461f0397e619`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.48 |
| Strings | 30 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; high_entropy=7.5; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://www[.]globalsign[.]com/repository/0 | strings |
| url | hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0 | strings |
| url | hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J | strings |
| url | hxxp://ocsp2[.]globalsign[.]com/rootr30; | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/root-r3.crt06 | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/gsatlasr3dvtlsca2025q4.crt0 | strings |
| url | hxxp://crl[.]globalsign[.]com/root-r3.crl0! | strings |
| hash | f43d7de9cc5b3b1af8568b39a9607d50216fbc1865fb85a9b9963260e912e37e | static_analysis |
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
