# Image Processing




## Normalizasyon ve Standartizasyon Farkı

----------------------------------------------

## Normalizasyon

**Amaç:** Görüntü piksel değerlerini belirli bir aralığa ölçeklendirmek.

**Kullanım:**
- Veri setindeki piksel değerlerini genellikle [0, 1] aralığına getirir. Bu, bir pikselin en karanlık (siyah) ile en parlak (beyaz) arasındaki oranı korur.
- Özellikle derin öğrenme modellerinde, normalizasyon kullanılarak eğitim sürecini daha etkili hale getirebilir, çünkü genellikle bu modeller, [0, 1] aralığında ölçeklenmiş veri setlerini daha iyi işler.

## Standartizasyon

**Amaç:** Görüntü piksel değerlerini belirli bir ortalama ve standart sapma etrafında standart hale getirmek.

**Kullanım:**
- Piksel değerlerini genellikle ortalama değeri 0 ve standart sapma değeri 1 olacak şekilde standartlaştırır.
- Standartlaştırma, piksel değerlerinin birbirine göre sapmalarını düzeltir ve görüntüdeki kontrastı artırabilir.
- Standartlaştırma, bazı görüntü işleme uygulamalarında, özellikle daha geleneksel yöntemlerde ve bazı özel durumlarda kullanılabilir.
