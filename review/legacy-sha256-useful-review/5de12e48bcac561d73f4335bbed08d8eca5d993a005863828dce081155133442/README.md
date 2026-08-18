# 🧬 Payload Analysis

`5de12e48bcac561d73f4335bbed08d8eca5d993a005863828dce081155133442`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/5de12e48bcac561d73f4335bbed08d8eca5d993a005863828dce081155133442.md](../../../../../malware-like/oraculo/botnet/5de12e48bcac561d73f4335bbed08d8eca5d993a005863828dce081155133442.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:57:27.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5de12e48bcac561d73f4335bbed08d8eca5d993a005863828dce081155133442`
- **SHA1:** `c708ae23d2a1a2c9f73f1f49c8a63e55c5360fe0`
- **MD5:** `a815a8c37db96b1524950f3d6f4e1e91`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 326 B |
| Entropía | 5.11 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.25.0 (linux-gnu)
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 185.228.26.XXX | static_analysis |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| hash | 5de12e48bcac561d73f4335bbed08d8eca5d993a005863828dce081155133442 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
