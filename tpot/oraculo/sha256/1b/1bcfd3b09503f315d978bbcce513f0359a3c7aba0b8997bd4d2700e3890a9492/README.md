# 🧬 Payload Analysis

`1bcfd3b09503f315d978bbcce513f0359a3c7aba0b8997bd4d2700e3890a9492`

## 📌 Resumen

Artefacto de 4.0 KiB. Formato identificado como DOS executable (COM), start instruction 0xeb364a6f f338d333. Presenta entropía elevada (7.94), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1bcfd3b09503f315d978bbcce513f0359a3c7aba0b8997bd4d2700e3890a9492`
- **SHA1:** `5e22b99384a73b95c78b047f35d9a7c8ab034fe4`
- **MD5:** `7cd06720ab89c95dd86f55789e468e33`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xeb364a6f f338d333 |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 8 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xeb364a6f f338d333; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 1bcfd3b09503f315d978bbcce513f0359a3c7aba0b8997bd4d2700e3890a9492 | static_analysis |
| ip | 189.79.136.XXX | artifact_source |

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
