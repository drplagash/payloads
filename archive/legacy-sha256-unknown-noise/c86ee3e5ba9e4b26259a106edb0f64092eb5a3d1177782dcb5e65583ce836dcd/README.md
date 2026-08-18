# 🧬 Payload Analysis

`c86ee3e5ba9e4b26259a106edb0f64092eb5a3d1177782dcb5e65583ce836dcd`

## 📌 Resumen

Artefacto de 968 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.65. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c86ee3e5ba9e4b26259a106edb0f64092eb5a3d1177782dcb5e65583ce836dcd`
- **SHA1:** `cd9e5585b0a2b4d90a1cfb21cfa960eca415fbc6`
- **MD5:** `0f6e0dffae4ec85b2c6d70f5b2d1b5a9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 968 B |
| Entropía | 5.65 |
| Strings | 17 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | c86ee3e5ba9e4b26259a106edb0f64092eb5a3d1177782dcb5e65583ce836dcd | static_analysis |
| ip | 160.119.71.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
