# 🧬 Payload Analysis

`232bc712eac2187a86f4d56cd3210b92513f52477f86caf2bf3daee4eda7d2d8`

## 📌 Resumen

Artefacto de 4.0 KiB. Presenta entropía elevada (7.78), compatible con contenido empaquetado, cifrado o de alta aleatoriedad. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificaron 2 comandos observados o extraídos. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53.000000Z`
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
/data/local/tmp/ufo.apkOKAY
/data/local/tmp/ufo.apk,33261DATA
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| hash | 232bc712eac2187a86f4d56cd3210b92513f52477f86caf2bf3daee4eda7d2d8 | static_analysis |
| ip | 220.83.108.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
