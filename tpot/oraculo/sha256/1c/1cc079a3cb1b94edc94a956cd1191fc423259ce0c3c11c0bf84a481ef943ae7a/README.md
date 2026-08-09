# 🧬 Payload Analysis

`1cc079a3cb1b94edc94a956cd1191fc423259ce0c3c11c0bf84a481ef943ae7a`

## 📌 Resumen

Artefacto clasificado como **Payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `1cc079a3cb1b94edc94a956cd1191fc423259ce0c3c11c0bf84a481ef943ae7a`
- **SHA1:** `612d944a40babcfb342757a3ec56f4cda04255af`
- **MD5:** `e7227f39f5d7bf0c2b12e3047ba31c3e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 108 B |
| Entropía | 5.01 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.64.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| hash | 1cc079a3cb1b94edc94a956cd1191fc423259ce0c3c11c0bf84a481ef943ae7a | static_analysis |
| command | User-Agent: curl/7.64.0 | strings |
| ip | 177.136.32.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
