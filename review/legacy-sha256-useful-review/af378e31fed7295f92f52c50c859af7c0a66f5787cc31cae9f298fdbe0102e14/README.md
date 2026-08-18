# 🧬 Payload Analysis

`af378e31fed7295f92f52c50c859af7c0a66f5787cc31cae9f298fdbe0102e14`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como DOS executable (COM), start instruction 0x8c3ca3b7 0f66c956. Presenta entropía elevada (7.87), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:20.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `af378e31fed7295f92f52c50c859af7c0a66f5787cc31cae9f298fdbe0102e14`
- **MD5:** `fe14c272be1a9a6a1db1458f0ae82277`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0x8c3ca3b7 0f66c956 |
| Tamaño | 1.4 KiB |
| Entropía | 7.87 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0x8c3ca3b7 0f66c956; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | af378e31fed7295f92f52c50c859af7c0a66f5787cc31cae9f298fdbe0102e14 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
