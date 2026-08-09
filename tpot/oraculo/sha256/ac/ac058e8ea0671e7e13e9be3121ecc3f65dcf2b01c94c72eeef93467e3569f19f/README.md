# 🧬 Payload Analysis

`ac058e8ea0671e7e13e9be3121ecc3f65dcf2b01c94c72eeef93467e3569f19f`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ac058e8ea0671e7e13e9be3121ecc3f65dcf2b01c94c72eeef93467e3569f19f`
- **SHA1:** `691bdf9b37072129ecc655939f1b4bef068526cb`
- **MD5:** `bde222f5ce15c442402cae0b0726326e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG ADTS, layer I, v2,  56 kbps, Stereo |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG ADTS, layer I, v2,  56 kbps, Stereo; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | ac058e8ea0671e7e13e9be3121ecc3f65dcf2b01c94c72eeef93467e3569f19f | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | media or resource |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
