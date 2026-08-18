# 🧬 Payload Analysis

`37d0c078f16dfc715593b11ab50abb295600ceca7e126ab67e7b6cc9fb15570c`

## 📌 Resumen

Artefacto de 116 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.86. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:52.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `37d0c078f16dfc715593b11ab50abb295600ceca7e126ab67e7b6cc9fb15570c`
- **SHA1:** `9d04ee298f70cf1eec3a5fa7ec25e313e5ff0741`
- **MD5:** `c4193c943e019d8e5a83882ad1c7423d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 116 B |
| Entropía | 4.86 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 37d0c078f16dfc715593b11ab50abb295600ceca7e126ab67e7b6cc9fb15570c | static_analysis |
| ip | 207.154.238.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
