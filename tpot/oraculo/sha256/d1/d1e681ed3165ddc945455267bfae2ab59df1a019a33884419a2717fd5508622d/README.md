# 🧬 Payload Analysis

`d1e681ed3165ddc945455267bfae2ab59df1a019a33884419a2717fd5508622d`

## 📌 Resumen

Artefacto de 77 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.74. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:09:37.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d1e681ed3165ddc945455267bfae2ab59df1a019a33884419a2717fd5508622d`
- **SHA1:** `4c4758efaa53f151dfe942f52fa1b847a500d8d2`
- **MD5:** `b44926a32932c82ea8e73bd0876c3981`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 77 B |
| Entropía | 4.74 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.29.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.172.XXX | static_analysis |
| command | User-Agent: curl/7.29.0 | strings |
| hash | d1e681ed3165ddc945455267bfae2ab59df1a019a33884419a2717fd5508622d | static_analysis |
| ip | 118.193.59.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
