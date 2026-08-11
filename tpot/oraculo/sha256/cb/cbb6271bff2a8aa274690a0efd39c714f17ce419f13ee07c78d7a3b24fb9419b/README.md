# 🧬 Payload Analysis

`cbb6271bff2a8aa274690a0efd39c714f17ce419f13ee07c78d7a3b24fb9419b`

## 📌 Resumen

Artefacto de 1.0 KiB. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.45. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `172.86.119.XXX` — confianza Alto, evidencia hardcoded_in_payload
- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `cbb6271bff2a8aa274690a0efd39c714f17ce419f13ee07c78d7a3b24fb9419b`
- **SHA1:** `b2d1049f39456d29f43830c20c1a8ff3e138b1c0`
- **MD5:** `63b0b8ebf3eff1e397656ae15ac9dc60`

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
| hash | cbb6271bff2a8aa274690a0efd39c714f17ce419f13ee07c78d7a3b24fb9419b | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
