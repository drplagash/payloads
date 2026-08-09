# 🧬 Payload Analysis

`ee2b228e00d95d3d1bf03db2579c9d4340173be123db83a718f7ebc1930c854d`

## 📌 Resumen

Artefacto de 198 B. Formato identificado como ASCII text, with CRLF line terminators. Entropía registrada: 5.09. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Descarga remota. Se identificaron 2 comandos observados o extraídos. Se identificaron 4 indicadores técnicos.


## 🏷️ Clasificación

- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:38:58.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ee2b228e00d95d3d1bf03db2579c9d4340173be123db83a718f7ebc1930c854d`
- **MD5:** `ba0bf8bab96b77374a912115cc8ab788`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 198 B |
| Entropía | 5.09 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
User-Agent: Wget/1.25.0 (linux-gnu)
User-Agent: curl/7.38.0
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 41.216.189.XXX | static_analysis |
| command | User-Agent: Wget/1.25.0 (linux-gnu) | strings |
| command | User-Agent: curl/7.38.0 | strings |
| hash | ee2b228e00d95d3d1bf03db2579c9d4340173be123db83a718f7ebc1930c854d | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
