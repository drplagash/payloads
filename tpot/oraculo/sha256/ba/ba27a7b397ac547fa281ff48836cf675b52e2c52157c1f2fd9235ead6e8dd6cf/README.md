# 🧬 Payload Analysis

`ba27a7b397ac547fa281ff48836cf675b52e2c52157c1f2fd9235ead6e8dd6cf`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:18:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ba27a7b397ac547fa281ff48836cf675b52e2c52157c1f2fd9235ead6e8dd6cf`
- **SHA1:** `b1bb7c84609f11c2267043371c1e167fd17f7e92`
- **MD5:** `73c3ac572fd4f8f57204f87cda4447b9`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 124 B |
| Entropía | 5.12 |
| Strings | 5 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.128.XXX | static_analysis |
| hash | ba27a7b397ac547fa281ff48836cf675b52e2c52157c1f2fd9235ead6e8dd6cf | static_analysis |
| ip | 135.233.112.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
