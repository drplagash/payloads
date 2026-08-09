# 🧬 Payload Analysis

`513d666f14ea9968598f76a541a02985536f283fe0f5ee7b0de78305c3f4c2dd`

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

- **SHA256:** `513d666f14ea9968598f76a541a02985536f283fe0f5ee7b0de78305c3f4c2dd`
- **SHA1:** `2e0dffcc2898240daec1f90d53f4cfbd60f6d036`
- **MD5:** `d426c193a994178f95bce86e393b3e93`

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
| hash | 513d666f14ea9968598f76a541a02985536f283fe0f5ee7b0de78305c3f4c2dd | static_analysis |
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
