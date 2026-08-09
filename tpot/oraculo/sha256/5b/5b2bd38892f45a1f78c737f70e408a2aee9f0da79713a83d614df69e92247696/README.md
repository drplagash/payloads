# 🧬 Payload Analysis

`5b2bd38892f45a1f78c737f70e408a2aee9f0da79713a83d614df69e92247696`

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

- **SHA256:** `5b2bd38892f45a1f78c737f70e408a2aee9f0da79713a83d614df69e92247696`
- **SHA1:** `bcde5954e81086901bd9df4e4ba9ad9c96f9f7b1`
- **MD5:** `c9e8aff370097d033ced2a582720e723`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.79 |
| Strings | 22 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apkOKAY="
/data/local/tmp/ufo.apkWRTE="
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 5b2bd38892f45a1f78c737f70e408a2aee9f0da79713a83d614df69e92247696 | static_analysis |
| command | /data/local/tmp/ufo.apkOKAY=" | strings |
| command | /data/local/tmp/ufo.apkWRTE=" | strings |
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
