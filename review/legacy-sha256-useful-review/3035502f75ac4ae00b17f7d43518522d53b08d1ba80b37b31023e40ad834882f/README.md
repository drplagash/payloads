# 🧬 Payload Analysis

`3035502f75ac4ae00b17f7d43518522d53b08d1ba80b37b31023e40ad834882f`

## 📌 Resumen

Artefacto de 84 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.73. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:56:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3035502f75ac4ae00b17f7d43518522d53b08d1ba80b37b31023e40ad834882f`
- **SHA1:** `766b77e6ac4fa6fe13b6472d4a7d39dce9fc098b`
- **MD5:** `c15e9e29eb42c68ded8d189635845cda`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.73 |
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
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | 3035502f75ac4ae00b17f7d43518522d53b08d1ba80b37b31023e40ad834882f | static_analysis |
| ip | 47.250.123.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
