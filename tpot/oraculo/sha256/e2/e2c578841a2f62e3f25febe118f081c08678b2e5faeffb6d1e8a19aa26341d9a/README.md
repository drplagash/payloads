# 🧬 Payload Analysis

`e2c578841a2f62e3f25febe118f081c08678b2e5faeffb6d1e8a19aa26341d9a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e2c578841a2f62e3f25febe118f081c08678b2e5faeffb6d1e8a19aa26341d9a`
- **MD5:** `eab7fd677f744285dfe4f3aecfee6e2a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 801 B |
| Entropía | 5.5 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 188.68.57.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | e2c578841a2f62e3f25febe118f081c08678b2e5faeffb6d1e8a19aa26341d9a | static_analysis |
| ip | 144.172.106.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
