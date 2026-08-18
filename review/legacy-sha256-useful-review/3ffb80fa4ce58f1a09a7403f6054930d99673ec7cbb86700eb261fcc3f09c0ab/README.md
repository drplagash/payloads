# 🧬 Payload Analysis

`3ffb80fa4ce58f1a09a7403f6054930d99673ec7cbb86700eb261fcc3f09c0ab`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/3ffb80fa4ce58f1a09a7403f6054930d99673ec7cbb86700eb261fcc3f09c0ab.md](../../../../../malware-like/oraculo/botnet/3ffb80fa4ce58f1a09a7403f6054930d99673ec7cbb86700eb261fcc3f09c0ab.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3ffb80fa4ce58f1a09a7403f6054930d99673ec7cbb86700eb261fcc3f09c0ab`
- **SHA1:** `db10ddd2457e5686cb930c9cde5f730b78a505a1`
- **MD5:** `9a83a05c985ff8ad379bb588e4ae6285`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), maybe with interrupt 22h, start instruction 0xeb2e8180 1d37297f |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), maybe with interrupt 22h, start instruction 0xeb2e8180 1d37297f; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 3ffb80fa4ce58f1a09a7403f6054930d99673ec7cbb86700eb261fcc3f09c0ab | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
