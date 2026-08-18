# 🧬 Payload Analysis

`d640ab6ab13ad254e0d3d5021a7f8bef60b14703177c46be49203c2b798a6d03`

## 📌 Resumen

Artefacto de 444 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.54. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d640ab6ab13ad254e0d3d5021a7f8bef60b14703177c46be49203c2b798a6d03`
- **SHA1:** `3a792591e4c540929a8a07b05854e0bed6dcf71a`
- **MD5:** `78b6ec35539769cf3aef25eebe77d966`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 444 B |
| Entropía | 5.54 |
| Strings | 10 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | d640ab6ab13ad254e0d3d5021a7f8bef60b14703177c46be49203c2b798a6d03 | static_analysis |
| ip | 5.61.209.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
