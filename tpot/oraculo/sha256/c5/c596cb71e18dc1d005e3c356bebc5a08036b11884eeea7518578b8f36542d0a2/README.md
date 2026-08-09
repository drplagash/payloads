# 🧬 Payload Analysis

`c596cb71e18dc1d005e3c356bebc5a08036b11884eeea7518578b8f36542d0a2`

## 📌 Resumen

Artefacto clasificado como **Binary payload** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:07:53+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `c596cb71e18dc1d005e3c356bebc5a08036b11884eeea7518578b8f36542d0a2`
- **SHA1:** `61c6b08dc49cebf4d0e5bc29af7536fa24abaf74`
- **MD5:** `7296f6f7761c57cf257fb4146c498635`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.75 |
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
| hash | c596cb71e18dc1d005e3c356bebc5a08036b11884eeea7518578b8f36542d0a2 | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| ip | 8.216.5.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
