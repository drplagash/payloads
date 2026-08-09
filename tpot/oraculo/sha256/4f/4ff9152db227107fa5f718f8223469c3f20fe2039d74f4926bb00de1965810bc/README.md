# 🧬 Payload Analysis

`4ff9152db227107fa5f718f8223469c3f20fe2039d74f4926bb00de1965810bc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T18:44:48.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4ff9152db227107fa5f718f8223469c3f20fe2039d74f4926bb00de1965810bc`
- **MD5:** `241ed141b37bf79e0cd6ecf7dbd3f12c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 1018 B |
| Entropía | 5.23 |
| Strings | 30 |

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 179.43.167.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| hash | 4ff9152db227107fa5f718f8223469c3f20fe2039d74f4926bb00de1965810bc | static_analysis |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
