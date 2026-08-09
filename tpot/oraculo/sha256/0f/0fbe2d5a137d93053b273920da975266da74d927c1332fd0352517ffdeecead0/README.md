# 🧬 Payload Analysis

`0fbe2d5a137d93053b273920da975266da74d927c1332fd0352517ffdeecead0`

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

- **SHA256:** `0fbe2d5a137d93053b273920da975266da74d927c1332fd0352517ffdeecead0`
- **SHA1:** `de86530deb8e06ea2f401920ca45d1ad47ff54d0`
- **MD5:** `5ba59e205ef5711f9fd54d9649117c06`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.1 KiB |
| Entropía | 7.71 |
| Strings | 14 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.7; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apk,33261WRTE
/data/local/tmp/ufo.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0fbe2d5a137d93053b273920da975266da74d927c1332fd0352517ffdeecead0 | static_analysis |
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
