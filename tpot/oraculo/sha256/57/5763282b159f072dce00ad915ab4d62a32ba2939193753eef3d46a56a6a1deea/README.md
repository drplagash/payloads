# 🧬 Payload Analysis

`5763282b159f072dce00ad915ab4d62a32ba2939193753eef3d46a56a6a1deea`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.15. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5763282b159f072dce00ad915ab4d62a32ba2939193753eef3d46a56a6a1deea`
- **SHA1:** `45f9602536fe2804522a8d5f19f1c998c43ea820`
- **MD5:** `2936cab54bcd33f3f05d295a696065c4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.15 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5763282b159f072dce00ad915ab4d62a32ba2939193753eef3d46a56a6a1deea | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

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
