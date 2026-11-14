from django.db import models
from django.conf import settings

class Category(models.Model):
    name = models.CharField('Название', max_length=100, unique=True)
    description = models.TextField('Описание', blank=True)

    class Meta:
        db_table = 'categories'
        verbose_name = 'Категория'
        verbose_name_plural = 'Категории'

    def __str__(self):
        return self.name

class Order(models.Model):
    STATUS_CHOICES = [
        ('open', 'Открыт'),
        ('in_progress', 'В работе'),
        ('done', 'Завершён'),
        ('cancelled', 'Отменён'),
    ]

    customer = models.ForeignKey(
        settings.AUTH_USER_MODEL, 
        on_delete=models.CASCADE, 
        related_name='orders',
        verbose_name='Заказчик'
    )
    category = models.ForeignKey(
        Category, 
        on_delete=models.SET_NULL, 
        null=True, blank=True, 
        related_name='orders',
        verbose_name='Категория'
    )
    title = models.CharField('Название', max_length=200)
    description = models.TextField('Описание')
    budget = models.DecimalField('Бюджет', max_digits=10, decimal_places=2)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='open')
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        db_table = 'orders'
        ordering = ['-created_at']
        verbose_name = 'Заказ'
        verbose_name_plural = 'Заказы'

    def __str__(self):
        return self.title

class Response(models.Model):
    STATUS_CHOICES = [
        ('pending', 'Ожидает'),
        ('accepted', 'Принят'),
        ('rejected', 'Отклонён'),
    ]

    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='responses', verbose_name='Заказ')
    executor = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='responses', verbose_name='Исполнитель')
    message = models.TextField('Сообщение')
    proposed_budget = models.DecimalField('Предлагаемая стоимость', max_digits=10, decimal_places=2)
    status = models.CharField('Статус', max_length=20, choices=STATUS_CHOICES, default='pending')
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        db_table = 'responses'
        constraints = [
            models.UniqueConstraint(fields=['order', 'executor'], name='unique_order_executor')
        ]
        verbose_name = 'Отклик'
        verbose_name_plural = 'Отклики'

    def __str__(self):
        return f'Отклик на {self.order.title} от {self.executor.email}'

class Review(models.Model):
    order = models.ForeignKey(Order, on_delete=models.CASCADE, related_name='reviews', verbose_name='Заказ')
    author = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_written', verbose_name='Автор')
    recipient = models.ForeignKey(settings.AUTH_USER_MODEL, on_delete=models.CASCADE, related_name='reviews_received', verbose_name='Получатель')
    rating = models.IntegerField('Оценка')
    comment = models.TextField('Комментарий', blank=True)
    created_at = models.DateTimeField('Создано', auto_now_add=True)

    class Meta:
        db_table = 'reviews'
        verbose_name = 'Отзыв'
        verbose_name_plural = 'Отзывы'