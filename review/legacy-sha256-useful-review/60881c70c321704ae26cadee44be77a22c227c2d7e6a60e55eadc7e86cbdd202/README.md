# 🧬 Payload Analysis

`60881c70c321704ae26cadee44be77a22c227c2d7e6a60e55eadc7e86cbdd202`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.03. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:39.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `60881c70c321704ae26cadee44be77a22c227c2d7e6a60e55eadc7e86cbdd202`
- **MD5:** `5ae0b83355953953d70b4a83898d3d20`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.03 |
| Strings | 97 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 60881c70c321704ae26cadee44be77a22c227c2d7e6a60e55eadc7e86cbdd202 | static_analysis |
| ip | 176.124.197.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
