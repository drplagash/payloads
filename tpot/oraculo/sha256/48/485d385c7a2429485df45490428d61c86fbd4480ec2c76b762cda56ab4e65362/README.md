# 🧬 Payload Analysis

`485d385c7a2429485df45490428d61c86fbd4480ec2c76b762cda56ab4e65362`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Yara signature match. Se identificó 1 indicador técnico adicional. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/485d385c7a2429485df45490428d61c86fbd4480ec2c76b762cda56ab4e65362.md](../../../../../malware-like/oraculo/botnet/485d385c7a2429485df45490428d61c86fbd4480ec2c76b762cda56ab4e65362.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:34.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `485d385c7a2429485df45490428d61c86fbd4480ec2c76b762cda56ab4e65362`
- **MD5:** `c48c9fd56cd6786ea18d5069787cf87f`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 3.6 KiB |
| Entropía | 5.39 |
| Strings | 73 |

## 🧠 Comportamiento observado

1. **Yara signature match**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; yara_matches=1; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 485d385c7a2429485df45490428d61c86fbd4480ec2c76b762cda56ab4e65362 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
