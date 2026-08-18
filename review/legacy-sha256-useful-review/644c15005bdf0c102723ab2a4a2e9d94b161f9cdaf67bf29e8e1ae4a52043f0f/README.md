# 🧬 Payload Analysis

`644c15005bdf0c102723ab2a4a2e9d94b161f9cdaf67bf29e8e1ae4a52043f0f`

## 📌 Resumen

Artefacto de 4.0 KiB. Entropía registrada: 7.05. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:02:12.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `644c15005bdf0c102723ab2a4a2e9d94b161f9cdaf67bf29e8e1ae4a52043f0f`
- **SHA1:** `4168bd24fb498b0f501c4966c26acc8af8f4181c`
- **MD5:** `6abb874c3e9dd8f632f50d6d2f4ab952`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.05 |
| Strings | 39 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.0; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 644c15005bdf0c102723ab2a4a2e9d94b161f9cdaf67bf29e8e1ae4a52043f0f | static_analysis |
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
