# 🧬 Payload Analysis

`3c9efdddf255ed44492660692b5f9250ee2fa25f1656f5262c79639fd723b54a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3c9efdddf255ed44492660692b5f9250ee2fa25f1656f5262c79639fd723b54a`
- **SHA1:** `bb33ad1eaaa595478866491f8865332144fa8bf0`
- **MD5:** `aa5adb8741c6cbbce3a6b40b910eea83`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.4 KiB |
| Entropía | 7.89 |
| Strings | 3 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; high_entropy=7.9; iocs=2

## 🖥️ Comandos observados / extraídos

```text
_WGETVd
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 3c9efdddf255ed44492660692b5f9250ee2fa25f1656f5262c79639fd723b54a | static_analysis |
| command | _WGETVd | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
