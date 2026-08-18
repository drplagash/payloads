# 🧬 Payload Analysis

`1ec71a3bfc213ef3ff07b585006f208404b9058b358751e5d1a8cda9f44dc805`

## 📌 Resumen

Artefacto de 997 B. Formato identificado como ASCII text, with very long lines (403), with CRLF line terminators. Entropía registrada: 5.52. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 3 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `45.153.34.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1ec71a3bfc213ef3ff07b585006f208404b9058b358751e5d1a8cda9f44dc805`
- **SHA1:** `5ba814e21dc7b9e05aca732836dac6fa3ec36b7a`
- **MD5:** `9efb264dd6255f6cc9f6da821a7c8b75`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (403), with CRLF line terminators |
| Tamaño | 997 B |
| Entropía | 5.52 |
| Strings | 16 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with very long lines (403), with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 45.153.34.XXX | static_analysis |
| hash | 1ec71a3bfc213ef3ff07b585006f208404b9058b358751e5d1a8cda9f44dc805 | static_analysis |
| ip | 193.26.115.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
