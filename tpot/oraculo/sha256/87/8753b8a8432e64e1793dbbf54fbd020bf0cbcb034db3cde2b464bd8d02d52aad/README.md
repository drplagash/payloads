# 🧬 Payload Analysis

`8753b8a8432e64e1793dbbf54fbd020bf0cbcb034db3cde2b464bd8d02d52aad`

## 📌 Resumen

Artefacto de 130 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.16. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 indicadores técnicos. **C2 / infraestructura de control:**

- **Posible C2:** `190.179.168.XXX` — confianza Alto, evidencia hardcoded_in_payload


## 🗓️ Registro

- **Registrado:** `2026-08-09T20:05:15.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8753b8a8432e64e1793dbbf54fbd020bf0cbcb034db3cde2b464bd8d02d52aad`
- **SHA1:** `0b4a2f9f12f67f1d75beb011d2b6e3c17e425d50`
- **MD5:** `cbc5ef277b504f5b20291f85de7d76a1`

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
| hash | 8753b8a8432e64e1793dbbf54fbd020bf0cbcb034db3cde2b464bd8d02d52aad | static_analysis |
| ip | 140.238.153.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
