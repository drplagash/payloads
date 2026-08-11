# 🧬 Payload Analysis

`237363734eece9506fc08a614fe10820c0105273dbcb1f3bca72698bf22d0913`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/237363734eece9506fc08a614fe10820c0105273dbcb1f3bca72698bf22d0913.md](../../../../../malware-like/oraculo/botnet/237363734eece9506fc08a614fe10820c0105273dbcb1f3bca72698bf22d0913.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `237363734eece9506fc08a614fe10820c0105273dbcb1f3bca72698bf22d0913`
- **SHA1:** `f371d7802be6a8900128b7a9cf5907512faba335`
- **MD5:** `51a7166f512dc790a1caa63f6d4e0535`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 142 B |
| Entropía | 5.19 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.73.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 94.156.152.XXX | static_analysis |
| command | User-Agent: curl/7.73.0 | strings |
| hash | 237363734eece9506fc08a614fe10820c0105273dbcb1f3bca72698bf22d0913 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
