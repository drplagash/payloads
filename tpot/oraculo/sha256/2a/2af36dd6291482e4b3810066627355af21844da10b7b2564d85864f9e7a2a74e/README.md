# 🧬 Payload Analysis

`2af36dd6291482e4b3810066627355af21844da10b7b2564d85864f9e7a2a74e`

## 📌 Resumen

Artefacto de 136 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.12. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:48:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2af36dd6291482e4b3810066627355af21844da10b7b2564d85864f9e7a2a74e`
- **SHA1:** `cdb48b2c888229c687c103dace0b34015e88f146`
- **MD5:** `6340fb76cfd956fcd33fc1c7e8dabe21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 136 B |
| Entropía | 5.12 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.154.43.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 2af36dd6291482e4b3810066627355af21844da10b7b2564d85864f9e7a2a74e | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
