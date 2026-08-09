# 🧬 Payload Analysis

`efa8bacbfe4537e030226c520e98e715c4efce8b3f9cb6b87a0c7ba87459cfdb`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como Compiled PSI (v1) data. Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:43:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `efa8bacbfe4537e030226c520e98e715c4efce8b3f9cb6b87a0c7ba87459cfdb`
- **MD5:** `575aa7f5ffe06be1353ba7981c15cd2a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Compiled PSI (v1) data |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Alta entropía / posible empaquetado o cifrado**

## 🔬 Evidencia de clasificación

- High entropy (7.9) — posible packer/encrypted
High entropy (7.9) — posible packer/encrypted

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | efa8bacbfe4537e030226c520e98e715c4efce8b3f9cb6b87a0c7ba87459cfdb | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
