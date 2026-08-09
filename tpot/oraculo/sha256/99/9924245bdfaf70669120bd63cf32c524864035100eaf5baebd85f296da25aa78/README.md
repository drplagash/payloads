# 🧬 Payload Analysis

`9924245bdfaf70669120bd63cf32c524864035100eaf5baebd85f296da25aa78`

## 📌 Resumen

Artefacto de 4.0 KiB. Formato identificado como very old 16-bit-int little-endian archive. Presenta entropía elevada (7.94), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:26:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9924245bdfaf70669120bd63cf32c524864035100eaf5baebd85f296da25aa78`
- **SHA1:** `79604866ff9183a7030353b0f475a614c340d4a5`
- **MD5:** `9c5b0cb1d0983a376d02dee7aadb6037`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | very old 16-bit-int little-endian archive |
| Tamaño | 4.0 KiB |
| Entropía | 7.94 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=very old 16-bit-int little-endian archive; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 9924245bdfaf70669120bd63cf32c524864035100eaf5baebd85f296da25aa78 | static_analysis |
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
