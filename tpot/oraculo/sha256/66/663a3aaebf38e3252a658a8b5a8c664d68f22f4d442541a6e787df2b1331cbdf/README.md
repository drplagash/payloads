# 🧬 Payload Analysis

`663a3aaebf38e3252a658a8b5a8c664d68f22f4d442541a6e787df2b1331cbdf`

## 📌 Resumen

Artefacto de 82 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.78. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:14:38.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `663a3aaebf38e3252a658a8b5a8c664d68f22f4d442541a6e787df2b1331cbdf`
- **SHA1:** `29e7bc12e2c6dd1d7a3aacc589969c06b4410e99`
- **MD5:** `481b6b16f2b3c6ef3eac2234dbe32071`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 82 B |
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
| ip | 190.179.153.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 663a3aaebf38e3252a658a8b5a8c664d68f22f4d442541a6e787df2b1331cbdf | static_analysis |
| ip | 8.216.5.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
