# 🧬 Payload Analysis

`0d8de1c2bc96ba42e96e18103e2463a48d8b8de66830b6f09ba9a50074c13c93`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:51:39+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0d8de1c2bc96ba42e96e18103e2463a48d8b8de66830b6f09ba9a50074c13c93`
- **SHA1:** `0aea0178f25b4a9b28d2d16f8dcfc5c8334d74d0`
- **MD5:** `c0348571eacec60d1b90c355fc323453`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
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
| ip | 190.179.130.XXX | static_analysis |
| hash | 0d8de1c2bc96ba42e96e18103e2463a48d8b8de66830b6f09ba9a50074c13c93 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 47.84.105.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
