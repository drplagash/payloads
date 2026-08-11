# 🧬 Payload Analysis

`02c48fd969dfb46fea10494932629afdb11b2be18f97b1530d796dd09eff0333`

## 📌 Resumen

Artefacto de 130 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.16. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:04:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `02c48fd969dfb46fea10494932629afdb11b2be18f97b1530d796dd09eff0333`
- **SHA1:** `9cc23d4f9c2afe271cb21e0c420e422b83312c45`
- **MD5:** `531b94f2c27ccc466a1185213e235feb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 130 B |
| Entropía | 5.16 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 02c48fd969dfb46fea10494932629afdb11b2be18f97b1530d796dd09eff0333 | static_analysis |
| ip | 220.181.1.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
