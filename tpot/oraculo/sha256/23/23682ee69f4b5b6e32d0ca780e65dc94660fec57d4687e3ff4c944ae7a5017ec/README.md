# 🧬 Payload Analysis

`23682ee69f4b5b6e32d0ca780e65dc94660fec57d4687e3ff4c944ae7a5017ec`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `23682ee69f4b5b6e32d0ca780e65dc94660fec57d4687e3ff4c944ae7a5017ec`
- **SHA1:** `911ed61a363c95f98d4ca9fa7bc63fb87c6946f2`
- **MD5:** `a31bb13a3384cfd0e982d44a7e52d6fb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 744 B |
| Entropía | 5.33 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| hash | 23682ee69f4b5b6e32d0ca780e65dc94660fec57d4687e3ff4c944ae7a5017ec | static_analysis |
| ip | 87.106.223.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
