# 🧬 Payload Analysis

`beac99936530c04aa9d30081701f2d8204cbd350e5519e6846a2184a5fd39f3f`

## 📌 Resumen

Artefacto de 85 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.87. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:42:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `beac99936530c04aa9d30081701f2d8204cbd350e5519e6846a2184a5fd39f3f`
- **SHA1:** `97adff2aa5b78e61005322df353309a011b5a853`
- **MD5:** `708e7d02537ae1c90cd051229755c66c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 85 B |
| Entropía | 4.87 |
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
| ip | 190.179.166.XXX | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| hash | beac99936530c04aa9d30081701f2d8204cbd350e5519e6846a2184a5fd39f3f | static_analysis |
| ip | 51.158.206.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
