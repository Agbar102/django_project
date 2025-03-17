from django.db import models

from ckeditor.fields import RichTextField

class Banner(models.Model):
    name = models.CharField("Имя", max_length=100)
    banner = models.ImageField(upload_to="tovar", verbose_name="Баннер", null=True, blank=True)
    link = models.URLField("ссылка", max_length=100, null=True, blank=False)

    class Meta:
        verbose_name = "Баннер"
        verbose_name_plural = "Баннеры"

    def __str__(self):
        return self.name



class User(models.Model ):
    name = models.CharField("Имя", max_length=100)
    phone_number = models.CharField("Номер телефона", max_length=12)

    class Meta:
        verbose_name = "Пользователь"
        verbose_name_plural = "Пользователи"

    def __str__(self):
        return self.name


class Category(models.Model):
    name = models.CharField("Название категории", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=1)

    class Meta:
        verbose_name = "Категория"
        verbose_name_plural = "Категории"
        ordering = ("order",)

    def __str__(self):
        return self.name


class Subcategory(models.Model):
    category = models.ForeignKey(Category, on_delete=models.SET_NULL, related_name="sub_categories", null=True)
    name = models.CharField("Название категории", max_length=100)
    order = models.PositiveIntegerField("Порядок", default=1)

    class Meta:
        verbose_name = "Подкатегория"
        verbose_name_plural = "Подкатегории"
        ordering = ("order",)

    def __str__(self):
        return self.name


class Item(models.Model):
    user = models.ManyToManyField(User, related_name="items")
    sub_category = models.ForeignKey(Subcategory, on_delete=models.CASCADE, related_name="items", null=True)
    image = models.ImageField(upload_to="tovar", verbose_name="Главная картинка товара", null=True, blank=True)
    title = models.CharField(verbose_name="Заголовок товара", max_length=255)
    description = models.TextField(verbose_name="Описание товара")
    price = models.DecimalField(verbose_name="Цена", max_digits=8, decimal_places=2)
    production = models.CharField(verbose_name="Производство", max_length=255)
    model = models.CharField(verbose_name="Модель", max_length=255)
    is_available = models.BooleanField(verbose_name="Наличие", default=False)
    color = models.CharField("Цвет", max_length=20)
    order = models.PositiveIntegerField("Порядок", default=1)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = "Товар"
        verbose_name_plural = "Товары"
        ordering = ("order",)


class Characteristic(models.Model):
    item = models.OneToOneField(Item, on_delete=models.CASCADE, related_name="characteristic")
    text = RichTextField("Текст характеристики")

    class Meta:
        verbose_name = "Характеристика"
        verbose_name_plural = verbose_name

    def __str__(self):
        return self.item.title

# class Contacts(models.Model):
#     location = models.CharField(verbose_name="Местоположения" , max_length=255)
#     time_work = models.TimeField(verbose_name="Время работы",default="Работаем с 09:00 до 18:00", max_length=255)
#     number_phone = models.CharField(verbose_name="Тел:", max_length=255)
#     gmai = models.CharField(verbose_name="Email:", max_length=255)
#
#     class Meta:
#         ordering = ['name']



