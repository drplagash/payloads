# 🧬 Payload Analysis

`d3fbd54a8025c757484118114f0b5a54105eb95b8e3a3d68660e96f372b91cf0`

## 📌 Resumen

Artefacto de 96 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.93. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:05:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3fbd54a8025c757484118114f0b5a54105eb95b8e3a3d68660e96f372b91cf0`
- **SHA1:** `703809a289966dcd37f308c0895d416b0bfc8941`
- **MD5:** `5aae46f7a4d0fac87df917eb2cf76484`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 96 B |
| Entropía | 4.93 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 51.81.104.XXX | static_analysis |
| command | User-Agent: curl/7.38.0 | strings |
| hash | d3fbd54a8025c757484118114f0b5a54105eb95b8e3a3d68660e96f372b91cf0 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
