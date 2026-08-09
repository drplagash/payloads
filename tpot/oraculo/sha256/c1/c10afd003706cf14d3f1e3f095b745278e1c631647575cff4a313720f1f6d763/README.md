# 🧬 Payload Analysis

`c10afd003706cf14d3f1e3f095b745278e1c631647575cff4a313720f1f6d763`

## 📌 Resumen

La evidencia técnica es compatible con **Suspicious Payload**. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis.


## 🏷️ Clasificación

- **Categoría:** `Suspicious Payload`
- **Confianza:** `Baja`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c10afd003706cf14d3f1e3f095b745278e1c631647575cff4a313720f1f6d763`
- **SHA1:** `b29e5d5e940c12fe3c3e5d58f6fb56788e7f298e`
- **MD5:** `9eb51315fa1237a5b2277f61e76de231`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Commodore VIC-20 +8K BASIC program, offset 0x2e28, line 45667, token (0x85), 3 last bytes 0xacfc3b |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Commodore VIC-20 +8K BASIC program, offset 0x2e28, line 45667, token (0x85), 3 last bytes 0xacfc3b; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c10afd003706cf14d3f1e3f095b745278e1c631647575cff4a313720f1f6d763 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | candidate malware unknown |
| Prioridad | medium |
| Score | 5.0 |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
