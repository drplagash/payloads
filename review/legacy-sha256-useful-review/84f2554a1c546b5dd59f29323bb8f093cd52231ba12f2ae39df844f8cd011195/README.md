# 🧬 Payload Analysis

`84f2554a1c546b5dd59f29323bb8f093cd52231ba12f2ae39df844f8cd011195`

## 📌 Resumen

Artefacto de 4.0 KiB. Formato identificado como DOS executable (COM), start instruction 0x8c4c0b28 e5080a7a. Presenta entropía elevada (7.93), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Binary execution. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:56.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `84f2554a1c546b5dd59f29323bb8f093cd52231ba12f2ae39df844f8cd011195`
- **SHA1:** `f609dc8781dd9536e53fdd4de8f753c05bb47787`
- **MD5:** `40411a001b8b3fb738d599561cab990c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8c4c0b28 e5080a7a |
| Tamaño | 4.0 KiB |
| Entropía | 7.93 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **High entropy obfuscation**
2. **Binary execution**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8c4c0b28 e5080a7a; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 84f2554a1c546b5dd59f29323bb8f093cd52231ba12f2ae39df844f8cd011195 | static_analysis |
| ip | 103.105.40.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | archive container |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
