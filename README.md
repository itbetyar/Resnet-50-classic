# ResNet-50 Képosztályozó | IT Betyár

Egyszerű oktatási célú AI modell minta képfelismerésre ResNet-50 architektúrával.

[![🚀 IT Betyár Demo](https://img.shields.io/badge/🚀_IT_Betyár-Élő_Demo-orange)](https://itbetyar.hu/project/computer-vision-resnet-50/)
[![🤗 Hugging Face](https://img.shields.io/badge/🤗_Hugging_Face-Space-yellow)](https://huggingface.co/spaces/itbetyar/3-Resnet-50-Classification)

[![🎓 Tanfolyam](https://img.shields.io/badge/🎓_AI_Tanfolyam-itbetyar.hu-green)](https://itbetyar.hu/mesterseges-intelligencia-fejleszto-tanfolyam/)

---

| Demo az itbetyar-on | Github project | Hugging Face demo |
| :--- | :--- | :---|

---

[![Hugging Face Space](https://img.shields.io/badge/🤗%20Hugging%20Face-Space-blue)](https://huggingface.co/spaces/itbetyar/3-Resnet-50-Classification)
[![Python 3.11](https://img.shields.io/badge/python-3.11-blue.svg)](https://www.python.org/downloads/)
[![License](https://img.shields.io/badge/license-MIT-green.svg)](LICENSE)

## 📖 Leírás

Ez a projekt egy **ResNet-50** konvolúciós neurális hálót használ képosztályozásra. A modell 1000 különböző kategóriát ismer fel az ImageNet adatbázis alapján - állatoktól kezdve tárgyakon és járműveken át mindenféle objektumot.

🔗 **Élő demo projektleírás:** [itbetyar.hu/project/computer-vision-resnet-50](https://itbetyar.hu/project/computer-vision-resnet-50/)

## 🎯 Funkciók

- **1000 kategória felismerése** - ImageNet adatbázis alapján
- **Top-5 predikció** - A legvalószínűbb osztályok megjelenítése valószínűségi értékekkel
- **Egyszerű felület** - Gradio-alapú webes interfész
- **Példaképek** - 8 tesztkép azonnal kipróbálható

## 🧠 Modell részletek

### Technikai specifikáció

| Paraméter | Érték |
|-----------|-------|
| **Modell típus** | CNN - Konvolúciós neurális háló (ResNet architektúra) |
| **Rétegszám** | 50 réteg (mély residuális háló) |
| **Paraméterek** | ~25.6 millió |
| **Modell fájlméret** | ~98 MB |
| **Tanító adatszett** | ImageNet (~1.2 millió kép, 1000 kategória) |
| **Algoritmus** | ResNet-50 (Residual Network - skip connection) |
| **Számítási igény** | ~4.1 GFLOP |

### Mai viszonyítás

<table>
  <thead>
    <tr>
      <th>Modell</th>
      <th>Év</th>
      <th>Rétegszám</th>
      <th>Paraméterek</th>
    </tr>
  </thead>
  <tbody>
    <tr>
      <td><strong>ResNet-50</strong></td>
      <td>2015</td>
      <td>50 réteg</td>
      <td>~25 millió</td>
    </tr>
    <tr>
      <td><strong>GPT-4</strong></td>
      <td>2023</td>
      <td>120+ transformer réteg</td>
      <td>~1.7 trillió</td>
    </tr>
    <tr>
      <td><strong>Stable Diffusion</strong></td>
      <td>2022</td>
      <td>-</td>
      <td>~890 millió</td>
    </tr>
    <tr>
      <td><strong>Vision Transformer (ViT-Giant)</strong></td>
      <td>2021</td>
      <td>48 réteg</td>
      <td>~2 milliárd</td>
    </tr>
  </tbody>
</table>

**Összefoglalva:** A ResNet-50 ma már "klasszikus" modellnek számít - hatékony, gyors, de a modern AI modellek 100-1000x nagyobbak. Oktatásra/demo-ra viszont tökéletes! 🎯

## 🚀 Történet

**Készítette:** Microsoft Research Asia, 2015  

A ResNet (Residual Network) forradalmasította a deep learning világát az úgynevezett **skip connection** (átugrási kapcsolat) technológiával, amely megoldotta a nagyon mély neurális hálók tanításának problémáját.

## 🛠️ Telepítés és futtatás

### Követelmények

- Python 3.11
- pip package manager

### Függőségek telepítése
```bash
