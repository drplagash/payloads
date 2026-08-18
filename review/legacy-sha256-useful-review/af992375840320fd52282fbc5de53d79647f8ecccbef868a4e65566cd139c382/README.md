# 🧬 Payload Analysis

`af992375840320fd52282fbc5de53d79647f8ecccbef868a4e65566cd139c382`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como Java serialization data, version 6625. Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `af992375840320fd52282fbc5de53d79647f8ecccbef868a4e65566cd139c382`
- **SHA1:** `25aa832effd123b4520105905571f4c88970be7a`
- **MD5:** `3c2c6310c2ad13f0562654361e4a6c71`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Java serialization data, version 6625 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Java serialization data, version 6625; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | af992375840320fd52282fbc5de53d79647f8ecccbef868a4e65566cd139c382 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
