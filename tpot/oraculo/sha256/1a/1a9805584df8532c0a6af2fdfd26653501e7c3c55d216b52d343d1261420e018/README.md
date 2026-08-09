# 🧬 Payload Analysis

`1a9805584df8532c0a6af2fdfd26653501e7c3c55d216b52d343d1261420e018`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1a9805584df8532c0a6af2fdfd26653501e7c3c55d216b52d343d1261420e018`
- **MD5:** `5faf92465cb09f0ee3bbc06b88f22541`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 618 B |
| Entropía | 5.7 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 1a9805584df8532c0a6af2fdfd26653501e7c3c55d216b52d343d1261420e018 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
