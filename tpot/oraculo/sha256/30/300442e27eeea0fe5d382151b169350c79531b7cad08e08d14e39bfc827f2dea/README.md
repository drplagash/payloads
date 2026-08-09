# 🧬 Payload Analysis

`300442e27eeea0fe5d382151b169350c79531b7cad08e08d14e39bfc827f2dea`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:49+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `300442e27eeea0fe5d382151b169350c79531b7cad08e08d14e39bfc827f2dea`
- **SHA1:** `0151473abe0a42025a13b51560e3723e91b31821`
- **MD5:** `c12a97e2e6d1d11dc93ee00f46b28ad1`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.95 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=8.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 300442e27eeea0fe5d382151b169350c79531b7cad08e08d14e39bfc827f2dea | static_analysis |
| ip | 37.57.94.XXX | artifact_source |

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
