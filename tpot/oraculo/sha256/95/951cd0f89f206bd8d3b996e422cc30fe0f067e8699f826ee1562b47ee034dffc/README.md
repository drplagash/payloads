# 🧬 Payload Analysis

`951cd0f89f206bd8d3b996e422cc30fe0f067e8699f826ee1562b47ee034dffc`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `951cd0f89f206bd8d3b996e422cc30fe0f067e8699f826ee1562b47ee034dffc`
- **MD5:** `0681b570d69cba2a014d343def766c1d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 7.78 |
| Strings | 15 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.8; iocs=3

## 🖥️ Comandos observados / extraídos

```text
/data/local/tmp/tv.apk,33261DATA
/data/local/tmp/tv.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 951cd0f89f206bd8d3b996e422cc30fe0f067e8699f826ee1562b47ee034dffc | static_analysis |
| command | /data/local/tmp/tv.apk,33261DATA | strings |
| command | /data/local/tmp/tv.apkOKAY | strings |
| ip | 1.28.208.XXX | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_High_Entropy |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
