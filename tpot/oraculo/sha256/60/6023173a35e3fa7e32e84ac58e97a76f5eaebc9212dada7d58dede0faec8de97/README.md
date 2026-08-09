# 🧬 Payload Analysis

`6023173a35e3fa7e32e84ac58e97a76f5eaebc9212dada7d58dede0faec8de97`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:54+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6023173a35e3fa7e32e84ac58e97a76f5eaebc9212dada7d58dede0faec8de97`
- **SHA1:** `a994ea2249e5e3516bf6a7dea6df96ce140ed196`
- **MD5:** `d6f13ed74a076f12b4026f9e40698494`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 419 B |
| Entropía | 5.39 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 15.204.184.XXX | static_analysis |
| ip | 190.179.160.XXX | static_analysis |
| hash | 6023173a35e3fa7e32e84ac58e97a76f5eaebc9212dada7d58dede0faec8de97 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
