# 🧬 Payload Analysis

`07a271fe70f12425e616732c0859c3c5226ccc12d9c6e4d2fd3ddc43131d8b5b`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `07a271fe70f12425e616732c0859c3c5226ccc12d9c6e4d2fd3ddc43131d8b5b`
- **MD5:** `3add1fadf713dbb22837b9369d116699`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 618 B |
| Entropía | 5.68 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 172.110.223.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| hash | 07a271fe70f12425e616732c0859c3c5226ccc12d9c6e4d2fd3ddc43131d8b5b | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
