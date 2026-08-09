# 🧬 Payload Analysis

`b87cd8278d864f7f4d8eff8d77bc82253555e39abdf4a4a7126bbd5fa3723909`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:34:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b87cd8278d864f7f4d8eff8d77bc82253555e39abdf4a4a7126bbd5fa3723909`
- **SHA1:** `a6c8c26aef131131a72b0234c0310d1b9d113b49`
- **MD5:** `e06461b3b196b1f65d5d304303420b90`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.79 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apk,33261WRTE
/data/local/tmp/ufo.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | b87cd8278d864f7f4d8eff8d77bc82253555e39abdf4a4a7126bbd5fa3723909 | static_analysis |
| command | /data/local/tmp/ufo.apk,33261WRTE | strings |
| command | /data/local/tmp/ufo.apkOKAY | strings |
| ip | 180.107.116.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
