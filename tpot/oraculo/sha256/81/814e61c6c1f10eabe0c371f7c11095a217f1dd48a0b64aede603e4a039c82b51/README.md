# 🧬 Payload Analysis

`814e61c6c1f10eabe0c371f7c11095a217f1dd48a0b64aede603e4a039c82b51`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `814e61c6c1f10eabe0c371f7c11095a217f1dd48a0b64aede603e4a039c82b51`
- **MD5:** `f701ce58c69371eb36888d3ccc6ec4bb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 416 B |
| Entropía | 5.37 |
| Strings | 11 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 1.1.1.XXX | static_analysis |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.174.XXX | static_analysis |
| hash | 814e61c6c1f10eabe0c371f7c11095a217f1dd48a0b64aede603e4a039c82b51 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
