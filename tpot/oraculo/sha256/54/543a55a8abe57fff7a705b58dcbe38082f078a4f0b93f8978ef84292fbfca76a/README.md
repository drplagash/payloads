# 🧬 Payload Analysis

`543a55a8abe57fff7a705b58dcbe38082f078a4f0b93f8978ef84292fbfca76a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:49:32+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `543a55a8abe57fff7a705b58dcbe38082f078a4f0b93f8978ef84292fbfca76a`
- **SHA1:** `a174da4bf1176a177c3ebfed4d5662668a8ba8bf`
- **MD5:** `b5ade9e2dd63aa54ef55ba80da7d461f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 416 B |
| Entropía | 5.39 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.144.XXX | static_analysis |
| hash | 543a55a8abe57fff7a705b58dcbe38082f078a4f0b93f8978ef84292fbfca76a | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
