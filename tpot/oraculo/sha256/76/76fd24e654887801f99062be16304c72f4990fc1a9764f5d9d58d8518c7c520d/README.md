# 🧬 Payload Analysis

`76fd24e654887801f99062be16304c72f4990fc1a9764f5d9d58d8518c7c520d`

## 📌 Resumen

Artefacto de 133 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.10. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:39:05.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `76fd24e654887801f99062be16304c72f4990fc1a9764f5d9d58d8518c7c520d`
- **SHA1:** `9a6697763a9dcf5a6c94eaaee880b04b78705678`
- **MD5:** `06b019507a00139242aae652abf9b919`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 133 B |
| Entropía | 5.1 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/8.7.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.166.XXX | static_analysis |
| command | User-Agent: curl/8.7.1 | strings |
| hash | 76fd24e654887801f99062be16304c72f4990fc1a9764f5d9d58d8518c7c520d | static_analysis |
| ip | 178.128.151.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
