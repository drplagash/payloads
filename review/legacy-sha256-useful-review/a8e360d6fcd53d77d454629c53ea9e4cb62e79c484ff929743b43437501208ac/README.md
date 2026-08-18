# 🧬 Payload Analysis

`a8e360d6fcd53d77d454629c53ea9e4cb62e79c484ff929743b43437501208ac`

## 📌 Resumen

Artefacto de 4.0 KiB. Presenta entropía elevada (7.20), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:50:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a8e360d6fcd53d77d454629c53ea9e4cb62e79c484ff929743b43437501208ac`
- **SHA1:** `b3ac1c461f49d3066142d0c2c08bbccac608060f`
- **MD5:** `adcc898b80f5e4a5e896cc206952ad9a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.2 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.2; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | a8e360d6fcd53d77d454629c53ea9e4cb62e79c484ff929743b43437501208ac | static_analysis |
| ip | 45.150.206.XXX | artifact_source |

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
