# 🧬 Payload Analysis

`b68ea9929607b6b242f21591bc980d71c60f41dc20bfbce70b11ea0c6a1e253a`

## 📌 Resumen

Artefacto de 967 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.65. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b68ea9929607b6b242f21591bc980d71c60f41dc20bfbce70b11ea0c6a1e253a`
- **SHA1:** `a2299288842de4b4527f6575a6e87aa30094ceb0`
- **MD5:** `0ff9c5f23ea9f71b4489f11f6d8bb4cf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 967 B |
| Entropía | 5.65 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | b68ea9929607b6b242f21591bc980d71c60f41dc20bfbce70b11ea0c6a1e253a | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
