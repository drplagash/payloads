# 🧬 Payload Analysis

`b28b438bdb75694a43ca143f41559d7f9beb7d68b6e6b977a254ca284b0aecc7`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b28b438bdb75694a43ca143f41559d7f9beb7d68b6e6b977a254ca284b0aecc7`
- **SHA1:** `fad4b12c18c5fa96650075ee4cfbf8a15cc0de15`
- **MD5:** `59ef6e94f04c3fed67f80b9e9a8e28c6`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.78 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.81.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.160.XXX | static_analysis |
| hash | b28b438bdb75694a43ca143f41559d7f9beb7d68b6e6b977a254ca284b0aecc7 | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| ip | 62.210.198.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
