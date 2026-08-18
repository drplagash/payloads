# 🧬 Payload Analysis

`2845f5b96859e4972caba969361435cef750a832ad08963f1560123c618fe522`

## 📌 Resumen

Artefacto de 110 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.92. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:37:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2845f5b96859e4972caba969361435cef750a832ad08963f1560123c618fe522`
- **SHA1:** `25c01488197850641158d88bfb7484942e288054`
- **MD5:** `2a66f4fbc28ba5591b95d5825d1b71bc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 110 B |
| Entropía | 4.92 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.74.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.140.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | 2845f5b96859e4972caba969361435cef750a832ad08963f1560123c618fe522 | static_analysis |
| ip | 8.216.7.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
