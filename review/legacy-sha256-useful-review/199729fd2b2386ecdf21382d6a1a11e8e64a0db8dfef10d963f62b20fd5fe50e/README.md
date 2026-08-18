# 🧬 Payload Analysis

`199729fd2b2386ecdf21382d6a1a11e8e64a0db8dfef10d963f62b20fd5fe50e`

## 📌 Resumen

Artefacto de 82 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.77. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:36.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `199729fd2b2386ecdf21382d6a1a11e8e64a0db8dfef10d963f62b20fd5fe50e`
- **SHA1:** `cba487ee67c4068d5bf71e87ef75f5ae5af41386`
- **MD5:** `199fa4c3f90d77e9bccb6e275025bdd5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
| Entropía | 4.77 |
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
| ip | 190.179.172.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 199729fd2b2386ecdf21382d6a1a11e8e64a0db8dfef10d963f62b20fd5fe50e | static_analysis |
| ip | 47.251.48.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
