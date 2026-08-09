# 🧬 Payload Analysis

`a18054eb375504b97d2e5da35a3a5630d22b65e062334fd719dab80a3000942b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a18054eb375504b97d2e5da35a3a5630d22b65e062334fd719dab80a3000942b`
- **SHA1:** `1320bd88e068922dd92357c86011032a03a9637f`
- **MD5:** `277205854d09ce078c71ab19fe617d2d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | MPEG-4 LOAS, 4 or more streams, 8 or more streams |
| Tamaño | 1.4 KiB |
| Entropía | 7.9 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=MPEG-4 LOAS, 4 or more streams, 8 or more streams; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | a18054eb375504b97d2e5da35a3a5630d22b65e062334fd719dab80a3000942b | static_analysis |
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
