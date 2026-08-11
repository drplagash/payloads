# 🧬 Payload Analysis

`6baa59d66840d77220dffe0677ec79b2f5f717955f3185b9d65feacf44863622`

## 📌 Resumen

Artefacto de 738 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.36. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6baa59d66840d77220dffe0677ec79b2f5f717955f3185b9d65feacf44863622`
- **SHA1:** `f7d910658877130a21a32cf8b4c1709f8e5fb20c`
- **MD5:** `b8f2158bf9fd54a47ba1f4c00159e77c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 738 B |
| Entropía | 5.36 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 6baa59d66840d77220dffe0677ec79b2f5f717955f3185b9d65feacf44863622 | static_analysis |
| ip | 87.106.90.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
