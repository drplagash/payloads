# 🧬 Payload Analysis

`d1c9327f71dd9b3b7a260a1af1746d34b8deb47351dc4be1162a242f3f7d2863`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:30:55+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d1c9327f71dd9b3b7a260a1af1746d34b8deb47351dc4be1162a242f3f7d2863`
- **SHA1:** `5170332a94ba87419e8fd8a388c29e4f8da092dc`
- **MD5:** `3d9eb660f212a0903024ea1914e93110`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.81 |
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
| ip | 190.179.140.XXX | static_analysis |
| hash | d1c9327f71dd9b3b7a260a1af1746d34b8deb47351dc4be1162a242f3f7d2863 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.77.195.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
