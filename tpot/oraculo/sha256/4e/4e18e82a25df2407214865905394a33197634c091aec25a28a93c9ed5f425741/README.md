# 🧬 Payload Analysis

`4e18e82a25df2407214865905394a33197634c091aec25a28a93c9ed5f425741`

## 📌 Resumen

Artefacto de 83 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.78. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4e18e82a25df2407214865905394a33197634c091aec25a28a93c9ed5f425741`
- **SHA1:** `1b9c6b29a25b143b83aa54a516785b0a61cea01b`
- **MD5:** `65b3030c764e12a9a01700827ca81a50`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.78 |
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
| ip | 190.179.160.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 4e18e82a25df2407214865905394a33197634c091aec25a28a93c9ed5f425741 | static_analysis |
| ip | 47.254.22.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
