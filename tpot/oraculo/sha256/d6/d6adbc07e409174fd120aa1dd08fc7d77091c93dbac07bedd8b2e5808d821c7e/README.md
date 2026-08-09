# 🧬 Payload Analysis

`d6adbc07e409174fd120aa1dd08fc7d77091c93dbac07bedd8b2e5808d821c7e`

## 📌 Resumen

Artefacto de 137 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.15. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:36:21.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d6adbc07e409174fd120aa1dd08fc7d77091c93dbac07bedd8b2e5808d821c7e`
- **SHA1:** `37cad28b4629c389cae74647e7f50903c273e41c`
- **MD5:** `e79eacdf223d19b6bbded3a050db8d22`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 137 B |
| Entropía | 5.15 |
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
| ip | 152.89.76.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | d6adbc07e409174fd120aa1dd08fc7d77091c93dbac07bedd8b2e5808d821c7e | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
