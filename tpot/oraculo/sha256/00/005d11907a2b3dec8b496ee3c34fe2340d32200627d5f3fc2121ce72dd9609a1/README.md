# 🧬 Payload Analysis

`005d11907a2b3dec8b496ee3c34fe2340d32200627d5f3fc2121ce72dd9609a1`

## 📌 Resumen

Artefacto de 1.4 KiB. Entropía registrada: 7.15. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:35:39.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `005d11907a2b3dec8b496ee3c34fe2340d32200627d5f3fc2121ce72dd9609a1`
- **SHA1:** `155e47d9fc5c27980decbfda9ec7363e4e99ded9`
- **MD5:** `cd72fb7b2302612dad1ef851852280ad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.15 |
| Strings | 7 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 005d11907a2b3dec8b496ee3c34fe2340d32200627d5f3fc2121ce72dd9609a1 | static_analysis |
| ip | 200.43.89.XXX | artifact_source |

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
