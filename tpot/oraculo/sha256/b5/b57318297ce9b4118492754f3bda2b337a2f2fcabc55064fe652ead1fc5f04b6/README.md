# 🧬 Payload Analysis

`b57318297ce9b4118492754f3bda2b337a2f2fcabc55064fe652ead1fc5f04b6`

## 📌 Resumen

Artefacto de 117 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.10. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b57318297ce9b4118492754f3bda2b337a2f2fcabc55064fe652ead1fc5f04b6`
- **SHA1:** `1adcb256dd363fed79854b253a99885ab0914749`
- **MD5:** `3a9cf22d38f941454c0a9c3cc82811f6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 117 B |
| Entropía | 5.1 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | b57318297ce9b4118492754f3bda2b337a2f2fcabc55064fe652ead1fc5f04b6 | static_analysis |
| ip | 20.127.244.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
