# 🧬 Payload Analysis

`388f3f601b4ca6600f8cd2013fc8cd4f21713d94d079e1e0a5df676fe0c1aa6b`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificó 1 comando observado o extraído. Se identificaron 3 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/388f3f601b4ca6600f8cd2013fc8cd4f21713d94d079e1e0a5df676fe0c1aa6b.md](../../../../../malware-like/oraculo/botnet/388f3f601b4ca6600f8cd2013fc8cd4f21713d94d079e1e0a5df676fe0c1aa6b.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `388f3f601b4ca6600f8cd2013fc8cd4f21713d94d079e1e0a5df676fe0c1aa6b`
- **SHA1:** `725c778379eaa3069bef6d76b11ba0481c351f38`
- **MD5:** `06e2bf0ef5e3a30c6b595a84f500dc9a`

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
| hash | 388f3f601b4ca6600f8cd2013fc8cd4f21713d94d079e1e0a5df676fe0c1aa6b | static_analysis |
| ip | 187.17.228.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | truncated download |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
