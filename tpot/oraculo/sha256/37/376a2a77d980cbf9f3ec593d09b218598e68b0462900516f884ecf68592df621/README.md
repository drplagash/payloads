# 🧬 Payload Analysis

`376a2a77d980cbf9f3ec593d09b218598e68b0462900516f884ecf68592df621`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como Applesoft BASIC program data, first line number 55. Presenta entropía elevada (7.86), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:06:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `376a2a77d980cbf9f3ec593d09b218598e68b0462900516f884ecf68592df621`
- **SHA1:** `6d8b85ab6b889fc9a407957454d899f759108514`
- **MD5:** `c5c2445a78c72c11917571b7f3b48bb8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Applesoft BASIC program data, first line number 55 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Applesoft BASIC program data, first line number 55; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 376a2a77d980cbf9f3ec593d09b218598e68b0462900516f884ecf68592df621 | static_analysis |
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
