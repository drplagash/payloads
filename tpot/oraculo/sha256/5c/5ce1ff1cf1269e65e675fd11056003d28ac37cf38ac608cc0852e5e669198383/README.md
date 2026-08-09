# 🧬 Payload Analysis

`5ce1ff1cf1269e65e675fd11056003d28ac37cf38ac608cc0852e5e669198383`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.03. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:52:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5ce1ff1cf1269e65e675fd11056003d28ac37cf38ac608cc0852e5e669198383`
- **SHA1:** `c471730d9f963104341c0462f9970a6430f9df05`
- **MD5:** `215f7d60a37c9299a7ddb79fff48ca7b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.03 |
| Strings | 34 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5ce1ff1cf1269e65e675fd11056003d28ac37cf38ac608cc0852e5e669198383 | static_analysis |
| ip | 128.70.137.XXX | artifact_source |

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
