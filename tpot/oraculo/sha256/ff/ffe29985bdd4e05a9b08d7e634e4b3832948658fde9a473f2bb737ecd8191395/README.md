# 🧬 Payload Analysis

`ffe29985bdd4e05a9b08d7e634e4b3832948658fde9a473f2bb737ecd8191395`

## 📌 Resumen

Artefacto de 84 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 4.86. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Binary payload`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:24:57.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ffe29985bdd4e05a9b08d7e634e4b3832948658fde9a473f2bb737ecd8191395`
- **SHA1:** `a3479e28085f69120ee9c4316377aba8c771dc8b`
- **MD5:** `41797e3b86c2701c4ad7f2201427e6e4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 84 B |
| Entropía | 4.86 |
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
| ip | 190.179.128.XXX | static_analysis |
| command | User-Agent: curl/7.64.1 | strings |
| hash | ffe29985bdd4e05a9b08d7e634e4b3832948658fde9a473f2bb737ecd8191395 | static_analysis |
| ip | 47.251.57.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
