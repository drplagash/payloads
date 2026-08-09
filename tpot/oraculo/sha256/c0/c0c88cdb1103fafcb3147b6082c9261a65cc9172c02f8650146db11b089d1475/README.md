# 🧬 Payload Analysis

`c0c88cdb1103fafcb3147b6082c9261a65cc9172c02f8650146db11b089d1475`

## 📌 Resumen

Artefacto de 1.7 KiB. Presenta entropía elevada (7.73), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:12:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c0c88cdb1103fafcb3147b6082c9261a65cc9172c02f8650146db11b089d1475`
- **SHA1:** `8fe947fae4dedc6c59bc8a7b76e5af81b1f9bbfc`
- **MD5:** `a80fba831af9331066b2a73cb1866686`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.7 KiB |
| Entropía | 7.73 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.7; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | c0c88cdb1103fafcb3147b6082c9261a65cc9172c02f8650146db11b089d1475 | static_analysis |
| ip | 69.5.169.XXX | artifact_source |

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
