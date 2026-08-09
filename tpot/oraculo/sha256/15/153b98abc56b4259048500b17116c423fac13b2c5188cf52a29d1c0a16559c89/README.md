# 🧬 Payload Analysis

`153b98abc56b4259048500b17116c423fac13b2c5188cf52a29d1c0a16559c89`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:37:19+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `153b98abc56b4259048500b17116c423fac13b2c5188cf52a29d1c0a16559c89`
- **MD5:** `e6a0e97811e733699d59bdd4fc6e86dd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | DOS executable (COM), start instruction 0xb8891178 5bccc6f5 |
| Tamaño | 1.4 KiB |
| Entropía | 7.86 |
| Strings | 2 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=DOS executable (COM), start instruction 0xb8891178 5bccc6f5; high_entropy=7.9; iocs=1

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 153b98abc56b4259048500b17116c423fac13b2c5188cf52a29d1c0a16559c89 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
