# 🧬 Payload Analysis

`df4ff00eae93294fc482b1fddf7e389bba9f9865f20b85190aa88e202bbca00f`

## 📌 Resumen

Artefacto de 115 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.93. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.140.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `df4ff00eae93294fc482b1fddf7e389bba9f9865f20b85190aa88e202bbca00f`
- **SHA1:** `9735468049bcf1cd2020ea5f1c02c9d8d2232a44`
- **MD5:** `1f64199e3635563a7d5a4d01f14ae928`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 115 B |
| Entropía | 4.93 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | df4ff00eae93294fc482b1fddf7e389bba9f9865f20b85190aa88e202bbca00f | static_analysis |
| ip | 138.68.70.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
