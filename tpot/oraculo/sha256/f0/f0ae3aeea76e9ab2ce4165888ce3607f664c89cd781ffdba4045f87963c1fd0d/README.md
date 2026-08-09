# 🧬 Payload Analysis

`f0ae3aeea76e9ab2ce4165888ce3607f664c89cd781ffdba4045f87963c1fd0d`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f0ae3aeea76e9ab2ce4165888ce3607f664c89cd781ffdba4045f87963c1fd0d`
- **MD5:** `75cba261c80d1108eadb9608e072ded7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 3.0 KiB |
| Entropía | 7.68 |
| Strings | 23 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.7; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/ufo.apk,33261DATA
/data/local/tmp/ufo.apkOKAYl^
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f0ae3aeea76e9ab2ce4165888ce3607f664c89cd781ffdba4045f87963c1fd0d | static_analysis |
| command | /data/local/tmp/ufo.apk,33261DATA | strings |
| command | /data/local/tmp/ufo.apkOKAYl^ | strings |
| ip | 117.68.74.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
