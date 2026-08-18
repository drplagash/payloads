# 🧬 Payload Analysis

`0c53c2e2b474cef3077458a1ebc81a7c0269eefe5c9799e72698693a3ec9ad56`

## 📌 Resumen

Artefacto de 4.0 KiB. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `gsatlasr3dvtlsca2025q40J` en `hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J`. Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/0c53c2e2b474cef3077458a1ebc81a7c0269eefe5c9799e72698693a3ec9ad56.md](../../../../../malware-like/oraculo/downloader/0c53c2e2b474cef3077458a1ebc81a7c0269eefe5c9799e72698693a3ec9ad56.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0c53c2e2b474cef3077458a1ebc81a7c0269eefe5c9799e72698693a3ec9ad56`
- **MD5:** `1800fdfcdd03faf1ca1b6703d66a83a6`

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
| url | hxxp://ocsp[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q40J | strings |
| url | hxxps://www[.]globalsign[.]com/repository/0 | strings |
| url | hxxp://crl[.]globalsign[.]com/ca/gsatlasr3dvtlsca2025q4.crl0 | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/root-r3.crt06 | strings |
| url | hxxp://ocsp2[.]globalsign[.]com/rootr30; | strings |
| url | hxxp://crl[.]globalsign[.]com/root-r3.crl0! | strings |
| url | hxxp://secure[.]globalsign[.]com/cacert/gsatlasr3dvtlsca2025q4.crt0 | strings |
| hash | 0c53c2e2b474cef3077458a1ebc81a7c0269eefe5c9799e72698693a3ec9ad56 | static_analysis |
| ip | 151.101.66.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
