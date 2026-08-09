# 🧬 Payload Analysis

`f8c55d45c0e67abd51cc282c83efb14159722a1f40705e1e02f7a0bb283d1cf3`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f8c55d45c0e67abd51cc282c83efb14159722a1f40705e1e02f7a0bb283d1cf3`
- **SHA1:** `e1ea474e5076f24eae77757c6f4124c31ad6d937`
- **MD5:** `3caf754141ef35076b0ac1afb972707a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.77 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/tv.apk,33261DATA
/data/local/tmp/tv.apkOKAYu
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | f8c55d45c0e67abd51cc282c83efb14159722a1f40705e1e02f7a0bb283d1cf3 | static_analysis |
| command | /data/local/tmp/tv.apk,33261DATA | strings |
| command | /data/local/tmp/tv.apkOKAYu | strings |
| ip | 201.173.65.XXX | artifact_source |

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
