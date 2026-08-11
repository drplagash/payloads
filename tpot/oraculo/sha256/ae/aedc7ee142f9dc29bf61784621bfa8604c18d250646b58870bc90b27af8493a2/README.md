# 🧬 Payload Analysis

`aedc7ee142f9dc29bf61784621bfa8604c18d250646b58870bc90b27af8493a2`

## 📌 Resumen

Artefacto de 1.0 KiB. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.44. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `172.86.119.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `aedc7ee142f9dc29bf61784621bfa8604c18d250646b58870bc90b27af8493a2`
- **SHA1:** `4c1c69bec90ffd86acc3389278110101523c1b1e`
- **MD5:** `0a49b5237f00a963c72beda3630058bc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1.0 KiB |
| Entropía | 5.44 |
| Strings | 33 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| ip | 172.86.119.XXX | static_analysis |
| hash | aedc7ee142f9dc29bf61784621bfa8604c18d250646b58870bc90b27af8493a2 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
