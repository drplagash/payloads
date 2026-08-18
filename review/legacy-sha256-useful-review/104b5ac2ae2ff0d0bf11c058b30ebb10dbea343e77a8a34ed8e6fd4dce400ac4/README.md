# 🧬 Payload Analysis

`104b5ac2ae2ff0d0bf11c058b30ebb10dbea343e77a8a34ed8e6fd4dce400ac4`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/104b5ac2ae2ff0d0bf11c058b30ebb10dbea343e77a8a34ed8e6fd4dce400ac4.md](../../../../../malware-like/oraculo/botnet/104b5ac2ae2ff0d0bf11c058b30ebb10dbea343e77a8a34ed8e6fd4dce400ac4.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `104b5ac2ae2ff0d0bf11c058b30ebb10dbea343e77a8a34ed8e6fd4dce400ac4`
- **SHA1:** `8ea8374a73fc5401b8591ba8d5e5c8f47a1773d8`
- **MD5:** `c78e97016db0f36b13623d8a125da4a0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 94 B |
| Entropía | 4.81 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: curl/7.61.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.169.XXX | static_analysis |
| command | User-Agent: curl/7.61.1 | strings |
| hash | 104b5ac2ae2ff0d0bf11c058b30ebb10dbea343e77a8a34ed8e6fd4dce400ac4 | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
