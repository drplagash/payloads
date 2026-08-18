# 🧬 Payload Analysis

`1c55d5ffeb9a7000d2ebdc2a801745f7bc25428fbf318d84318f5be538cb4439`

## 📌 Resumen

Artefacto de 966 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.64. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `134.0.0.XXX` — confianza Medio, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1c55d5ffeb9a7000d2ebdc2a801745f7bc25428fbf318d84318f5be538cb4439`
- **SHA1:** `9beddbead3fbce52884f9dd06b5d1d637f43efd7`
- **MD5:** `a846143ced47130d828aad8de83e7086`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 966 B |
| Entropía | 5.64 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 134.0.0.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | 1c55d5ffeb9a7000d2ebdc2a801745f7bc25428fbf318d84318f5be538cb4439 | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
