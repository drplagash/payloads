# 🧬 Payload Analysis

`5bdcbe9c97b940ec94f898f5be7dcea05ae250f7b6428955d19ddf147682312a`

## 📌 Resumen

Artefacto de 83 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.73. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5bdcbe9c97b940ec94f898f5be7dcea05ae250f7b6428955d19ddf147682312a`
- **SHA1:** `024057808a64e7cbdadfce4e8bfc8e83f397753c`
- **MD5:** `eee2c980b2a1e185ee2555b221d1e304`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 83 B |
| Entropía | 4.73 |
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
| ip | 190.179.144.XXX | static_analysis |
| command | User-Agent: curl/7.81.0 | strings |
| hash | 5bdcbe9c97b940ec94f898f5be7dcea05ae250f7b6428955d19ddf147682312a | static_analysis |
| ip | 51.158.249.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
