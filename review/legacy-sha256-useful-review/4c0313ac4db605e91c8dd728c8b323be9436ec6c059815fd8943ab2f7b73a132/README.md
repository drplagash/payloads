# 🧬 Payload Analysis

`4c0313ac4db605e91c8dd728c8b323be9436ec6c059815fd8943ab2f7b73a132`

## 📌 Resumen

Artefacto de 113 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.94. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:21:42.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4c0313ac4db605e91c8dd728c8b323be9436ec6c059815fd8943ab2f7b73a132`
- **SHA1:** `707f147dca7e427d3b36bff072c90646b84a5ce4`
- **MD5:** `cbc880f7d2b16289004a4a529cde6c00`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 113 B |
| Entropía | 4.94 |
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
| ip | 190.179.128.XXX | static_analysis |
| command | User-Agent: curl/7.74.0 | strings |
| hash | 4c0313ac4db605e91c8dd728c8b323be9436ec6c059815fd8943ab2f7b73a132 | static_analysis |
| ip | 8.211.149.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
