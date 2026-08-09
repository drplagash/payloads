# 🧬 Payload Analysis

`eefdcbc002fdc86ec4195eb9ab2cf1e1e29ce2d0b2d4066d38e02493d80804c1`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `eefdcbc002fdc86ec4195eb9ab2cf1e1e29ce2d0b2d4066d38e02493d80804c1`
- **SHA1:** `bc45a07c589be10c775d39f4544eda162235c2f1`
- **MD5:** `d2c1068e77dc944b5a56b251dfd80b4c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.72 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.177.XXX | static_analysis |
| hash | eefdcbc002fdc86ec4195eb9ab2cf1e1e29ce2d0b2d4066d38e02493d80804c1 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.84.117.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
