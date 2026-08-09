# 🧬 Payload Analysis

`0df121e711d749ce16f031b315ee5d38d28055c8b4c4cd4496a72d0863c79c51`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:34:59+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0df121e711d749ce16f031b315ee5d38d28055c8b4c4cd4496a72d0863c79c51`
- **SHA1:** `34a229ae1babe09d7169c07cd30722a8c68a481f`
- **MD5:** `32e0d37ffc71f5e29b73209d6fe7ab60`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 25 B |
| Entropía | 4.16 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=2

## 🖥️ Comandos observados / extraídos

```text
MODULE LOAD /tmp/exp.so
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| hash | 0df121e711d749ce16f031b315ee5d38d28055c8b4c4cd4496a72d0863c79c51 | static_analysis |
| command | MODULE LOAD /tmp/exp.so | strings |
| ip | 124.236.108.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
