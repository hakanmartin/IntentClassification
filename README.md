# Niyet Tespiti

Bu proje, metinlerdeki niyetleri tespit etmek için kural tabanlı ve makine öğrenmesi modelleri (Naive Bayes ve SVM) kullanır. 

## İçindekiler

- [Kurulum](#kurulum)
- [Kullanım](#kullanım)
  - [Kural Tabanlı Niyet Tespiti](#kural-tabanlı-niyet-tespiti)
  - [Metin Verilerine Duygu Analizi Uygulama](#metin-verilerine-duygu-analizi-uygulama)
  - [Metin Verilerine Varlık Tanımlama](#metin-verilerine-varlık-tanımlama)
  - [Naive Bayes ile Model Eğitimi ve Testi](#naive-bayes-ile-model-eğitimi-ve-testi)
  - [SVM ile Model Eğitimi ve Testi](#svm-ile-model-eğitimi-ve-testi)
  - [SVM ile Eklenen Tüm Özelliklerle Modelin Eğitimi ve Testi](#svm-ile-eklenen-tüm-özelliklerle-modelin-eğitimi-ve-testi)
- [Projenin Temel Dosyaları](#projenin-temel-dosyaları)
- [Model Performansları](#model-performansları)
  - [Naive Bayes](#naive-bayes)
  - [SVM](#svm)

## Kurulum

1. Gerekli Python paketlerini yükleyin:
2. 
    ```bash
    pip install spacy pandas fuzzywuzzy scikit-learn seaborn matplotlib
    ```

3. SpaCy Türkçe modelini indirin:
4. 
    ```bash
    python -m spacy download tr_core_news_md
    ```

5. Excel dosyalarınızı projenin kök dizinine ekleyin:
    - `Niyet-Pattern.xlsx`
    - `Egitim-3972.xlsx`
    - `Test-1000.xlsx`
    - `Egitim-3972-4.xlsx`
    - `Test3-1000.xlsx`

## Kullanım

### Kural Tabanlı Niyet Tespiti

Kural tabanlı niyet tespiti için `niyettespiti4.py` dosyasını çalıştırın:

```bash
python niyettespiti4.py
```
Kullanıcıdan bir metin girdisi isteyerek niyeti tespit eder. Klavyeden 'q' harfi girilene kadar program çalışmaya devam eder.

### Metin verilerine Duygu Analizi uygulama

Duygu analizi için gerekli paketleri yükleyin.

```bash
    pip install transformers torch numpy warnings
```
Duygu analizi için kullanılan model: [duygu analiz](https://huggingface.co/cardiffnlp/twitter-xlm-roberta-base-sentiment)

Veri setinde bulunan Türkçe verilere duygu analizi uygulamak ve 'DA' kolonuna duygu deüerlerini yazdırmak için `DuyguAnaliz.py` dosyasını çalıştırın.

```bash
python DuyguAnaliz.py
```

### Metin verilerine Varlık Tanımlama

Varlık tanıma için gerekli paketleri yükleyin.

```bash
    pip install tqdm numpy
```

Veri setinde bulunan Türkçe verilere varlık tanımlaması uygulamak ve varlığın tanımlanmasına bağlı olarak 'NER' kolonuna 1 ya da 0 yazarak kayıt etmek için `ner1-0.py` dosyasını çalıştırın.

```bash
python ner1-0.py
```

Eğitim ve Test veri setlerine uygulamak için farklı dosyalar için iki kez çalıştırmayı düşünebilirsiniz.

### Naive Bayes ile Model Eğitimi ve Testi

Naive Bayes modeli ile niyet tespiti ve testi için `Naive.py` dosyasını çalıştırın.

```bash
python Naive.py
```

Modelin doğruluğunu ve performansını gösteren çıktılar üretir. Çıktı, Karmaşıklık Matrisi ile görselleştirilir.

### SVM ile Model Eğitimi ve Testi

SVM modeli ile niyet tespiti ve testi için `SVC.py` dosyasını çalıştırın.

```bash
python SVC.py
```

Naive Bayes modelinde de olduğu gibi modelin doğruluğunu ve performansını gösteren çıktılar üretir.

### SVM ile eklenen tüm özelliklerle modelin eğitimi ve testi

Veri setinin son hali ile SVM modelini eğitip test etmek ve sonuçları görüntülemek için `final.py` dosyasını çalıştırın. Bu aynı zamanda, makine öğrenme modeli ile niyet tespiti uygulamamızın son hali...

```bash
python final.py
```
Destek Vektör Makinesi Eğitim ve Test veri setlerinde belirlenen özellikler ile eğitilir ve test edilir. Doğruluk oranları bir tablo halinde yazdırılır. Ayrıntılı değerler Karmaşıklık Matrisi ile görselleştirilir.

## Projenin Temel Dosyaları
Projede bulunan farklı modeller, deneysel çalışmalar, ve uygulama hedefi ile doğrudan gerekliliği bulunmayan birçok dosya çıkarılmıştır. Uygulamanın hedefine doğrudan hizmet eden basitleştirilmiş dosyalar bunlardır:

- `niyettespiti4.py`: Kural tabanlı niyet tespiti.
- `DuyguAnaliz.py`: Türkçe verilere Duygu Analizi.
- `ner1-0.py`: Türkçe verilere SpaCy ile varlık tanımlama.
- `Naive.py`: Naive Bayes modeli ile niyet tespiti ve testi.
- `SVC.py`: SVM modeli ile niyet tespiti ve testi(yalnızca tf-idf vectörleştirme ile).
- `final.py`: SVM modeli ile modelin eğitimi ve testi.
- `Niyet-Pattern.xlsx`: Kural tabanlı niyet tespiti için kullanılan kalıplar.
- `Egitim-3972.xlsx`: Naive Bayes eğitimi için kullanılan veri seti.
- `Test-1000.xlsx`: Naive Bayes testi için kullanılan veri seti.
- `Egitim-3972-4.xlsx`: SVM eğitimi için kullanılan veri seti.
- `Test3-1000.xlsx`: SVM testi için kullanılan veri seti.

Bunlar dışındaki dosyalar deneyseldir. Deneysel sonuçlar için denenebilirler.

## Model Performansları

### Naive Bayes

Model doğruluğu ve diğer metrikler `Naive.py` dosyasında çalıştırıldıktan sonra gösterilir.

### SVM

Model doğruluğu ve diğer metrikler `SVC.py` dosyasında çalıştırıldıktan sonra gösterilir.
