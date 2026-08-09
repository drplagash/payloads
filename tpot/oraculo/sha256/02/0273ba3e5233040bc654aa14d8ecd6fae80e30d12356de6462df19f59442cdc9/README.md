# 🧬 Payload Analysis

`0273ba3e5233040bc654aa14d8ecd6fae80e30d12356de6462df19f59442cdc9`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se registró 1 detección YARA válida. Se asociaron 2 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:47:25+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0273ba3e5233040bc654aa14d8ecd6fae80e30d12356de6462df19f59442cdc9`
- **SHA1:** `f2e464e76a8b87e29fb2aeeda758c2c297ed4856`
- **MD5:** `4cff29b39ad59848a7ad797f1a743164`

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
/data/local/tmp/tv.apkOKAY
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0273ba3e5233040bc654aa14d8ecd6fae80e30d12356de6462df19f59442cdc9 | static_analysis |
| command | /data/local/tmp/tv.apk,33261DATA | strings |
| command | /data/local/tmp/tv.apkOKAY | strings |
| ip | 119.207.147.XXX | artifact_source |

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
