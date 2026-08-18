# 🧬 Payload Analysis

`70acee4ef7d5c0d5c62cf3c84c1b78d418ab35a2b7047489597ba84e232f50d1`

## 📌 Resumen

Artefacto de 954 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.48. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `45.153.34.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `70acee4ef7d5c0d5c62cf3c84c1b78d418ab35a2b7047489597ba84e232f50d1`
- **SHA1:** `4afd7add816f6214766817cb214c102f5f8b2d39`
- **MD5:** `50b4a9481f90bf9bd85900ad3af41394`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 954 B |
| Entropía | 5.48 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 45.153.34.XXX | static_analysis |
| ip | 190.179.140.XXX | static_analysis |
| hash | 70acee4ef7d5c0d5c62cf3c84c1b78d418ab35a2b7047489597ba84e232f50d1 | static_analysis |
| ip | 124.198.131.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
