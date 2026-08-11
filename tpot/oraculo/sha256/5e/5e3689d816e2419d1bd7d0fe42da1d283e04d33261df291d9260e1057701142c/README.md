# 🧬 Payload Analysis

`5e3689d816e2419d1bd7d0fe42da1d283e04d33261df291d9260e1057701142c`

## 📌 Resumen

Artefacto de 1.0 KiB. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.45. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `172.86.119.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5e3689d816e2419d1bd7d0fe42da1d283e04d33261df291d9260e1057701142c`
- **SHA1:** `22b4d58de4847090126f7e36bea4c77d5eb4fb1e`
- **MD5:** `0c85242689d1b9110eed528b69527c59`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.45 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 172.86.119.XXX | static_analysis |
| hash | 5e3689d816e2419d1bd7d0fe42da1d283e04d33261df291d9260e1057701142c | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
