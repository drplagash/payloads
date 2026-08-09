# 🧬 Payload Analysis

`e929978d19bc84acc343a6d405b586fce45bf2f8d22d6bf66fafff8dc20b716d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:39:31+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e929978d19bc84acc343a6d405b586fce45bf2f8d22d6bf66fafff8dc20b716d`
- **MD5:** `8830b3da1c7af11def518ae89e0efe22`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 462 B |
| Entropía | 5.61 |
| Strings | 12 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | e929978d19bc84acc343a6d405b586fce45bf2f8d22d6bf66fafff8dc20b716d | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
