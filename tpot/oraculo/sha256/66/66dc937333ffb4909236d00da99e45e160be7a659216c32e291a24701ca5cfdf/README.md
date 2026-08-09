# 🧬 Payload Analysis

`66dc937333ffb4909236d00da99e45e160be7a659216c32e291a24701ca5cfdf`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `gsatlasr3dvtlsca2025q4.crl0` en `hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0`. Se extrajeron 7 referencias URL únicas. La evidencia es estática: este snapshot no demuestra por sí solo que la descarga llegara a ejecutarse.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:10:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `66dc937333ffb4909236d00da99e45e160be7a659216c32e291a24701ca5cfdf`
- **SHA1:** `a3c2d4fb4ea265fc6b565b35808e5453a2ddb78f`
- **MD5:** `6ea9c7d32ece5dd6102f1901cd06c011`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.48 |
| Strings | 31 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; high_entropy=7.5; iocs=8

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0 | strings |
| url | hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/root-r3.crt06 | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/gsatlasr3dvtlsca2025q4.crt0 | strings |
| url | hxxps://www[.]globalsign[.]com/repository/0 | strings |
| url | hxxp://crl[.]globalsign[.]com/root-r3.crl0! | strings |
| url | hxxp://ocsp2[.]globalsign[.]com/rootr30; | strings |
| hash | 66dc937333ffb4909236d00da99e45e160be7a659216c32e291a24701ca5cfdf | static_analysis |
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
