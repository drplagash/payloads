# 🧬 Payload Analysis

`232bc712eac2187a86f4d56cd3210b92513f52477f86caf2bf3daee4eda7d2d8`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `232bc712eac2187a86f4d56cd3210b92513f52477f86caf2bf3daee4eda7d2d8`
- **SHA1:** `1ab6a955ac26543e1fc170224e0f0c6a9649f50c`
- **MD5:** `d0f630679441d1d5ccb41bda941b1ab6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.78 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apk,33261DATA
/data/local/tmp/ufo.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 232bc712eac2187a86f4d56cd3210b92513f52477f86caf2bf3daee4eda7d2d8 | static_analysis |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| ip | 220.83.108.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
