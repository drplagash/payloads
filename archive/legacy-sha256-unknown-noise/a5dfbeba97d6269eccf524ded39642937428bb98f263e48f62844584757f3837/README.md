# 🧬 Payload Analysis

`a5dfbeba97d6269eccf524ded39642937428bb98f263e48f62844584757f3837`

## 📌 Resumen

Artefacto de 1.0 KiB. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.41. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `172.86.119.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a5dfbeba97d6269eccf524ded39642937428bb98f263e48f62844584757f3837`
- **SHA1:** `bebd8aeda527ac8908a9055297fa4e39f2ada6d5`
- **MD5:** `d9a14fb9deaf0d57a5b9c4058eb22658`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.41 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 172.86.119.XXX | static_analysis |
| hash | a5dfbeba97d6269eccf524ded39642937428bb98f263e48f62844584757f3837 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
