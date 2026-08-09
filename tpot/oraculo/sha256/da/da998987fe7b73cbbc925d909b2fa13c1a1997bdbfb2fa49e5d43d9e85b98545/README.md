# 🧬 Payload Analysis

`da998987fe7b73cbbc925d909b2fa13c1a1997bdbfb2fa49e5d43d9e85b98545`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:59:10+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `da998987fe7b73cbbc925d909b2fa13c1a1997bdbfb2fa49e5d43d9e85b98545`
- **SHA1:** `998bf96031353ed4dc251dac17f7a24537f1962c`
- **MD5:** `93b53b42f112553143f3c79ec9b91c79`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 512 B |
| Entropía | 5.69 |
| Strings | 13 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | da998987fe7b73cbbc925d909b2fa13c1a1997bdbfb2fa49e5d43d9e85b98545 | static_analysis |
| ip | 107.189.24.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
