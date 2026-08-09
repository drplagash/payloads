# 🧬 Payload Analysis

`5c422e238c136369a9c2bd12c44ef5fb934df22e27b815800c15145094446d42`

## 📌 Resumen

Artefacto de 1.4 KiB. Formato identificado como Atari 68xxx CPX file (version 5f30). Presenta entropía elevada (7.89), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. Las detecciones YARA incluyen `Suspicious_High_Entropy`. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 indicador técnico adicional.


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5c422e238c136369a9c2bd12c44ef5fb934df22e27b815800c15145094446d42`
- **SHA1:** `b6de05e7d00d845415ea1b04db050c9c60f0149f`
- **MD5:** `c3405e0f59e16d36061312aac7b42ab7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | Atari 68xxx CPX file (version 5f30) |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=Atari 68xxx CPX file (version 5f30); high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5c422e238c136369a9c2bd12c44ef5fb934df22e27b815800c15145094446d42 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

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
