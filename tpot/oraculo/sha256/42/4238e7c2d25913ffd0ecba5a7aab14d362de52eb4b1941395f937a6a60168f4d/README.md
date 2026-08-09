# 🧬 Payload Analysis

`4238e7c2d25913ffd0ecba5a7aab14d362de52eb4b1941395f937a6a60168f4d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Info`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4238e7c2d25913ffd0ecba5a7aab14d362de52eb4b1941395f937a6a60168f4d`
- **SHA1:** `ba07058a129c72841b24ad93f4c7615fa775c4f3`
- **MD5:** `1259840b01821da8fed337380b558b0b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 116 B |
| Entropía | 4.89 |
| Strings | 4 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | 4238e7c2d25913ffd0ecba5a7aab14d362de52eb4b1941395f937a6a60168f4d | static_analysis |
| ip | 64.226.93.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
