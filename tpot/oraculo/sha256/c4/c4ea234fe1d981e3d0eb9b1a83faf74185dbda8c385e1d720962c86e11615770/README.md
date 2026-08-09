# 🧬 Payload Analysis

`c4ea234fe1d981e3d0eb9b1a83faf74185dbda8c385e1d720962c86e11615770`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:47:28+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c4ea234fe1d981e3d0eb9b1a83faf74185dbda8c385e1d720962c86e11615770`
- **SHA1:** `13d9030dd88148979292bf883b498eb3505ce5ba`
- **MD5:** `766be8ffe4d50bc1b6eada50461754cf`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 791 B |
| Entropía | 5.51 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 13.93.165.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| hash | c4ea234fe1d981e3d0eb9b1a83faf74185dbda8c385e1d720962c86e11615770 | static_analysis |
| ip | 108.181.132.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
